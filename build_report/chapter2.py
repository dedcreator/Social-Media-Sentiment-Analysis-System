import docx
from docx.shared import Pt
from .helpers import add_heading_1, add_heading_2, add_heading_3, add_body_p, add_bullet_p, add_styled_table

def add_chapter_two(doc):
    add_heading_1(doc, "CHAPTER TWO", align_center=True, space_before=18, space_after=4)
    add_heading_1(doc, "LITERATURE REVIEW", align_center=True, space_before=0, space_after=18)

    # 2.1 Introduction
    add_heading_2(doc, "2.1 Introduction")
    p1 = (
        "The explosive growth of user-generated content across the internet has catalyzed a profound paradigm shift in how public "
        "sentiment, social attitudes, and political allegiances are monitored and analyzed. As modern democratic contests become increasingly "
        "intertwined with digital communication networks, sentiment analysis has emerged as an indispensable multidisciplinary discipline "
        "straddling computer science, artificial intelligence, computational linguistics, and political sociology. This chapter presents "
        "an exhaustive review of relevant literature, establishing the theoretical foundations of sentiment analysis, contrasting lexicon-based "
        "and deep learning paradigms, evaluating social media's role in democratic elections, critically examining existing commercial "
        "and academic election monitoring systems, and identifying the specific research gaps that motivate the proposed system."
    )
    add_body_p(doc, p1)

    # 2.2 Theoretical Foundations
    add_heading_2(doc, "2.2 Theoretical Foundations of Natural Language Processing and Sentiment Analysis")
    p2 = (
        "Natural Language Processing (NLP) is a foundational branch of Artificial Intelligence concerned with enabling computational "
        "agents to read, decipher, understand, and derive meaningful insights from human languages. Within NLP, Sentiment Analysis "
        "(frequently termed Opinion Mining) specifically focuses on the computational treatment of opinion, sentiment, subjectivity, and "
        "affect in textual corpora (Pang and Lee, 2008). Sentiment analysis tasks are conventionally categorized across three granular levels: "
        "document-level analysis (evaluating whether an entire document expresses an overall positive or negative opinion), sentence-level "
        "analysis (determining the polarity of individual sentences), and aspect-level or entity-level analysis (identifying the specific "
        "target or entity—such as a political candidate—and determining the exact sentiment directed toward that entity)."
    )
    add_body_p(doc, p2)

    # 2.2.1 Lexicon-Based
    add_heading_3(doc, "2.2.1 Lexicon-Based Sentiment Scoring Paradigms")
    p3 = (
        "The foundational era of computational sentiment classification relied heavily upon lexicon-based methodologies. A sentiment "
        "lexicon is essentially a structured dictionary of words, terms, and idioms, where each entry is pre-annotated with a semantic "
        "orientation and numerical valence score. Prominent classical lexicons include the General Inquirer (Stone et al., 1966), "
        "WordNet-Affect (Strapparava and Valitutti, 2004), and SentiWordNet (Baccianella et al., 2010), which assign positive and negative "
        "objective scores to synsets."
    )
    add_body_p(doc, p3)

    p4 = (
        "While traditional lexicons perform reasonably well on formal, grammatically curated prose (such as editorial reviews), "
        "they exhibit severe limitations when applied to the informal, unstructured, and colloquial nature of social media communication. "
        "Microblog posts are characterized by irregular capitalization, intentional typographical elongations (e.g., 'coooool'), "
        "exclamation mark repetitions ('!!!'), internet acronyms ('lol', 'smh'), and rich Unicode emojis. To resolve these limitations, "
        "Hutto and Gilbert (2014) engineered VADER (Valence Aware Dictionary and sEntiment Reasoner). VADER introduces a gold-standard "
        "sentiment lexicon specifically tuned to microblogging and social media discourse, incorporating five generalizable grammatical "
        "and syntactical heuristics:"
    )
    add_body_p(doc, p4)

    add_bullet_p(doc, "Punctuation marks—particularly the exclamation mark (!)—amplify sentiment intensity without modifying polarity direction.", bold_prefix="1. Punctuation Emphasis: ")
    add_bullet_p(doc, "Words in ALL CAPS in the presence of non-capitalized words systematically boost sentiment intensity (e.g., 'GREAT' vs. 'great').", bold_prefix="2. Capitalization Heuristic: ")
    add_bullet_p(doc, "Degree adverbs or booster words (e.g., 'extremely', 'scarcely', 'slightly') dynamically scale the valence intensity of subsequent terms.", bold_prefix="3. Degree Modifiers: ")
    add_bullet_p(doc, "Contrastive conjunctions (specifically 'but') shift sentiment orientation, assigning dominant weight to the clause following the conjunction.", bold_prefix="4. Contrastive Conjunctions: ")
    add_bullet_p(doc, "Examining tri-gram windows preceding lexical terms to detect negation words (e.g., 'not', 'never', 'hardly'), which invert or attenuate polarity.", bold_prefix="5. Tri-gram Negation Handling: ")

    p5 = (
        "The primary advantages of VADER are its near-zero computational latency (processing thousands of sentences per second on a "
        "single CPU core), absolute determinism, and complete independence from massive training datasets. However, VADER remains constrained "
        "by its inability to capture long-range contextual semantic dependencies and nuanced political sarcasm."
    )
    add_body_p(doc, p5)

    # 2.2.2 Machine Learning and Transformers
    add_heading_3(doc, "2.2.2 Machine Learning and Deep Contextual Transformers (BERT & DistilBERT)")
    p6 = (
        "To surpass the limitations of rigid lexicon matching, researchers transitioned toward statistical Machine Learning (ML) classifiers "
        "—such as Naive Bayes, Support Vector Machines (SVM), and Logistic Regression—operating on n-gram and Term Frequency-Inverse "
        "Document Frequency (TF-IDF) feature vectors (Medhat et al., 2014). While statistical classifiers capture statistical word "
        "co-occurrences, they treat text as an unordered 'bag-of-words', entirely discarding word order, grammatical structure, and "
        "contextual polysemy (where a single word assumes different meanings depending on surrounding context)."
    )
    add_body_p(doc, p6)

    p7 = (
        "The watershed breakthrough in NLP occurred with the introduction of the Transformer architecture by Vaswani et al. (2017), "
        "which dispensed with recurrence and convolutions in favor of multi-head self-attention mechanisms. Building upon this foundation, "
        "Devlin et al. (2019) at Google AI introduced BERT (Bidirectional Encoder Representations from Transformers). Unlike prior language "
        "models (such as Word2Vec, GloVe, or standard LSTMs) that processed text unidirectionally (left-to-right or right-to-left), "
        "BERT pre-trains deep bidirectional representations by jointly conditioning on both left and right context across all layers using "
        "Masked Language Modeling (MLM) and Next Sentence Prediction (NSP)."
    )
    add_body_p(doc, p7)

    p8 = (
        "Despite its extraordinary benchmark performance, full BERT models (such as BERT-base with 110 million parameters) impose severe "
        "computational burdens, demanding substantial GPU memory and exhibiting high inference latency that complicates real-time web deployment. "
        "To democratize transformer deployment, Sanh et al. (2019) developed DistilBERT, an innovative knowledge distillation framework. "
        "DistilBERT compresses the BERT architecture by 40% while preserving 97% of its full downstream language comprehension capabilities "
        "and running 60% faster during inference. In this project, a fine-tuned DistilBERT model (distilbert-base-uncased-finetuned-sst-2-english) "
        "is integrated to provide deep contextual sentiment classification, complemented by automatic fallback to NLTK VADER."
    )
    add_body_p(doc, p8)

    # 2.3 Social Media in Elections
    add_heading_2(doc, "2.3 Social Media as a Public Opinion Sphere in Modern Elections")
    p9 = (
        "The digital public sphere concept—originally formulated by philosopher Jürgen Habermas—has found a vibrant contemporary manifestation "
        "in social media networks. Microblogging and social networking services provide unmediated platforms where citizens actively "
        "participate in political debates, hold leaders accountable, and mobilize collective electoral action (Loader and Mercea, 2011). "
        "In democratic elections worldwide, social media analytics have repeatedly demonstrated predictive and explanatory power regarding "
        "voter preferences (Tumasjan et al., 2010; Ceron et al., 2014)."
    )
    add_body_p(doc, p9)

    p10 = (
        "In the Nigerian electoral landscape, social media has redefined civic participation. Beginning prominently with the 2011 General "
        "Elections and accelerating through the 2015, 2019, and 2023 electoral cycles, platforms like X, YouTube, and Facebook have served "
        "as central command posts for political discourse. During the 2023 Nigerian elections, youth voter turnout and digital mobilization "
        "reached historic peaks, driven by digital campaigns, viral town hall excerpts, and citizen-led election oversight. For the upcoming "
        "2027 Gubernatorial races, social media chatter represents the frontline of electoral perception, reflecting real-time voter reactions "
        "to candidate manifestos, debates, and local developmental track records across states like Lagos, Kano, Rivers, and Oyo."
    )
    add_body_p(doc, p10)

    # 2.4 Review of Existing Systems
    add_heading_2(doc, "2.4 Review of Existing Sentiment Analysis Systems and Election Monitoring Platforms")
    p11 = (
        "Existing commercial and academic systems for media monitoring and political sentiment tracking fall broadly into two categories: "
        "commercial enterprise media intelligence platforms and domain-specific academic research prototypes."
    )
    add_body_p(doc, p11)

    p12 = (
        "Commercial enterprise platforms—such as Brandwatch Consumer Research, Meltwater, Sprout Social, and Hootsuite Enterprise—offer "
        "broad social listening capabilities across global brands. While powerful, these platforms exhibit significant drawbacks in the "
        "context of African electoral monitoring: they charge exorbitant annual licensing fees (frequently exceeding $15,000 to $40,000 USD), "
        "operate as closed-source proprietary systems with zero visibility into classification algorithms, lack specialized Named Entity "
        "Recognition for local Nigerian candidate aliases, and offer no live interactive NLP sandboxes where researchers can inspect "
        "model decision boundaries."
    )
    add_body_p(doc, p12)

    p13 = (
        "On the other hand, academic research prototypes developed in university laboratories (e.g., US 2020 Twitter trackers, Kenya 2022 "
        "election monitors) typically consist of ad-hoc Jupyter Notebook scripts or static offline analysis. These prototypes suffer from "
        "lack of persistent database architectures, absence of user-friendly interactive web dashboards, dependence on single fragile "
        "classification engines with no fallback redundancy, and complete inability to perform continuous automated data collection in the background."
    )
    add_body_p(doc, p13)

    # 2.5 Comparative Analysis Table
    add_heading_2(doc, "2.5 Comparative Analysis of Existing Methodologies")
    p14 = (
        "To systematically evaluate the state of the art and elucidate the technical positioning of the proposed system, "
        "Table 2.1 presents a comprehensive comparative analysis across key architectural, algorithmic, and operational criteria."
    )
    add_body_p(doc, p14)

    headers_2_1 = ["Evaluation Dimension", "Brandwatch Enterprise", "Meltwater Listening", "Sprout Social", "Academic Prototype", "Proposed Election System"]
    rows_2_1 = [
        ["System Architecture", "Cloud SaaS (Proprietary)", "Cloud SaaS (Proprietary)", "Cloud SaaS (Proprietary)", "Standalone Jupyter Script", "Decoupled 4-Tier Web App"],
        ["Underlying Framework", "Proprietary Java/Scala", "Proprietary Microservices", "Proprietary Cloud API", "Ad-hoc Python Scripts", "Python 3.11 / Django 4.2"],
        ["NLP Classification Engine", "Proprietary ML Classifier", "Generic Sentiment API", "Rule-based + Basic ML", "Single Lexicon (VADER/TextBlob)", "Dual-Engine (VADER + DistilBERT)"],
        ["Multi-Source Support", "Twitter, FB, Instagram", "News, Twitter, Web", "Twitter, FB, LinkedIn", "Twitter only (CSV upload)", "X, YouTube, FB, RSS Feeds"],
        ["Candidate Entity Matching", "Manual Keyword Rules", "Manual Query Strings", "Manual Search Terms", "Hardcoded String Find", "Dynamic Database NER Alias Map"],
        ["Automated Redundancy", "SLA Failover Only", "SLA Failover Only", "None", "None (Fails on Error)", "Automated Fallback to VADER"],
        ["Real-time NLP Sandbox", "Not Available", "Not Available", "Not Available", "Not Available", "Interactive Live Sandbox UI"],
        ["Dynamic Topic WordCloud", "Static Cloud Charts", "Static Word Lists", "Keyword Clusters", "Basic Matplotlib script", "AJAX-Filtered (All/Pos/Neg)"],
        ["Cost and Accessibility", "Prohibitive ($15k-$40k/yr)", "Prohibitive ($12k+/yr)", "Prohibitive ($3k-$10k/yr)", "Free / Non-Functional", "Open Source / Zero Cost (SQLite)"]
    ]
    col_w_2_1 = [1.4, 1.0, 1.0, 1.0, 1.0, 1.3]
    add_styled_table(doc, "Table 2.1: Comparative Analysis of Existing Sentiment Analysis and Election Monitoring Platforms", headers_2_1, rows_2_1, col_w_2_1)

    # 2.6 Identified Gaps
    add_heading_2(doc, "2.6 Identified Research Gaps and Proposed System Contribution")
    p15 = (
        "The comparative analysis in Table 2.1 clearly reveals critical research and engineering gaps in current election sentiment platforms:"
    )
    add_body_p(doc, p15)

    add_bullet_p(doc, "Existing academic and commercial systems operate on a rigid single-engine paradigm. When transformer models encounter memory exhaustion or latency spikes, systems fail entirely. Conversely, pure lexicon tools fail on complex syntax. The literature lacks a unified dual-engine architecture capable of seamlessly executing fast lexicon scoring while providing deep transformer contextual classification with automated fallback.", bold_prefix="Gap 1: Absence of Resilient Dual-Engine Hybrid Architectures: ")
    add_bullet_p(doc, "Standard sentiment tools treat text generically, failing to associate sentiment with specific candidate entities, political aliases, and state races within a structured relational database.", bold_prefix="Gap 2: Lack of Specialized Nigerian Candidate NER Mapping: ")
    add_bullet_p(doc, "Commercial tools are cost-prohibitive for Nigerian universities, independent election observers, and local civic organizations, while open-source tools lack end-to-end user interfaces, database persistence, and automated background collectors.", bold_prefix="Gap 3: Prohibitive Commercial Costs and Disconnected Academic Scripts: ")
    add_bullet_p(doc, "Existing systems offer no interactive sandbox interface where election analysts can input arbitrary candidate quotes, manifesto excerpts, or citizen statements to immediately inspect model predictions, confidence distributions, and engine behaviors.", bold_prefix="Gap 4: Absence of Live Interactive NLP Verification Sandboxes: ")

    p16 = (
        "The system engineered in this project directly resolves each of these identified gaps, providing an accessible, robust, "
        "open-source, dual-engine sentiment analysis and candidate perception monitoring platform designed specifically for the "
        "2027 Gubernatorial Elections in Nigeria."
    )
    add_body_p(doc, p16)

    doc.add_page_break()
