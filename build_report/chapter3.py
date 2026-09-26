import docx
from docx.shared import Pt
from .helpers import add_heading_1, add_heading_2, add_heading_3, add_body_p, add_bullet_p, add_styled_table

def add_chapter_three(doc):
    add_heading_1(doc, "CHAPTER THREE", align_center=True, space_before=18, space_after=4)
    add_heading_1(doc, "RESEARCH METHODOLOGY", align_center=True, space_before=0, space_after=18)

    # 3.1 Introduction
    add_heading_2(doc, "3.1 Introduction and Proposed System Framework")
    p1 = (
        "This chapter establishes the research methodology, engineering paradigms, architectural blueprints, and algorithmic "
        "frameworks governing the design and implementation of the Social Media Sentiment Analysis and Election Monitoring Platform. "
        "Developing an enterprise-grade computational platform capable of processing thousands of multi-source unstructured social posts, "
        "executing dual-engine NLP classification, maintaining relational integrity, and rendering real-time interactive visual analytics "
        "demands a rigorous, iterative software engineering methodology. The following sections outline the Agile Scrum framework, "
        "detail the multi-tier system architecture, describe the data ingestion and Named Entity Recognition (NER) pipeline, explain "
        "the dual-engine sentiment classification mathematical logic, present system modeling artifacts, and justify the technology stack."
    )
    add_body_p(doc, p1)

    # 3.2 Agile Scrum Framework
    add_heading_2(doc, "3.2 System Development Life Cycle: Agile Scrum Framework")
    p2 = (
        "To ensure continuous stakeholder feedback, rapid prototyping, modular code decoupledness, and systematic risk mitigation, "
        "the Agile Scrum software development lifecycle framework was adopted. In contrast to rigid traditional Waterfall methodologies "
        "—which defer integration and testing to the terminal phases of development—Agile Scrum organizes development into discrete, "
        "time-boxed iterations called Sprints, typically spanning two weeks each (Schwaber and Sutherland, 2020)."
    )
    add_body_p(doc, p2)

    p3 = (
        "The project execution was organized into six distinct, two-week Sprints across a twelve-week development cycle, as detailed "
        "in Table 3.1. Each sprint incorporated sprint planning, daily progress reviews, continuous test-driven implementation, "
        "sprint reviews, and retrospective adjustments."
    )
    add_body_p(doc, p3)

    headers_3_1 = ["Sprint ID", "Sprint Focus & Domain", "Key Engineering Deliverables", "Timeline", "Status"]
    rows_3_1 = [
        ["Sprint 1", "Requirements & Relational Models", "System requirements specification, Django 4.2 project scaffold, StateRace & Candidate relational schemas, SQLite/PostgreSQL configuration", "Weeks 1 - 2", "Completed"],
        ["Sprint 2", "Multi-Source Ingestion & NER", "Automated collectors for Twitter API v2, YouTube Data API v3, Nigerian news RSS feeds (Punch, Vanguard, Daily Post), NER candidate alias dictionary", "Weeks 3 - 4", "Completed"],
        ["Sprint 3", "Dual-Engine NLP Pipeline", "NLTK VADER integration with social slang/emojis heuristics, Hugging Face DistilBERT fine-tuning pipeline, automated fallback failover controller", "Weeks 5 - 6", "Completed"],
        ["Sprint 4", "Interactive Dashboard & Visuals", "Tailwind CSS dark glassmorphism layout, Chart.js time-series sentiment area charts, Candidate Net Sentiment Index leaderboards, state/race filters", "Weeks 7 - 8", "Completed"],
        ["Sprint 5", "Word Clouds & Live NLP Sandbox", "Dynamic topic WordCloud generation (AJAX-filtered: All/Pos/Neg), live interactive NLP sandbox modal, automated background collection management command", "Weeks 9 - 10", "Completed"],
        ["Sprint 6", "Testing, Evaluation & Documentation", "Execution of 21 automated unit/integration test suite, confusion matrix benchmarking, performance latency profiling, comprehensive project report compilation", "Weeks 11 - 12", "Completed"]
    ]
    col_w_3_1 = [0.9, 1.4, 2.5, 0.9, 0.8]
    add_styled_table(doc, "Table 3.1: Agile Scrum Sprint Roadmap & Development Iterations", headers_3_1, rows_3_1, col_w_3_1)

    # 3.3 Multi-Tier Architecture
    add_heading_2(doc, "3.3 Proposed Multi-Tier System Architecture")
    p4 = (
        "To achieve high cohesion, loose coupling, horizontal scalability, and ease of maintenance, the system is architectured "
        "into four distinct operational tiers: Data Ingestion & External Sources Tier, Dual-Engine NLP & Classification Tier, "
        "Data Storage & Persistence Tier, and Presentation & Visual Analytics Tier."
    )
    add_body_p(doc, p4)

    add_bullet_p(doc, "Interfaces with external social media platforms and news providers. It encapsulates multi-platform API clients (Twitter API v2, YouTube Data API v3), XML RSS feed parsers for reputable Nigerian dailies (Punch, Vanguard, Daily Post, Google News Nigeria), and an automated realistic post simulation generator. It incorporates SSL certificate verification fallback adapters to guarantee continuous data ingestion even in restrictive proxy or network environments.", bold_prefix="1. Data Ingestion & External Sources Tier: ")
    add_bullet_p(doc, "The core intelligence layer responsible for textual normalization, Named Entity Recognition, and sentiment scoring. It houses the dual classification engines: NLTK VADER (lexicon-based) and Hugging Face DistilBERT (deep learning transformer). The engine router dynamically routes text to the appropriate model and manages automatic failover redundancy.", bold_prefix="2. Dual-Engine NLP & Classification Tier: ")
    add_bullet_p(doc, "Managed via Django's Object-Relational Mapper (ORM), supporting seamless dual-engine database operation. In development environments, it utilizes a zero-configuration SQLite3 engine (db.sqlite3); in production environments, it connects transparently to an enterprise PostgreSQL relational database. It maintains relational integrity across StateRace, Candidate, SocialPost, and CollectionJob entities.", bold_prefix="3. Data Storage & Persistence Tier: ")
    add_bullet_p(doc, "The client-facing interface delivering real-time sentiment analytics to election observers and campaign analysts. Built using HTML5, modern Tailwind CSS, FontAwesome 6, Chart.js, and vanilla JavaScript AJAX. It renders interactive KPI metric cards, time-series area charts, candidate perception comparison bars, dynamic positive and negative word clouds, a live NLP testing sandbox, and CSV dataset export utilities.", bold_prefix="4. Presentation & Visual Analytics Tier: ")

    # 3.4 Ingestion and NER
    add_heading_2(doc, "3.4 Multi-Source Data Ingestion and Entity-Matching Methodology")
    p5 = (
        "The automated post ingestion pipeline operates through both scheduled background cron jobs and on-demand live triggers from "
        "the web dashboard. When an ingestion job is initiated, the system retrieves raw textual content from the selected channels:"
    )
    add_body_p(doc, p5)

    add_bullet_p(doc, "Raw text is sanitized by stripping embedded HTML tags, XML character entities, web URLs, tracking parameters, and excessive whitespace using compiled regular expression filters.", bold_prefix="a. Text Cleaning and Sanitization: ")
    add_bullet_p(doc, "Social media emojis (e.g., thumbs up, clapping hands, anger faces) and colloquial symbols are normalized into recognized token strings, preserving crucial sentiment signals that standard alphanumeric parsers discard.", bold_prefix="b. Emoji and Punctuation Preservation: ")
    add_bullet_p(doc, "The cleaned text is evaluated against a pre-compiled, highly granular dictionary of candidate aliases, honorifics, nicknames, party acronyms, and geographical keywords stored in the database. For example, mentions of 'Hamzat', 'Femi Hamzat', or 'Obafemi Hamzat' are automatically mapped to Dr. Kadri Obafemi Hamzat (APC, Lagos State). Mentions of 'Jandor' or 'Adediran' are mapped to Abdul-Azeez Adediran (PDP, Lagos State). Mentions of 'Abba Gida Gida' are mapped to Abba Kabir Yusuf (NNPP, Kano State).", bold_prefix="c. Intelligent Named Entity Recognition (NER): ")
    add_bullet_p(doc, "If direct candidate keywords are not detected, the algorithm scans for state mentions (e.g., 'Rivers', 'Kano', 'Oyo', 'Nasarawa') to associate the post with the corresponding StateRace entity, ensuring no relevant electoral discourse is omitted.", bold_prefix="d. State Electoral Race Association: ")

    # 3.5 Dual-Engine NLP
    add_heading_2(doc, "3.5 Dual-Engine NLP Classification Architecture (VADER & DistilBERT)")
    p6 = (
        "The mathematical foundation of the sentiment classification system is engineered around a dual-engine architecture, combining "
        "the deterministic efficiency of rule-based lexicons with the deep semantic comprehension of self-attention transformers."
    )
    add_body_p(doc, p6)

    # VADER Subheading
    add_heading_3(doc, "3.5.1 NLTK VADER Mathematical Formulation")
    p7 = (
        "The VADER engine computes valence scores by matching words in the input text against its human-validated sentiment lexicon. "
        "Individual token valence scores are adjusted based on heuristic rules (capitalization boost: +0.733, exclamation amplification: +0.292, "
        "degree modifier scaling: +/-0.293 to +/-0.360, contrastive 'but' re-weighting, and tri-gram negation flipping). The overall "
        "normalized compound polarity score (C) is computed as follows:"
    )
    add_body_p(doc, p7)

    p_eq1 = doc.add_paragraph()
    p_eq1.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    r_eq1 = p_eq1.add_run("Compound Score (C) = x / sqrt( x² + α )")
    r_eq1.font.name = 'Times New Roman'
    r_eq1.font.size = Pt(12)
    r_eq1.font.bold = True

    p8 = (
        "Where x represents the sum of the valence scores of each word in the text, and α represents a normalization parameter "
        "(empirically set to 15 in standard VADER implementations). The compound score C is continuous and bounded between -1.0 "
        "(extreme negative valence) and +1.0 (extreme positive valence). Based on standard academic thresholds, the sentiment label is assigned as:"
    )
    add_body_p(doc, p8)

    add_bullet_p(doc, "Assigned when the compound score C >= +0.05.", bold_prefix="• Positive: ")
    add_bullet_p(doc, "Assigned when the compound score C <= -0.05.", bold_prefix="• Negative: ")
    add_bullet_p(doc, "Assigned when -0.05 < C < +0.05.", bold_prefix="• Neutral: ")

    # DistilBERT Subheading
    add_heading_3(doc, "3.5.2 Hugging Face DistilBERT Contextual Transformer")
    p9 = (
        "For complex textual sequences where syntactic ambiguity or subtle political sentiment requires deep context, the system "
        "deploys a fine-tuned DistilBERT model (distilbert-base-uncased-finetuned-sst-2-english). Input text is tokenized into subword "
        "WordPieces, padded or truncated to a fixed sequence length, and injected with positional embeddings. The multi-head self-attention "
        "mechanism computes scaled dot-product attention across all input tokens simultaneously:"
    )
    add_body_p(doc, p9)

    p_eq2 = doc.add_paragraph()
    p_eq2.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    r_eq2 = p_eq2.add_run("Attention(Q, K, V) = softmax( (Q * K^T) / sqrt(d_k) ) * V")
    r_eq2.font.name = 'Times New Roman'
    r_eq2.font.size = Pt(12)
    r_eq2.font.bold = True

    p10 = (
        "Where Q, K, and V represent the Query, Key, and Value projection matrices respectively, and d_k is the dimensionality of the key vectors. "
        "The output [CLS] token representation is routed through a linear classification head and normalized via the Softmax activation "
        "function to produce class posterior probabilities for Positive, Neutral, and Negative sentiments. In the event of system memory "
        "pressure, PyTorch CUDA unavailability, or external model loading failure, an automated exception handler intercepts the request "
        "and seamlessly routes processing to the deterministic VADER engine, guaranteeing 100% operational uptime."
    )
    add_body_p(doc, p10)

    # 3.6 System Design Modeling
    add_heading_2(doc, "3.6 System Design Modeling")
    p11 = (
        "System modeling establishes the formal structural and behavioral blueprints of the software before and during implementation. "
        "Standard Unified Modeling Language (UML) notation was utilized to formalize system behavior across multiple perspectives:"
    )
    add_body_p(doc, p11)

    add_bullet_p(doc, "Identifies four primary user personas—System Administrator, Automated Collector Daemon, Election Analyst/Campaign Strategist, and Academic Researcher/Public Citizen—capturing interactions with core system use cases (post ingestion, dual classification, filtering, word clouds, sandbox evaluation, CSV export).", bold_prefix="1. Use Case Diagram: ")
    add_bullet_p(doc, "Models sequential control flow, decision branches, candidate identification loops, and database transaction commits during automated multi-source post harvesting.", bold_prefix="2. Data Ingestion Activity Workflow: ")
    add_bullet_p(doc, "Formalizes the operational pipeline from raw text input through emoji/slang preprocessing, engine router evaluation, parallel VADER/BERT execution, to final confidence score persistence.", bold_prefix="3. Dual-Engine Classification Activity Diagram: ")
    add_bullet_p(doc, "Defines relational entities, cardinalities (1:N between StateRace and Candidate; 1:N between Candidate and SocialPost), primary keys, foreign keys, and indexes ensuring relational integrity.", bold_prefix="4. Entity-Relationship Diagram (ERD): ")

    # 3.7 Technology Stack
    add_heading_2(doc, "3.7 Implementation Technology Stack and Toolchain Justification")
    p12 = (
        "The selection of implementation languages, frameworks, libraries, and database management systems was guided by principles "
        "of computational efficiency, maintainability, community support, and deployment flexibility. Table 3.2 details the technology "
        "stack and provides rigorous technical justification for each selected component."
    )
    add_body_p(doc, p12)

    headers_3_2 = ["Layer / Domain", "Technology Selected", "Version", "Technical Engineering Justification"]
    rows_3_2 = [
        ["Programming Language", "Python", "3.11+", "High-level expressive syntax, premier scientific computing ecosystem, native asynchronous I/O support, and industry-standard machine learning libraries."],
        ["Web Framework", "Django", "4.2 LTS", "Mature Model-View-Template (MVT) architecture, robust Object-Relational Mapper (ORM), built-in security protections against CSRF/SQLi, and rapid administration interface."],
        ["Relational Database", "SQLite & PostgreSQL", "3.39 / 15.0", "Zero-configuration file-based SQLite for rapid local testing and development; enterprise-grade PostgreSQL with ACID compliance for scalable production deployments."],
        ["NLP Lexicon Engine", "NLTK VADER", "3.9+", "Optimized for social media informal slang, punctuation emphasis, and emojis; ultra-low execution latency (<25ms); deterministic rule-based output."],
        ["Deep Learning NLP", "Hugging Face Transformers / PyTorch", "4.47 / 2.2+", "State-of-the-art self-attention transformer pipeline utilizing DistilBERT for deep contextual understanding with automated fallback."],
        ["Data Science & ML", "Scikit-Learn, Pandas, NumPy", "1.4 / 2.2 / 1.26", "High-performance vectorized array calculations, classification metric computations (confusion matrices, F1-scores), and dataset filtering."],
        ["Data Visualization", "Chart.js, WordCloud, Matplotlib", "4.4 / 1.9 / 3.10", "Client-side interactive animated HTML5 canvas charts; high-resolution server-side dynamic WordCloud generation categorized by sentiment polarity."],
        ["Front-End Styling", "Tailwind CSS & FontAwesome", "3.4 / 6.5", "Utility-first CSS framework enabling modern, responsive, dark-mode glassmorphism aesthetics without cumbersome heavyweight CSS bloat."],
        ["Networking & Feeds", "Requests, BeautifulSoup4, Urllib", "2.31 / 4.12", "Robust HTTP client libraries, resilient XML RSS parsing for Nigerian news feeds, and SSL fallback adapters for uninterrupted ingestion."]
    ]
    col_w_3_2 = [1.2, 1.3, 0.8, 3.4]
    add_styled_table(doc, "Table 3.2: Implementation Technology Stack and Toolchain Justification", headers_3_2, rows_3_2, col_w_3_2)

    # 3.8 Summary
    add_heading_2(doc, "3.8 Summary of Chapter Three")
    p13 = (
        "In summary, this chapter has systematically detailed the research methodology and technical frameworks underpinning the "
        "Social Media Sentiment Analysis System. The adoption of the Agile Scrum lifecycle facilitated six focused development sprints "
        "yielding a modular four-tier architecture. The automated multi-source ingestion pipeline, intelligent candidate NER matching algorithm, "
        "and dual-engine NLP classification architecture (uniting VADER with DistilBERT and automated fallback) establish a mathematically "
        "sound and operationally resilient foundation. In Chapter Four, the concrete implementation details, architectural diagrams, user "
        "interface designs, algorithmic listings, and empirical test results are thoroughly examined."
    )
    add_body_p(doc, p13)

    doc.add_page_break()
