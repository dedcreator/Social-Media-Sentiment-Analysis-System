# 🗳️ 2027 Gubernatorial Election Sentiment Analysis System

An end-to-end Social Media Sentiment Analysis and Monitoring platform designed for the **2027 Gubernatorial Elections**. The system monitors public political sentiment across **X (Twitter)**, **Facebook**, **YouTube Comments**, and **News Comment Sections**, categorizing posts into **Positive**, **Negative**, or **Neutral**, tracking candidate perception metrics, and rendering interactive dashboards and word clouds.

---

## 🚀 Key Features

1. **Multi-Source Automated Post Collection**:
   - Collects election-related posts from **X (Twitter)**, **Facebook**, **YouTube Comments**, and **News Comment Sections**.
   - Supports both real-time API integrations (`TWITTER_BEARER_TOKEN`, `YOUTUBE_API_KEY`) and automated realistic web/data collection simulations.
   - Intelligent Named Entity Recognition (NER) matching candidate aliases, keywords, and state races automatically.

2. **Dual-Engine Sentiment Classification**:
   - **NLTK VADER**: Specially tuned for social media slang, emojis, exclamation marks, and capitalization.
   - **Hugging Face Transformers / BERT**: Deep contextual sentiment classification (`distilbert-base-uncased-finetuned-sst-2-english`) with automated fallback.
   - Polarity scores (-1.0 to +1.0) and confidence metrics (pos, neu, neg breakdown).

3. **Candidate Reaction Analytics & Leaderboards**:
   - Computes **Net Sentiment Index** (`% Positive - % Negative`).
   - Identifies the **Most Positively Perceived Candidate**, the **Most Criticized Candidate**, and candidate with the **Highest Social Buzz**.
   - Stacked visual comparison bars and dedicated candidate profile pages.

4. **Sentiment Trends Over Time**:
   - Interactive time-series area charts tracking daily trajectories of Positive, Negative, and Neutral posts.
   - Filterable by State/Race, Candidate, Platform, Sentiment, and Time Window (7d, 14d, 30d, All Time).

5. **Dynamic Word Clouds & Topic Extraction**:
   - Generates high-resolution Word Clouds with dark slate theme.
   - Filterable dynamically via AJAX by:
     - **All Words**
     - **Positive Words Only** (Praise, vision, manifestos)
     - **Negative Words Only** (Critiques, grievances, challenges)
   - Frequency pill tags displaying word weights and counts.

6. **Interactive Dashboard & NLP Sandbox**:
   - Modern, responsive Dark/Slate Glassmorphism UI built with Tailwind CSS & Chart.js.
   - **One-Click Live Collector**: Ingest new posts from any platform directly from the top bar.
   - **Live NLP Classifier Sandbox**: Test custom text or quotes live in real-time with instant polarity feedback.
   - **CSV Export**: Download filtered post datasets for researchers.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.11, Django 4.2
- **Database**: PostgreSQL (with automatic zero-config SQLite fallback for development)
- **NLP / ML**: NLTK VADER, Hugging Face Transformers, PyTorch, Scikit-Learn
- **Visualization**: Chart.js, WordCloud, Matplotlib, Plotly
- **Frontend**: HTML5, Tailwind CSS, FontAwesome 6, Vanilla JS (AJAX)

---

## 📦 Project Structure

```
.
├── manage.py
├── requirements.txt
├── .env.example
├── election_sentiment/          # Django project configuration
│   ├── settings.py              # DB settings (Postgres/SQLite), Static & Media
│   ├── urls.py                  # Main URL routing
│   └── wsgi.py
├── tracker/                     # Main election sentiment application
│   ├── models.py                # StateRace, Candidate, SocialPost, CollectionJob
│   ├── sentiment_engine.py      # Dual VADER & Transformers/BERT classifier
│   ├── collectors.py            # Multi-platform post collection & entity matching
│   ├── analytics.py             # Word clouds, trends, platform & candidate summaries
│   ├── views.py                 # Dashboard, candidate detail, AJAX endpoints
│   ├── urls.py                  # Tracker routes
│   ├── admin.py                 # Django Admin configurations
│   ├── tests.py                 # Unit & integration test suite (12 tests)
│   └── management/commands/
│       ├── seed_election_data.py    # Seed realistic 2027 election data
│       └── collect_election_posts.py# Background / cron collector command
└── templates/
    ├── base.html                # Navigation, modals, dark UI layout
    └── tracker/
        ├── dashboard.html       # Interactive dashboard with charts & word clouds
        └── candidate_detail.html# Dedicated candidate analytics profile
```

---

## ⚡ Quickstart Guide

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Database
By default, the application runs immediately with SQLite (`db.sqlite3`).

To use **PostgreSQL**, set environment variables or create a `.env` file:
```bash
export POSTGRES_DB=election_sentiment_db
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=your_password
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
```

### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Seed Initial 2027 Election Data
Populate realistic candidates (Lagos, Rivers, Kano, Oyo, etc.) and multi-platform election posts:
```bash
python manage.py seed_election_data --count 200
```

### 5. Start the Development Server
```bash
python manage.py runserver
```
Visit: **`http://127.0.0.1:8000/`**

---

## 🤖 Automated Background Collection

To run automated periodic collection in the background:
```bash
# Run a single batch collection across all platforms
python manage.py collect_election_posts --platform ALL --count 15 --engine VADER

# Run continuous collection daemon every 60 seconds
python manage.py collect_election_posts --continuous --interval 60 --count 10
```

You can also trigger batch collections live from the web dashboard using the **"Collect Live Posts"** button in the top navigation!

---

## 🧪 Running Tests

Execute the automated test suite:
```bash
python manage.py test
```
All 12 unit and integration tests verify sentiment scoring, candidate metrics, collectors, word cloud generation, and HTTP/AJAX endpoints.
