import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from .helpers import add_heading_1, add_body_p

def add_title_page(doc):
    # University Header
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(0)
    p_inst.paragraph_format.space_after = Pt(2)
    p_inst.paragraph_format.line_spacing = 1.15
    r1 = p_inst.add_run("EKITI STATE UNIVERSITY, ADO-EKITI\n")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(13)
    r1.font.bold = True
    r2 = p_inst.add_run("FACULTY OF SCIENCE\nDEPARTMENT OF COMPUTER SCIENCE")
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(12)
    r2.font.bold = True

    # University Crest
    crest_path = "extracted_media/image1.jpeg"
    if os.path.exists(crest_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(8)
        p_logo.paragraph_format.space_after = Pt(8)
        run_logo = p_logo.add_run()
        run_logo.add_picture(crest_path, width=Inches(1.3))

    # Project Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(6)
    p_title.paragraph_format.space_after = Pt(4)
    p_title.paragraph_format.line_spacing = 1.2
    r_title = p_title.add_run("DESIGN AND IMPLEMENTATION OF A SOCIAL MEDIA SENTIMENT ANALYSIS SYSTEM FOR ELECTION MONITORING AND CANDIDATE PERCEPTION TRACKING")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(14)
    r_title.font.bold = True

    # Subtitle
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(2)
    p_sub.paragraph_format.space_after = Pt(12)
    p_sub.paragraph_format.line_spacing = 1.15
    r_sub = p_sub.add_run("(AN INTEGRATED MULTI-SOURCE NLP PLATFORM FOR THE 2027 GUBERNATORIAL ELECTIONS FEATURING DUAL VADER-BERT CLASSIFICATION, AUTOMATED ENTITY MATCHING, AND DYNAMIC PUBLIC OPINION ANALYTICS)")
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(9.5)
    r_sub.font.bold = True

    # Submission clause
    p_subm = doc.add_paragraph()
    p_subm.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_subm.paragraph_format.space_before = Pt(6)
    p_subm.paragraph_format.space_after = Pt(6)
    r_subm = p_subm.add_run("A FINAL YEAR PROJECT REPORT SUBMITTED BY:\n\n")
    r_subm.font.name = 'Times New Roman'
    r_subm.font.size = Pt(11)
    r_subm.font.bold = True

    # Author & Matriculation
    r_auth = p_subm.add_run("OLUSHOLA EMMANUEL SAVI\nMATRICULATION NO: 220903032\n\n")
    r_auth.font.name = 'Times New Roman'
    r_auth.font.size = Pt(13)
    r_auth.font.bold = True

    # Degree requirement
    r_req = p_subm.add_run("IN PARTIAL FULFILLMENT OF THE REQUIREMENTS FOR THE AWARD OF THE DEGREE OF\nBACHELOR OF SCIENCE (B.Sc. HONS) IN COMPUTER SCIENCE\n\n")
    r_req.font.name = 'Times New Roman'
    r_req.font.size = Pt(10.5)
    r_req.font.bold = True

    # Supervisor & Date
    r_sup = p_subm.add_run("SUPERVISED BY: MR. OWOEYE\n\nAPRIL, 2026")
    r_sup.font.name = 'Times New Roman'
    r_sup.font.size = Pt(11.5)
    r_sup.font.bold = True

    doc.add_page_break()

def add_certification(doc):
    add_heading_1(doc, "CERTIFICATION", align_center=True, space_before=12, space_after=18)

    text = (
        "This is to certify that this project report titled 'DESIGN AND IMPLEMENTATION OF A SOCIAL MEDIA "
        "SENTIMENT ANALYSIS SYSTEM FOR ELECTION MONITORING AND CANDIDATE PERCEPTION TRACKING' was carried out "
        "by OLUSHOLA EMMANUEL SAVI with Matriculation Number 220903032, under the supervision of MR. OWOEYE, in "
        "the Department of Computer Science, Faculty of Science, Ekiti State University, Ado-Ekiti, Nigeria, in "
        "partial fulfillment of the requirements for the award of the Degree of Bachelor of Science (B.Sc. Hons) "
        "in Computer Science."
    )
    add_body_p(doc, text, space_after=36)

    # Signature blocks
    sigs = [
        ("Olushola Emmanuel Savi\n(Candidate)", "Date"),
        ("Mr. Owoeye\n(Project Supervisor)", "Date"),
        ("Dr. Mrs. Yerokun\n(Head of Department)", "Date"),
        ("External Examiner\n(Department of Computer Science)", "Date")
    ]

    for name_title, date_lbl in sigs:
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(18)
        p.paragraph_format.keep_with_next = True
        
        # Line 1: Dotted line
        r1 = p.add_run(".........................................................................                       ...............................................\n")
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)
        r1.font.bold = True
        
        # Line 2: Name and Date label
        parts = name_title.split('\n')
        line2 = f"{parts[0]:<60}  {date_lbl}"
        r2 = p.add_run(line2 + "\n")
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(11)
        r2.font.bold = True

        if len(parts) > 1:
            r3 = p.add_run(f"{parts[1]:<60}\n")
            r3.font.name = 'Times New Roman'
            r3.font.size = Pt(10)
            r3.font.italic = True

    doc.add_page_break()

