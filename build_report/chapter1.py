import docx
from docx.shared import Pt
from .helpers import add_heading_1, add_heading_2, add_heading_3, add_body_p, add_bullet_p

def add_chapter_one(doc):
    add_heading_1(doc, "CHAPTER ONE", align_center=True, space_before=18, space_after=4)
    add_heading_1(doc, "INTRODUCTION", align_center=True, space_before=0, space_after=18)

    # 1.1 Background of the Study
    add_heading_2(doc, "1.1 Background of the Study")

    p1 = (
        "The twenty-first century has witnessed an extraordinary paradigm shift in the architecture of human communication, "
        "driven by the exponential proliferation of digital information communication technologies, high-speed mobile broadband, "
        "and interactive social web platforms. In contemporary democratic societies, political communication has decisively "
        "transcended traditional one-directional dissemination mechanisms—such as terrestrial television broadcasts, printed newspapers, "
        "and radio jingles—evolving into a hyper-connected, decentralized, and interactive public sphere. Platforms such as X (formerly Twitter), "
        "YouTube video comment threads, Facebook political groups, and digital news portals have emerged as primary virtual arenas "
        "where citizens freely express opinions, critique government policies, scrutinize political party manifestos, and construct "
        "collective perceptions of electoral candidates."
    )
    add_body_p(doc, p1)

    p2 = (
        "In the context of the Federal Republic of Nigeria, Africa's largest democracy with a population exceeding 220 million citizens, "
        "the influence of social media on electoral trajectories has reached unprecedented heights. Ahead of the anticipated 2027 "
        "General and Gubernatorial Elections, digital civic participation represents a pivotal barometer of the electorate's mood. "
        "Gubernatorial elections across key commercial, industrial, and demographic epicenters—including Lagos, Kano, Rivers, Oyo, "
        "Nasarawa, Kaduna, and Edo states—generate enormous volumes of user-generated digital discourse. Voters continuously share "
        "grievances regarding infrastructure deficits, economic hardships, inflation, and security concerns, while concurrently praising "
        "transformative policy blueprints, integrity, and visionary leadership exhibited by frontline gubernatorial candidates."
    )
    add_body_p(doc, p2)

    p3 = (
        "However, the sheer volume, velocity, and linguistic complexity of social media data present formidable computational hurdles. "
        "Every single day, tens of thousands of microblogs, comments, and debate rejoinders are generated across diverse social media "
        "ecosystems. Within these unstructured text streams lie subtle voter perceptions, emerging campaign crises, and shifts in "
        "electorate allegiance. Manually monitoring, categorizing, and quantifying this vast ocean of digital commentary is humanly "
        "impossible and logistically unsustainable. Consequently, organizations require automated computational methodologies capable "
        "of mining, normalizing, and classifying public sentiment at scale."
    )
    add_body_p(doc, p3)

    p4 = (
        "Natural Language Processing (NLP) and Sentiment Analysis—subfields of Artificial Intelligence and Computational Linguistics—provide "
        "the empirical mathematical framework necessary to resolve this challenge. By employing computational text classification algorithms, "
        "sentiment analysis extracts subjective valence from unstructured textual corpora, categorizing expressions into Positive, "
        "Negative, or Neutral sentiments. Historically, sentiment analysis relied predominantly on static sentiment lexicons. While "
        "lexicon approaches such as VADER (Valence Aware Dictionary and sEntiment Reasoner) excel at parsing informal microblog conventions, "
        "emojis, punctuation emphasis, and capitalizations, they frequently fail to capture deep contextual nuances, complex syntactical "
        "dependencies, and political sarcasm. Conversely, state-of-the-art Deep Contextual Transformers, such as BERT (Bidirectional "
        "Encoder Representations from Transformers) and its lightweight distilled variant DistilBERT, utilize multi-head self-attention "
        "mechanisms to understand bidirectional sentence semantics with remarkable accuracy, albeit at higher computational costs."
    )
    add_body_p(doc, p4)

    p5 = (
        "Recognizing the complementary strengths of these paradigms, this project designs and implements an integrated, multi-tier "
        "Social Media Sentiment Analysis System tailored specifically for monitoring the 2027 Gubernatorial Elections in Nigeria. "
        "The system engineers an automated data collection pipeline across multiple social feeds, an intelligent Named Entity Recognition "
        "(NER) algorithm matching candidate aliases, a robust dual-engine sentiment classification framework uniting VADER and DistilBERT, "
        "and an interactive analytics dashboard equipped with time-series trajectory area charts, dynamic topic word clouds, a live NLP sandbox, "
        "and exportable research datasets."
    )
    add_body_p(doc, p5)

    # 1.2 Statement of the Problem
    add_heading_2(doc, "1.2 Statement of the Problem")

    p6 = (
        "Accurate assessment of public opinion in high-stakes electoral contests is vital for democratic governance, policy formation, "
        "and campaign strategy. Despite this critical importance, existing methodologies and conventional sentiment tracking practices "
        "suffer from severe institutional, methodological, and computational limitations, enumerated as follows:"
    )
    add_body_p(doc, p6)

    add_bullet_p(doc, "Conventional public opinion surveys—conducted through physical questionnaires, town-hall interviews, or telephone sampling—are excessively expensive, logistically cumbersome, and suffer from extensive time lags. Survey results often take weeks to tabulate, rendering them obsolete in rapidly shifting campaign environments.", bold_prefix="1. High Cost and Inherent Inefficiency of Traditional Polling: ")
    add_bullet_p(doc, "Field surveys frequently exhibit demographic, geographic, and socio-economic biases, failing to capture the voices of youth demographics who predominantly express their political convictions online. Furthermore, human respondents frequently succumb to social desirability bias, concealing their true partisan preferences from survey enumerators.", bold_prefix="2. Demographic Sampling Bias and Social Desirability Distortion: ")
    add_bullet_p(doc, "Existing election monitors and political analysts who attempt to monitor social media manually rely on sporadic visual scrolling and anecdotal impressions. This manual approach is incapable of processing thousands of daily posts, resulting in severe confirmation bias and blind spots regarding emerging public backlash.", bold_prefix="3. Infeasibility of Manual Social Media Surveillance: ")
    add_bullet_p(doc, "Social media commentary in Nigerian political discourse is characterized by colloquial jargon, partisan slang, acronyms, creative spelling, heavy capitalization, and ubiquitous emoji usage. Generic off-the-shelf sentiment models trained on formal news or movie reviews fail catastrophically when confronted with informal socio-political text.", bold_prefix="4. Linguistic Complexity, Slang, and Contextual Nuance: ")
    add_bullet_p(doc, "Commercial enterprise media monitoring suites (such as Brandwatch, Sprinklr, or Meltwater) require prohibitive subscription fees running into tens of thousands of dollars annually. Furthermore, they operate as closed-box proprietary silos that do not expose candidate-entity mapping, lack Nigerian localized political dictionaries, and provide no real-time NLP sandboxes for custom empirical validation.", bold_prefix="5. Prohibitive Commercial Costs and Proprietary Opacity: ")
    add_bullet_p(doc, "Existing academic prototypes typically rely exclusively on a single classification technique—either pure rule-based lexicons (which miss complex contextual sarcasm) or heavy transformer neural networks (which suffer from inference latency, memory exhaustion, and external dependency failures). There is an acute lack of resilient hybrid systems with automated fallback architectures.", bold_prefix="6. Lack of Dual-Engine Redundancy and Automated Fallback: ")

    p7 = (
        "In the absence of an open, cost-effective, multi-source, and dual-engine sentiment analysis platform, electoral stakeholders "
        "remain deprived of empirical, real-time insights into citizen perception. This research directly resolves these challenges "
        "by engineering a robust, end-to-end platform tailored for the Nigerian 2027 Gubernatorial Elections."
    )
    add_body_p(doc, p7)

    # 1.3 Aim and Objectives of the Study
    add_heading_2(doc, "1.3 Aim and Objectives of the Study")

    p8 = (
        "The primary aim of this project is to design and implement an end-to-end, web-based Social Media Sentiment Analysis and "
        "Monitoring Platform for the 2027 Gubernatorial Elections in Nigeria, utilizing dual-engine Natural Language Processing and "
        "automated candidate entity matching to quantify public perception dynamics in real time."
    )
    add_body_p(doc, p8)

    p9 = "To accomplish this overarching aim, the following specific technical and empirical objectives were formulated:"
    add_body_p(doc, p9)

    add_bullet_p(doc, "To design and implement an automated, multi-source data collection pipeline capable of harvesting election-related textual posts from X (Twitter), YouTube comments, Facebook, and major Nigerian political news RSS feeds (Vanguard, Daily Post, Punch, Google News Nigeria), complemented by an automated realistic post simulation engine.", bold_prefix="1. Multi-Source Ingestion Pipeline: ")
    add_bullet_p(doc, "To formulate an intelligent Named Entity Recognition (NER) and keyword matching algorithm that dynamically associates ingested unstructured social media posts with specific gubernatorial candidates, political parties, and state electoral races.", bold_prefix="2. Automated Candidate Entity Matching: ")
    add_bullet_p(doc, "To architect and implement a dual-engine NLP classification pipeline combining the rule-based NLTK VADER lexicon (specialized for social media slang, capitalization heuristics, and emojis) with a fine-tuned Hugging Face DistilBERT deep learning transformer model, featuring automated fallback redundancy.", bold_prefix="3. Dual-Engine Sentiment Classification: ")
    add_bullet_p(doc, "To develop interactive visualization components—including responsive time-series trajectory area charts, candidate Net Sentiment Index leaderboards, platform share comparisons, and dynamic AJAX-filtered Word Clouds (positive vs. negative topic clusters)—utilizing Tailwind CSS and Chart.js.", bold_prefix="4. Real-Time Interactive Visual Analytics: ")
    add_bullet_p(doc, "To engineer a real-time NLP testing sandbox enabling researchers and campaign analysts to input arbitrary political statements, speech transcripts, or citizen quotes and receive instantaneous polarity classification and confidence scores.", bold_prefix="5. Live NLP Sandbox & Dataset Export: ")
    add_bullet_p(doc, "To rigorously evaluate the system's functional reliability, classification accuracy, precision, recall, F1-scores, and response latency through 21 automated unit/integration test cases and empirical benchmarking against human-annotated validation datasets.", bold_prefix="6. Empirical System Evaluation: ")

    # 1.4 Significance of the Study
    add_heading_2(doc, "1.4 Significance of the Study")

    p10 = (
        "The development and deployment of this Social Media Sentiment Analysis System holds profound theoretical, technical, "
        "and practical significance across multiple dimensions of modern society:"
    )
    add_body_p(doc, p10)

    add_bullet_p(doc, "Election management bodies such as the Independent National Electoral Commission (INEC) and accredited non-governmental election observation missions (e.g., Yiaga Africa, CDD) gain a continuous, data-driven mechanism to detect voter discontent, identify areas experiencing campaign friction, and monitor early warning signs of electoral violence.", bold_prefix="a. Electoral Integrity and Election Observers: ")
    add_bullet_p(doc, "Political parties, candidate campaign secretariats, and strategists can objectively assess how specific policy manifestos, infrastructure announcements, or town-hall appearances resonate with the electorate across individual states, allowing for adaptive, responsive campaign messaging.", bold_prefix="b. Political Campaign Strategists and Candidates: ")
    add_bullet_p(doc, "Investigative journalists, broadcast networks, and digital news agencies can substantiate political reporting with empirical sentiment analytics rather than relying solely on subjective editorial speculation or unscientific social media vox pops.", bold_prefix="c. News Media and Political Journalists: ")
    add_bullet_p(doc, "Scholars in Computer Science, Data Science, and Political Science gain an extensible, reproducible, open-source architectural template for investigating election sentiment dynamics, code-switching in political communication, and the comparative efficacy of lexicon versus deep transformer models in low-resource African electoral contexts.", bold_prefix="d. Academic Community and Computational Social Scientists: ")
    add_bullet_p(doc, "By democratizing access to aggregated public perception analytics, the system provides voters with transparent visibility into broad societal trends, counteracting the echo-chamber effects and algorithmic radicalization common on commercial social media platforms.", bold_prefix="e. General Voting Public and Civic Organizations: ")

    # 1.5 Scope and Delimitation of the Study
    add_heading_2(doc, "1.5 Scope and Delimitation of the Study")

    p11 = (
        "The scope of this research is specifically defined and delimited as follows:"
    )
    add_body_p(doc, p11)

    add_bullet_p(doc, "The system is specifically contextualized for the upcoming 2027 Nigerian Gubernatorial Elections, encompassing monitored state races including Lagos, Kano, Rivers, Oyo, Nasarawa, Taraba, Kaduna, and Edo states, tracking key candidates from leading parties (APC, PDP, NNPP, LP, Accord).", bold_prefix="1. Electoral Domain Scope: ")
    add_bullet_p(doc, "Data ingestion is configured for public digital channels: X (formerly Twitter), YouTube video comments, Facebook public community commentary, and reputable Nigerian news media RSS feeds (Punch, Vanguard, Daily Post, Google News Nigeria). Private encrypted messaging platforms (e.g., WhatsApp, Telegram) are explicitly delimited from this study due to end-to-end encryption and legal privacy boundaries.", bold_prefix="2. Data Sources Monitored: ")
    add_bullet_p(doc, "Text analysis focuses on English language posts, Nigerian political colloquialisms, common socio-political slang (e.g., 'godfatherism', 'structures', 'mandate', 'deliver'), punctuation heuristics, and Unicode emojis. Monolingual indigenous languages (pure Hausa, Yoruba, or Igbo) are excluded from the current baseline classifier and identified as opportunities for future research.", bold_prefix="3. Linguistic and NLP Scope: ")
    add_bullet_p(doc, "The web application is developed using Python 3.11 and the Django 4.2 framework, integrating SQLite for rapid local testing and PostgreSQL for production deployments, styled with modern Tailwind CSS and rendered using Chart.js.", bold_prefix="4. Technical Implementation Toolchain: ")

    # 1.6 Operational Definition of Terms
    add_heading_2(doc, "1.6 Operational Definition of Terms")

    p12 = "For the purpose of clarity and consistency throughout this report, the following technical terms are operationally defined:"
    add_body_p(doc, p12)

    add_bullet_p(doc, "The automated computational process of identifying, categorizing, and quantifying opinions, attitudes, and emotional valences expressed in textual documents as Positive, Negative, or Neutral.", bold_prefix="• Sentiment Analysis (Opinion Mining): ")
    add_bullet_p(doc, "A subfield of Artificial Intelligence and Computer Science concerned with enabling computational systems to process, understand, interpret, and generate human natural languages.", bold_prefix="• Natural Language Processing (NLP): ")
    add_bullet_p(doc, "Valence Aware Dictionary and sEntiment Reasoner; a specialized rule-based sentiment analysis lexicon and tool specifically sensitive to nuances expressed in social media contexts, including slang, capitalization, and emojis.", bold_prefix="• NLTK VADER: ")
    add_bullet_p(doc, "A state-of-the-art deep learning model architecture introduced by Vaswani et al. (2017) relying on multi-head self-attention mechanisms to capture complex bidirectional contextual dependencies between tokens in a text sequence.", bold_prefix="• Transformer Architecture: ")
    add_bullet_p(doc, "A lighter, faster, and distilled variant of BERT developed by Sanh et al. (2019) that retains 97% of BERT's language comprehension capabilities while being 40% smaller and 60% faster, utilized in this project for deep contextual sentiment classification.", bold_prefix="• DistilBERT: ")
    add_bullet_p(doc, "An information extraction subtask that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories, utilized here to match candidate names, aliases, and electoral states.", bold_prefix="• Named Entity Recognition (NER): ")
    add_bullet_p(doc, "A standardized normalized continuous numerical value ranging from -1.0 (extremely negative) to +1.0 (extremely positive), reflecting the overall emotional direction and intensity of an analyzed text.", bold_prefix="• Sentiment Polarity Score: ")
    add_bullet_p(doc, "An aggregated metric computed as the percentage of positive posts minus the percentage of negative posts for a specific candidate or political party (% Positive - % Negative), serving as the primary benchmark of public perception.", bold_prefix="• Net Sentiment Index (NSI): ")
    add_bullet_p(doc, "An Object-Relational Mapping abstraction provided by the Django framework that enables developers to interact with relational databases using Python object-oriented classes and querysets rather than raw SQL statements.", bold_prefix="• Django ORM: ")
    add_bullet_p(doc, "A modern front-end user interface design trend characterized by translucent frosted-glass containers, subtle borders, high contrast typography, and vibrant background gradients, implemented via Tailwind CSS.", bold_prefix="• Glassmorphism: ")

    # 1.7 Organization of the Project Report
    add_heading_2(doc, "1.7 Organization of the Project Report")

    p13 = (
        "This project report is systematically organized into five distinct, logically cohesive chapters, structured in "
        "accordance with standard university academic regulations:"
    )
    add_body_p(doc, p13)

    add_bullet_p(doc, "Presents the background of the study, articulates the problem statement, establishes the project's aim and specific objectives, outlines the significance, delineates the scope, defines operational terms, and summarizes report organization.", bold_prefix="Chapter One (Introduction): ")
    add_bullet_p(doc, "Conducts a comprehensive review of existing academic and commercial literature, reviews theoretical foundations of NLP and sentiment analysis, explores social media dynamics in elections, evaluates existing commercial and academic platforms, and identifies research gaps.", bold_prefix="Chapter Two (Literature Review): ")
    add_bullet_p(doc, "Details the research methodology, justifies the Agile Scrum framework, delineates the four-tier system architecture, explains multi-source data ingestion and candidate NER matching, outlines the dual-engine VADER-DistilBERT classification pipeline, and presents system design models.", bold_prefix="Chapter Three (Research Methodology): ")
    add_bullet_p(doc, "Presents the complete system design models, database schema dictionaries, user interface implementation views, core algorithmic code listings, REST API catalogs, comprehensive test cases, confusion matrices, and empirical performance evaluations.", bold_prefix="Chapter Four (System Design, Implementation, and Evaluation): ")
    add_bullet_p(doc, "Provides a synthesis of research accomplishments, highlights technical challenges and solutions, outlines actionable recommendations for future research, and concludes the dissertation.", bold_prefix="Chapter Five (Summary, Recommendations, and Conclusion): ")

    doc.add_page_break()
