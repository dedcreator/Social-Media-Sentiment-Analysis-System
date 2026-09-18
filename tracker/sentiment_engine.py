import re
import logging

logger = logging.getLogger(__name__)

# Try to initialize VADER
_vader_analyzer = None

def get_vader():
    global _vader_analyzer
    if _vader_analyzer is None:
        try:
            import nltk
            try:
                from nltk.sentiment.vader import SentimentIntensityAnalyzer
                _vader_analyzer = SentimentIntensityAnalyzer()
            except LookupError:
                # Fix for macOS / proxy environments where SSL certificate verification fails for NLTK
                try:
                    import ssl
                    try:
                        import certifi
                        ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())
                    except Exception:
                        ssl._create_default_https_context = ssl._create_unverified_context
                except Exception:
                    pass
                try:
                    nltk.download('vader_lexicon', quiet=True)
                except Exception as dl_err:
                    # Fallback to unverified SSL context if verified download failed
                    try:
                        import ssl
                        ssl._create_default_https_context = ssl._create_unverified_context
                        nltk.download('vader_lexicon', quiet=True)
                    except Exception as fallback_err:
                        logger.error(f"Failed to download NLTK vader_lexicon: {fallback_err}")
                from nltk.sentiment.vader import SentimentIntensityAnalyzer
                _vader_analyzer = SentimentIntensityAnalyzer()
        except Exception as e:
            logger.error(f"Failed to initialize VADER: {e}")
            _vader_analyzer = None
    return _vader_analyzer


# Lazy load Transformers pipeline
_transformer_pipeline = None
_transformer_load_attempted = False

def get_transformer_pipeline():
    global _transformer_pipeline, _transformer_load_attempted
    if _transformer_pipeline is None and not _transformer_load_attempted:
        _transformer_load_attempted = True
        try:
            from transformers import pipeline
            # Use a lightweight, robust sentiment pipeline
            _transformer_pipeline = pipeline(
                "sentiment-analysis",
                model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
                truncation=True,
                max_length=512
            )
            logger.info("Transformers pipeline loaded successfully.")
        except Exception as e:
            logger.warning(f"Could not load Transformers model: {e}. Falling back to VADER.")
            _transformer_pipeline = None
    return _transformer_pipeline


def clean_text_for_sentiment(text: str) -> str:
    """Cleans URLs and excessive whitespace while keeping emojis and punctuation."""
    if not text:
        return ""
    # Remove URL links
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    # Normalize multiple whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def analyze_with_vader(text: str) -> dict:
    """Analyze text using NLTK VADER sentiment analyzer."""
    sia = get_vader()
    if not sia:
        # Fallback if VADER fails
        return {
            'label': 'Neutral',
            'score': 0.0,
            'pos': 0.0,
            'neu': 1.0,
            'neg': 0.0,
            'engine': 'Fallback'
        }

    cleaned = clean_text_for_sentiment(text)
    scores = sia.polarity_scores(cleaned or text)
    compound = scores['compound']

    # Standard VADER classification thresholds
    if compound >= 0.05:
        label = 'Positive'
    elif compound <= -0.05:
        label = 'Negative'
    else:
        label = 'Neutral'

    return {
        'label': label,
        'score': round(compound, 3),
        'pos': round(scores['pos'], 3),
        'neu': round(scores['neu'], 3),
        'neg': round(scores['neg'], 3),
        'engine': 'VADER'
    }


def analyze_with_transformers(text: str) -> dict:
    """Analyze text using Hugging Face Transformers pipeline (with automatic VADER fallback)."""
    pipe = get_transformer_pipeline()
    if pipe is None:
        # Fall back to VADER smoothly
        result = analyze_with_vader(text)
        result['engine'] = 'VADER (Transformers fallback)'
        return result

    cleaned = clean_text_for_sentiment(text)
    try:
        res = pipe(cleaned or text)[0]
        # DistilBERT outputs: 'POSITIVE' or 'NEGATIVE' with a score
        raw_label = res['label'].upper()
        conf = float(res['score'])

        if 'POS' in raw_label:
            label = 'Positive'
            compound = conf
            pos_score = conf
            neg_score = 1.0 - conf
            neu_score = 0.0
        elif 'NEG' in raw_label:
            label = 'Negative'
            compound = -conf
            pos_score = 1.0 - conf
            neg_score = conf
            neu_score = 0.0
        else:
            label = 'Neutral'
            compound = 0.0
            pos_score = 0.0
            neg_score = 0.0
            neu_score = 1.0

        return {
            'label': label,
            'score': round(compound, 3),
            'pos': round(pos_score, 3),
            'neu': round(neu_score, 3),
            'neg': round(neg_score, 3),
            'engine': 'Transformers/BERT'
        }
    except Exception as e:
        logger.warning(f"Error during Transformers sentiment inference: {e}. Using VADER.")
        result = analyze_with_vader(text)
        result['engine'] = 'VADER (Transformers error)'
        return result


def analyze_post_sentiment(text: str, engine: str = 'VADER') -> dict:
    """Main entrypoint for sentiment analysis. Supports 'VADER' or 'TRANSFORMERS'."""
    if engine and engine.upper() in ('TRANSFORMERS', 'BERT', 'TRANSFORMERS/BERT'):
        return analyze_with_transformers(text)
    return analyze_with_vader(text)