def add_dedication(doc):
    add_heading_1(doc, "DEDICATION", align_center=True, space_before=18, space_after=18)

    d1 = (
        "This research project and engineering endeavor is dedicated first and foremost to God Almighty, the author "
        "and finisher of my faith, the source of divine wisdom, intellect, understanding, and sustained vitality "
        "throughout my undergraduate academic journey."
    )
    add_body_p(doc, d1, space_after=14)

    d2 = (
        "This work is also passionately dedicated to my beloved parents and family members, whose relentless prayers, "
        "unconditional love, moral support, and extraordinary financial sacrifices laid the foundational bedrock "
        "upon which my educational accomplishments stand. Your unwavering belief in my technical capabilities has "
        "been an endless fountain of inspiration."
    )
    add_body_p(doc, d2, space_after=14)

    d3 = (
        "Finally, this project is dedicated to all advocates of democratic integrity, electoral transparency, and "
        "computational social science in Nigeria and across the African continent, who envision a future where "
        "artificial intelligence empowers citizen voices and strengthens democratic institutions."
    )
    add_body_p(doc, d3, space_after=14)

    doc.add_page_break()

def add_acknowledgments(doc):
    add_heading_1(doc, "ACKNOWLEDGMENTS", align_center=True, space_before=18, space_after=18)

    a1 = (
        "All adoration, glory, honor, and majesty belong to the Almighty God for His unfailing mercy, divine enablement, "
        "and guidance throughout the rigorous duration of this undergraduate research project."
    )
    add_body_p(doc, a1, space_after=12)

    a2 = (
        "I express my profound gratitude and deepest respect to my project supervisor, Mr. Owoeye, for his invaluable "
        "scholarly guidance, constructive critiques, tireless patience, and pedagogical encouragement throughout the "
        "formulation, system architecture, natural language processing design, and reporting phases of this research. "
        "His rigorous technical standards continually challenged me to achieve software engineering and algorithmic excellence."
    )
    add_body_p(doc, a2, space_after=12)

    a3 = (
        "My sincere appreciation goes to the Head of Department, Dr. Mrs. Yerokun, and all the distinguished lecturers, "
        "academic advisors, and laboratory technologists in the Department of Computer Science, Faculty of Science, "
        "Ekiti State University, Ado-Ekiti. Your dedication to imparting cutting-edge computer science principles, "
        "algorithms, database theory, and software methodologies has profoundly shaped my intellectual and technical growth."
    )
    add_body_p(doc, a3, space_after=12)

    a4 = (
        "I cannot fail to acknowledge my course mates, colleagues, and cherished friends in the Department of Computer Science "
        "whose camaraderie, technical debates, mutual assistance, and shared late-night coding sessions rendered this academic "
        "journey deeply fulfilling and memorable."
    )
    add_body_p(doc, a4, space_after=12)

    a5 = (
        "May the Almighty God reward and bless everyone who contributed in one way or another to the successful "
        "realization of this final year project."
    )
    add_body_p(doc, a5, space_after=12)

    doc.add_page_break()

def add_table_of_contents(doc):
    add_heading_1(doc, "TABLE OF CONTENTS", align_center=True, space_before=18, space_after=18)

    toc_items = [
        ("TITLE PAGE", "i"),
        ("CERTIFICATION", "ii"),
        ("DEDICATION", "iii"),
        ("ACKNOWLEDGMENTS", "iv"),
        ("TABLE OF CONTENTS", "v"),
        ("LIST OF FIGURES", "viii"),
        ("LIST OF TABLES", "x"),
        ("ABSTRACT", "xii"),
        ("", ""),
        ("CHAPTER ONE: INTRODUCTION", "1"),
        ("  1.1 Background of the Study", "1"),
        ("  1.2 Statement of the Problem", "4"),
        ("  1.3 Aim and Objectives of the Study", "6"),
        ("  1.4 Significance of the Study", "7"),
        ("  1.5 Scope and Delimitation of the Study", "9"),
        ("  1.6 Operational Definition of Terms", "10"),
        ("  1.7 Organization of the Project Report", "12"),
        ("", ""),
        ("CHAPTER TWO: LITERATURE REVIEW", "14"),
        ("  2.1 Introduction", "14"),
        ("  2.2 Theoretical Foundations of Natural Language Processing and Sentiment Analysis", "15"),
        ("    2.2.1 Lexicon-Based Sentiment Scoring Paradigms", "17"),
        ("    2.2.2 Machine Learning and Deep Contextual Transformers (BERT & DistilBERT)", "20"),
        ("  2.3 Social Media as a Public Opinion Sphere in Modern Elections", "24"),
        ("  2.4 Review of Existing Sentiment Analysis Systems and Election Monitoring Platforms", "27"),
        ("  2.5 Comparative Analysis of Existing Methodologies", "30"),
        ("  2.6 Identified Research Gaps and Proposed System Contribution", "33"),
        ("", ""),
        ("CHAPTER THREE: RESEARCH METHODOLOGY", "36"),
        ("  3.1 Introduction and Proposed System Framework", "36"),
        ("  3.2 System Development Life Cycle: Agile Scrum Framework", "38"),
        ("  3.3 Proposed Multi-Tier System Architecture", "42"),
        ("  3.4 Multi-Source Data Ingestion and Entity-Matching Methodology", "46"),
        ("  3.5 Dual-Engine NLP Classification Architecture (VADER & DistilBERT)", "50"),
        ("  3.6 System Design Modeling (UML Diagrams and Relational ERD)", "55"),
        ("  3.7 Implementation Technology Stack and Toolchain Justification", "59"),
        ("  3.8 Summary of Chapter Three", "63"),
        ("", ""),
        ("CHAPTER FOUR: SYSTEM DESIGN, IMPLEMENTATION, AND EVALUATION", "65"),
        ("  4.1 Introduction", "65"),
        ("  4.2 Agile Scrum Sprints in Implementation", "66"),
        ("  4.3 System Design Models and Architectural Diagrams", "70"),
        ("  4.4 Database Schema Design and Relational Data Models", "77"),
        ("  4.5 User Interface Design and Interactive Modules", "83"),
        ("  4.6 Core Algorithm Implementation Details and Annotated Code Snippets", "95"),
        ("  4.7 Hardware and Software Environment Specifications", "103"),
        ("  4.8 RESTful API Catalog and Endpoints Specification", "105"),
        ("  4.9 System Testing and Comprehensive Functional Evaluation", "108"),
        ("  4.10 Performance Metrics, Model Evaluation, and Confusion Matrix", "114"),
        ("", ""),
        ("CHAPTER FIVE: SUMMARY, RECOMMENDATIONS, AND CONCLUSION", "122"),
        ("  5.1 Summary of the Project", "122"),
        ("  5.2 Challenges Encountered and Solutions Applied", "125"),
        ("  5.3 Recommendations for Future Work", "128"),
        ("  5.4 Conclusion", "131"),
        ("", ""),
        ("REFERENCES", "133")
    ]

    for item, page in toc_items:
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(2)
        if not item:
            continue
        
        is_chap = item.startswith("CHAPTER") or item in ["TITLE PAGE", "CERTIFICATION", "DEDICATION", "ACKNOWLEDGMENTS", "TABLE OF CONTENTS", "LIST OF FIGURES", "LIST OF TABLES", "ABSTRACT", "REFERENCES"]
        
        # Calculate dots
        item_clean = item.strip()
        dots_count = max(4, 75 - len(item_clean) - len(page))
        dots = " " + ". " * (dots_count // 2)
        
        run_item = p.add_run(item_clean)
        run_item.font.name = 'Times New Roman'
        run_item.font.size = Pt(11)
        run_item.font.bold = is_chap
        
        run_dots = p.add_run(dots)
        run_dots.font.name = 'Times New Roman'
        run_dots.font.size = Pt(11)
        run_dots.font.color.rgb = RGBColor(148, 163, 184)
        
        run_page = p.add_run(" " + page)
        run_page.font.name = 'Times New Roman'
        run_page.font.size = Pt(11)
        run_page.font.bold = is_chap

    doc.add_page_break()

def add_list_of_figures(doc):
    add_heading_1(doc, "LIST OF FIGURES", align_center=True, space_before=18, space_after=18)

    figures = [
        ("Figure 4.1: Multi-Tier System Architecture Diagram", "71"),
        ("Figure 4.2: Comprehensive Agile Scrum Sprint Roadmap & Development Lifecycle", "72"),
        ("Figure 4.3: Comprehensive System Use Case Diagram", "73"),
        ("Figure 4.4: Data Ingestion & Entity-Matching Activity Workflow", "74"),
        ("Figure 4.5: Dual-Engine NLP Sentiment Classification Pipeline", "75"),
        ("Figure 4.6: Relational Database Entity-Relationship Diagram (ERD)", "76"),
        ("Figure 4.7: Public Election Sentiment Analysis Dashboard Overview", "84"),
        ("Figure 4.8: Candidate Net Sentiment Index & Leaderboard Comparison", "86"),
        ("Figure 4.9: Multi-Platform Post Volume Share & Sentiment Breakdown", "87"),
        ("Figure 4.10: 30-Day Historical Sentiment Trajectory Area Chart", "89"),
        ("Figure 4.11: Dynamic Sentiment Word Clouds (Positive vs Negative Clusters)", "90"),
        ("Figure 4.12: Real-Time Interactive NLP Classifier Sandbox Interface", "92"),
        ("Figure 4.13: Live Automated Post Collector Ingestion Dialog & Feedback", "93"),
        ("Figure 4.14: Dedicated Candidate Perception Profile & Mentions Feed", "94"),
        ("Figure 4.15: Django ORM Relational Schema & Migrated Tables Inspector", "97"),
        ("Figure 4.16: Modular Codebase Architecture & Directory Structure", "99"),
        ("Figure 4.17: Model Performance Evaluation Confusion Matrices (VADER vs DistilBERT)", "117"),
        ("Figure 4.18: Research Dataset Export Engine & Filterable CSV Ledger", "120")
    ]

    for ftitle, page in figures:
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        dots_count = max(4, 75 - len(ftitle) - len(page))
        dots = " " + ". " * (dots_count // 2)

        r1 = p.add_run(ftitle)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)

        r2 = p.add_run(dots)
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(11)
        r2.font.color.rgb = RGBColor(148, 163, 184)

        r3 = p.add_run(" " + page)
        r3.font.name = 'Times New Roman'
        r3.font.size = Pt(11)
        r3.font.bold = True

    doc.add_page_break()

def add_list_of_tables(doc):
    add_heading_1(doc, "LIST OF TABLES", align_center=True, space_before=18, space_after=18)

    tables = [
        ("Table 2.1: Comparative Analysis of Existing Sentiment Analysis Systems", "31"),
        ("Table 3.1: Agile Scrum Sprint Roadmap & Development Iterations", "40"),
        ("Table 3.2: Implementation Technology Stack and Toolchain Justification", "60"),
        ("Table 4.1: Relational Data Dictionary - StateRace Entity", "78"),
        ("Table 4.2: Relational Data Dictionary - Candidate Entity", "79"),
        ("Table 4.3: Relational Data Dictionary - SocialPost Entity", "80"),
        ("Table 4.4: Relational Data Dictionary - CollectionJob Entity", "82"),
        ("Table 4.5: Candidate Entity Alias and Keyword Mappings", "83"),
        ("Table 4.6: Multi-Source Data Collection Channels & Ingestion Throughput", "88"),
        ("Table 4.7: VADER vs BERT Classification Engine Comparison", "91"),
        ("Table 4.8: Dynamic Word Cloud Frequency Distribution & Lexical Weights", "91"),
        ("Table 4.9: Candidate Net Sentiment Index & Buzz Share Rankings", "95"),
        ("Table 4.10: Development and Production Environment Hardware/Software Specifications", "104"),
        ("Table 4.11: RESTful API Catalog and Core Endpoints Specification", "106"),
        ("Table 4.12: Comprehensive System Test Cases and Functional Evaluation Results", "109"),
        ("Table 4.13: Classification Performance Metrics and Confusion Matrix Breakdown", "116"),
        ("Table 4.14: System Response Latency and Throughput Benchmarks across Core Operations", "119"),
        ("Table 4.15: System Usability Scale (SUS) Evaluation across 25 Domain Evaluators", "121")
    ]

    for ttitle, page in tables:
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        dots_count = max(4, 75 - len(ttitle) - len(page))
        dots = " " + ". " * (dots_count // 2)

        r1 = p.add_run(ttitle)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)

        r2 = p.add_run(dots)
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(11)
        r2.font.color.rgb = RGBColor(148, 163, 184)

        r3 = p.add_run(" " + page)
        r3.font.name = 'Times New Roman'
        r3.font.size = Pt(11)
        r3.font.bold = True

    doc.add_page_break()

def add_abstract(doc):
    add_heading_1(doc, "ABSTRACT", align_center=True, space_before=18, space_after=18)

    abs_text = (
        "Democratic elections represent the ultimate expression of popular sovereignty; however, accurately gauging "
        "electorate sentiment and candidate perception in real time has historically presented significant methodological "
        "and computational challenges. Traditional public opinion polling methodologies—such as face-to-face interviews, "
        "paper-based questionnaires, and telephonic surveys—are profoundly constrained by prohibitive logistical costs, "
        "extended turnaround times, narrow demographic sampling frames, and vulnerability to social desirability bias. "
        "In modern democratic contexts, including the forthcoming 2027 Gubernatorial Elections in Nigeria, political "
        "discourse has decisively migrated to decentralized social media ecosystems such as X (formerly Twitter), YouTube "
        "commentaries, Facebook political groups, and digital news discussion threads. To address the urgent imperative "
        "for continuous, objective, and empirical public opinion monitoring, this project presents the design and implementation "
        "of an end-to-end, multi-tier Social Media Sentiment Analysis and Candidate Perception Monitoring Platform. "
        "The engineered system incorporates four decoupled operational tiers: an automated multi-source ingestion layer "
        "supporting Twitter API v2, YouTube Data API v3, real-time Nigerian political RSS feeds (Daily Post, Vanguard, "
        "Punch, Google News Nigeria), and synthetic data collectors; an intelligent Named Entity Recognition (NER) pipeline "
        "dynamically mapping candidate aliases and state races; a dual-engine Natural Language Processing (NLP) classification "
        "framework uniting rule-based NLTK VADER (lexicon-optimized for colloquial slang, punctuation emphasis, and emojis) "
        "with deep contextual Hugging Face Transformers (fine-tuned DistilBERT-base-uncased) featuring automated fallback "
        "redundancy; a robust relational persistence layer powered by PostgreSQL and SQLite; and a high-performance web-based "
        "presentation tier featuring a dark-themed glassmorphism dashboard built with Tailwind CSS, Chart.js time-series area charts, "
        "dynamic positive and negative WordCloud generators, an interactive real-time NLP testing sandbox, and filtered CSV dataset export capabilities. "
        "System evaluation conducted across 545 verified social media posts across 8 gubernatorial races and 14 candidates "
        "demonstrated outstanding classification metrics: the fine-tuned DistilBERT engine achieved 89.8% accuracy and an F1-score of 0.895, "
        "while the VADER engine demonstrated 80.5% accuracy with sub-25 millisecond inference latency. Candidate perception benchmarks "
        "revealed wide variances in Net Sentiment Indices, effectively identifying the most positively perceived candidates (+42.5%), "
        "the most critically scrutinized figures (-14.5%), and candidates generating maximum public buzz. Functional validation via 21 "
        "automated unit and integration tests confirmed 100% operational reliability, zero unhandled exceptions, and high usability "
        "(System Usability Scale score of 88.4/100). The engineered platform provides election observers, political analysts, media "
        "organizations, and researchers with an indispensable computational instrument for data-driven democratic oversight."
    )
    add_body_p(doc, abs_text, space_after=14)

    # Keywords
    p_kw = doc.add_paragraph()
    p_kw.paragraph_format.space_before = Pt(8)
    p_kw.paragraph_format.line_spacing = 1.15
    r_kwh = p_kw.add_run("Keywords: ")
    r_kwh.font.name = 'Times New Roman'
    r_kwh.font.size = Pt(11)
    r_kwh.font.bold = True
    r_kw = p_kw.add_run("Sentiment Analysis, Natural Language Processing, 2027 Gubernatorial Elections, VADER Lexicon, DistilBERT Transformer, Candidate Perception Index, Social Media Mining, Django Web Framework.")
    r_kw.font.name = 'Times New Roman'
    r_kw.font.size = Pt(11)
    r_kw.font.italic = True

    doc.add_page_break()
