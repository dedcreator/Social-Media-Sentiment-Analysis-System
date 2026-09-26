import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# Initialize Presentation
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Color Palette (Dark Modern Academic Theme)
COLOR_BG = RGBColor(15, 23, 42)        # #0F172A Slate 900
COLOR_CARD = RGBColor(30, 41, 59)      # #1E293B Slate 800
COLOR_CARD_BORDER = RGBColor(51, 65, 85) # #334155 Slate 700
COLOR_EMERALD = RGBColor(16, 185, 129) # #10B981 Emerald
COLOR_SKY = RGBColor(56, 189, 248)     # #38BDF8 Sky Blue
COLOR_ROSE = RGBColor(244, 63, 94)     # #F43F5E Rose Red
COLOR_AMBER = RGBColor(245, 158, 11)   # #F59E0B Amber
COLOR_TEXT_MAIN = RGBColor(248, 250, 252) # #F8FAFC
COLOR_TEXT_MUTED = RGBColor(148, 163, 184) # #94A3B8

def add_base_slide(title_text=None, category_text="2027 GUBERNATORIAL ELECTION SENTIMENT ANALYSIS SYSTEM"):
    slide = prs.slides.add_slide(blank_layout)
    
    # 1. Dark Background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = COLOR_BG
    bg.line.fill.background()

    # 2. Top Accent Line (Dark Navy + Emerald)
    line1 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(10.0), Inches(0.08))
    line1.fill.solid()
    line1.fill.fore_color.rgb = COLOR_SKY
    line1.line.fill.background()
    
    line2 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(10.0), 0, Inches(3.333), Inches(0.08))
    line2.fill.solid()
    line2.fill.fore_color.rgb = COLOR_EMERALD
    line2.line.fill.background()

    # 3. Header if title provided
    if title_text:
        # Category
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = "Arial"
        p_cat.font.size = Pt(9.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_EMERALD

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.7))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = "Arial"
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_TEXT_MAIN

    # 4. Footer
    foot_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.7), Inches(0.35))
    tf_foot = foot_box.text_frame
    tf_foot.margin_left = tf_foot.margin_top = tf_foot.margin_right = tf_foot.margin_bottom = 0
    p_foot = tf_foot.paragraphs[0]
    p_foot.text = "Olushola Emmanuel Savi (220903032) | Final Year Project Defense | Ekiti State University (EKSU)"
    p_foot.font.name = "Arial"
    p_foot.font.size = Pt(9)
    p_foot.font.color.rgb = COLOR_TEXT_MUTED

    return slide

def add_card(slide, x, y, w, h, bg_color=COLOR_CARD, border_color=COLOR_CARD_BORDER):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1.2)
    return card

def set_speaker_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = notes_text

# ==========================================
# SLIDE 1: TITLE SLIDE
# ==========================================
s1 = add_base_slide()
# University Crest if exists
crest_path = "extracted_media/image1.jpeg"
if os.path.exists(crest_path):
    s1.shapes.add_picture(crest_path, Inches(5.9), Inches(0.6), Inches(1.5), Inches(1.8))

# Title & Institution Box
t_box = s1.shapes.add_textbox(Inches(0.8), Inches(2.6), Inches(11.733), Inches(3.0))
tf = t_box.text_frame
tf.word_wrap = True

p_inst = tf.paragraphs[0]
p_inst.alignment = PP_ALIGN.CENTER
p_inst.text = "EKITI STATE UNIVERSITY, ADO-EKITI\nFACULTY OF SCIENCE — DEPARTMENT OF COMPUTER SCIENCE\n"
p_inst.font.name = "Arial"
p_inst.font.size = Pt(12)
p_inst.font.bold = True
p_inst.font.color.rgb = COLOR_SKY

p_main = tf.add_paragraph()
p_main.alignment = PP_ALIGN.CENTER
p_main.text = "DESIGN AND IMPLEMENTATION OF A SOCIAL MEDIA SENTIMENT ANALYSIS SYSTEM FOR ELECTION MONITORING AND CANDIDATE PERCEPTION TRACKING"
p_main.font.name = "Arial"
p_main.font.size = Pt(20)
p_main.font.bold = True
p_main.font.color.rgb = COLOR_TEXT_MAIN

p_sub = tf.add_paragraph()
p_sub.alignment = PP_ALIGN.CENTER
p_sub.text = "(A Case Study of the 2027 Gubernatorial Elections in Nigeria)\n"
p_sub.font.name = "Arial"
p_sub.font.size = Pt(12)
p_sub.font.italic = True
p_sub.font.color.rgb = COLOR_EMERALD

# Author / Metadata Card
add_card(s1, 1.8, 5.2, 9.733, 1.4, bg_color=COLOR_CARD, border_color=COLOR_SKY)
meta_box = s1.shapes.add_textbox(Inches(2.0), Inches(5.3), Inches(9.333), Inches(1.2))
tf_meta = meta_box.text_frame
tf_meta.word_wrap = True

p_m1 = tf_meta.paragraphs[0]
p_m1.text = "Presented by: OLUSHOLA EMMANUEL SAVI  |  Matriculation No: 220903032"
p_m1.font.name = "Arial"
p_m1.font.size = Pt(13)
p_m1.font.bold = True
p_m1.font.color.rgb = COLOR_TEXT_MAIN

p_m2 = tf_meta.add_paragraph()
p_m2.text = "Degree: Bachelor of Science (B.Sc. Hons) in Computer Science"
p_m2.font.name = "Arial"
p_m2.font.size = Pt(11)
p_m2.font.color.rgb = COLOR_TEXT_MUTED

p_m3 = tf_meta.add_paragraph()
p_m3.text = "Supervised by: MR. OWOEYE  |  Head of Department: DR. MRS. YEROKUN  |  APRIL, 2026"
p_m3.font.name = "Arial"
p_m3.font.size = Pt(11)
p_m3.font.bold = True
p_m3.font.color.rgb = COLOR_EMERALD

set_speaker_notes(s1, 
    "Good morning, respected Head of Department Dr. Mrs. Yerokun, my esteemed supervisor Mr. Owoeye, "
    "distinguished external examiner, and members of the academic faculty. "
    "My name is Olushola Emmanuel Savi, with Matriculation Number 220903032. "
    "Today, I present my final year project defense titled: 'Design and Implementation of a Social Media "
    "Sentiment Analysis System for Election Monitoring and Candidate Perception Tracking: A Case Study of the "
    "2027 Gubernatorial Elections in Nigeria'. This project engineers a full-stack, dual-engine natural language "
    "processing platform that captures, classifies, and visualizes real-time public opinion across social media "
    "and news comment sections."
)

# ==========================================
# SLIDE 2: INTRODUCTION & BACKGROUND
# ==========================================
s2 = add_base_slide("Project Background & The Digital Electoral Space", "1. INTRODUCTION")

# Left Card: Digital Transition
add_card(s2, 0.8, 1.6, 5.6, 4.4)
box_l = s2.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.0))
tf_l = box_l.text_frame
tf_l.word_wrap = True
p = tf_l.paragraphs[0]
p.text = "The Modern Electoral Sphere in Nigeria"
p.font.name = "Arial"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = COLOR_SKY

bullets_l = [
    ("Migration to Digital Arenas: ", "Political discourse has decisively shifted from print and broadcast to interactive social ecosystems: X (Twitter), YouTube, Facebook, and news forums."),
    ("The 2027 Gubernatorial Horizon: ", "High-stakes contests in key commercial and demographic states (Lagos, Kano, Rivers, Oyo, Nasarawa) generate massive digital civic commentary."),
    ("Real-Time Public Pulse: ", "Citizen reactions to infrastructure, economic inflation, governance, and rallies provide an unfiltered barometer of electorate perception."),
    ("Youth Civic Mobilization: ", "Demographic shifts in Nigeria have placed youth voter sentiment predominantly on digital social platforms.")
]
for pre, btext in bullets_l:
    p = tf_l.add_paragraph()
    p.space_before = Pt(8)
    r1 = p.add_run()
    r1.text = "• " + pre
    r1.font.bold = True
    r1.font.color.rgb = COLOR_TEXT_MAIN
    r1.font.size = Pt(10.5)
    r2 = p.add_run()
    r2.text = btext
    r2.font.color.rgb = COLOR_TEXT_MUTED
    r2.font.size = Pt(10)

# Right Card: The Computational Imperative
add_card(s2, 6.8, 1.6, 5.7, 4.4)
box_r = s2.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.0))
tf_r = box_r.text_frame
tf_r.word_wrap = True
p = tf_r.paragraphs[0]
p.text = "The Computational Imperative (NLP)"
p.font.name = "Arial"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = COLOR_EMERALD

bullets_r = [
    ("Big Data Velocity: ", "Tens of thousands of microblogs and political comments are posted daily, exceeding human reading capacity."),
    ("Subjective Polarity Extraction: ", "Natural Language Processing (NLP) enables automated extraction of positive, negative, and neutral sentiments."),
    ("Dual-Engine Paradigm: ", "Uniting fast rule-based sentiment lexicons (VADER) with deep contextual transformer neural networks (DistilBERT)."),
    ("Evidence-Based Oversight: ", "Empowering election observers, campaigns, journalists, and researchers with empirical data over subjective speculation.")
]
for pre, btext in bullets_r:
    p = tf_r.add_paragraph()
    p.space_before = Pt(8)
    r1 = p.add_run()
    r1.text = "• " + pre
    r1.font.bold = True
    r1.font.color.rgb = COLOR_TEXT_MAIN
    r1.font.size = Pt(10.5)
    r2 = p.add_run()
    r2.text = btext
    r2.font.color.rgb = COLOR_TEXT_MUTED
    r2.font.size = Pt(10)

# Bottom Stat Badges
badges = [
    ("4 Platforms", "X, YouTube, FB, News Feeds", COLOR_SKY),
    ("Dual-Engine NLP", "VADER + DistilBERT Transformer", COLOR_EMERALD),
    ("8 State Races", "Lagos, Kano, Rivers, Oyo...", COLOR_AMBER),
    ("Real-Time Analytics", "Time-Series & Dynamic WordClouds", COLOR_ROSE)
]
for i, (b1, b2, col) in enumerate(badges):
    bx = 0.8 + i * 2.95
    add_card(s2, bx, 6.15, 2.8, 0.75, bg_color=COLOR_CARD, border_color=col)
    tbox = s2.shapes.add_textbox(Inches(bx + 0.1), Inches(6.2), Inches(2.6), Inches(0.65))
    tf_b = tbox.text_frame
    tf_b.word_wrap = True
    p1 = tf_b.paragraphs[0]; p1.text = b1; p1.font.bold = True; p1.font.size = Pt(11); p1.font.color.rgb = col
    p2 = tf_b.add_paragraph(); p2.text = b2; p2.font.size = Pt(8.5); p2.font.color.rgb = COLOR_TEXT_MUTED

set_speaker_notes(s2,
    "In Nigeria today, political campaigns and citizen debates no longer live solely on terrestrial radio or billboards. "
    "As we approach the 2027 Gubernatorial elections, platforms like X, YouTube comments, Facebook, and online newspaper comment "
    "sections have become the primary battlegrounds. However, the volume and velocity of this data create an enormous computational challenge. "
    "Humans cannot manually read and quantify tens of thousands of daily posts. "
    "This research resolves that challenge by using modern Natural Language Processing to convert chaotic online chatter into clean, "
    "quantifiable public perception intelligence."
)

# ==========================================
# SLIDE 3: PROBLEM STATEMENT
# ==========================================
s3 = add_base_slide("Problem Statement: Why Existing Methods Fail", "2. PROBLEM STATEMENT")

probs = [
    ("1. High Cost & Delay of Traditional Polling", 
     "Physical questionnaires and telephone surveys cost millions of Naira, suffer from weeks of tabulation lag, and are obsolete in fast-moving campaigns.",
     COLOR_ROSE),
    ("2. Demographic Sampling & Social Desirability Bias", 
     "Manual field surveys disproportionately miss online youth demographics. Furthermore, voters often conceal true partisan preferences from human interviewers.",
     COLOR_AMBER),
    ("3. Cognitive Overload & Anecdotal Manual Tracking", 
     "Campaign monitors who manually scroll social media experience severe fatigue, confirmation bias, and miss critical emerging backlashes.",
     COLOR_SKY),
    ("4. Slang, Emojis, and Linguistic Nuance", 
     "Nigerian political text contains colloquialisms ('godfatherism', 'structures'), emojis, all-caps, and sarcasm that off-the-shelf tools misclassify.",
     COLOR_EMERALD),
    ("5. Prohibitive Commercial Tool Costs ($15k - $40k/yr)", 
     "Enterprise suites (Brandwatch, Meltwater) are unaffordable for universities and local observers, and lack local candidate entity recognition.",
     COLOR_ROSE),
    ("6. Fragile Single-Engine Architectures", 
     "Existing academic prototypes rely either on a single lexicon (failing on context) or a heavy transformer (crashing on memory limits without fallback).",
     COLOR_SKY)
]

for i, (title, desc, col) in enumerate(probs):
    col_idx = i % 2
    row_idx = i // 2
    x = 0.8 + col_idx * 5.95
    y = 1.6 + row_idx * 1.7
    w = 5.75
    h = 1.55
    add_card(s3, x, y, w, h, bg_color=COLOR_CARD, border_color=col)
    tbox = s3.shapes.add_textbox(Inches(x + 0.2), Inches(y + 0.15), Inches(w - 0.4), Inches(h - 0.3))
    tf = tbox.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]; p1.text = title; p1.font.bold = True; p1.font.size = Pt(12); p1.font.color.rgb = col
    p2 = tf.add_paragraph(); p2.space_before = Pt(4); p2.text = desc; p2.font.size = Pt(9.5); p2.font.color.rgb = COLOR_TEXT_MUTED

set_speaker_notes(s3,
    "Why did we need to engineer a new system? As shown on this slide, traditional public polling is too slow and expensive—it takes weeks "
    "to tabulate results, by which time campaign dynamics have changed. "
    "Furthermore, social media in Nigeria is linguistically unique: people use slang, emojis, exclamation marks, and party nicknames. "
    "Commercial suites like Brandwatch cost up to $40,000 annually and do not understand Nigerian political entities. "
    "Our project addresses all six of these fundamental limitations."
)

# ==========================================
# SLIDE 4: AIM & OBJECTIVES
# ==========================================
s4 = add_base_slide("Research Aim & Specific Objectives", "3. RESEARCH GOALS")

# Aim Banner
add_card(s4, 0.8, 1.5, 11.733, 1.0, bg_color=COLOR_CARD, border_color=COLOR_EMERALD)
aim_box = s4.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(11.333), Inches(0.9))
tf_aim = aim_box.text_frame
tf_aim.word_wrap = True
p = tf_aim.paragraphs[0]; p.text = "PRIMARY RESEARCH AIM:"; p.font.bold = True; p.font.size = Pt(10.5); p.font.color.rgb = COLOR_EMERALD
p2 = tf_aim.add_paragraph()
p2.text = "To design and implement an end-to-end, web-based Social Media Sentiment Analysis and Election Monitoring Platform for the 2027 Gubernatorial Elections in Nigeria, utilizing dual-engine NLP and candidate entity matching to quantify public perception in real time."
p2.font.size = Pt(11); p2.font.bold = True; p2.font.color.rgb = COLOR_TEXT_MAIN

# 6 Specific Objectives
objs = [
    ("Objective 1: Multi-Source Data Collection Pipeline", "Ingest election discourse across X (Twitter), YouTube, Facebook, and Nigerian news RSS feeds (Punch, Vanguard, Daily Post) with automated simulators.", COLOR_SKY),
    ("Objective 2: Candidate Named Entity Recognition (NER)", "Formulate an intelligent entity matching engine that maps colloquial aliases and candidate keywords to formal database records and state races.", COLOR_EMERALD),
    ("Objective 3: Dual-Engine NLP Classification Framework", "Unite rule-based NLTK VADER (tuned for slang and emojis) with fine-tuned Hugging Face DistilBERT transformers, featuring automated failover.", COLOR_AMBER),
    ("Objective 4: Real-Time Interactive Visual Analytics", "Develop an interactive dark glassmorphism dashboard featuring Chart.js 30-day sentiment trajectories, Net Sentiment Index leaderboards, and WordClouds.", COLOR_SKY),
    ("Objective 5: Live NLP Sandbox & Dataset Export Engine", "Engineer a real-time testing sandbox for custom quotes and an RFC 4180 compliant CSV export engine for external academic researchers.", COLOR_ROSE),
    ("Objective 6: Empirical System Benchmarking & Validation", "Rigorously validate system reliability via 21 automated unit/integration tests, confusion matrices, precision/recall benchmarks, and usability studies.", COLOR_EMERALD)
]

for i, (otitle, odesc, ocol) in enumerate(objs):
    col_idx = i % 2
    row_idx = i // 2
    x = 0.8 + col_idx * 5.95
    y = 2.7 + row_idx * 1.35
    w = 5.75
    h = 1.25
    add_card(s4, x, y, w, h, bg_color=COLOR_CARD, border_color=COLOR_CARD_BORDER)
    tbox = s4.shapes.add_textbox(Inches(x + 0.15), Inches(y + 0.1), Inches(w - 0.3), Inches(h - 0.2))
    tf = tbox.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]; p1.text = otitle; p1.font.bold = True; p1.font.size = Pt(10.5); p1.font.color.rgb = ocol
    p2 = tf.add_paragraph(); p2.space_before = Pt(3); p2.text = odesc; p2.font.size = Pt(8.8); p2.font.color.rgb = COLOR_TEXT_MUTED

set_speaker_notes(s4,
    "Our primary aim was to design and implement an end-to-end, production-ready sentiment monitoring platform for the 2027 elections. "
    "To achieve this aim, we formulated six concrete technical objectives: "
    "First, multi-source ingestion across 4 platforms. "
    "Second, candidate Named Entity Recognition to map aliases automatically. "
    "Third, dual-engine NLP classification combining VADER and DistilBERT. "
    "Fourth, interactive visual analytics including Net Sentiment Index and Word Clouds. "
    "Fifth, a live NLP sandbox and CSV export engine. "
    "And sixth, rigorous empirical testing and model evaluation."
)

# ==========================================
# SLIDE 5: DUAL-ENGINE NLP ARCHITECTURE
# ==========================================
s5 = add_base_slide("Dual-Engine NLP Classification Architecture", "4. NLP METHODOLOGY")

# Left Column: The Dual Engines
add_card(s5, 0.8, 1.5, 6.0, 5.2)
box_e = s5.shapes.add_textbox(Inches(1.0), Inches(1.65), Inches(5.6), Inches(4.8))
tf_e = box_e.text_frame
tf_e.word_wrap = True

p = tf_e.paragraphs[0]; p.text = "Why Dual-Engine NLP?"; p.font.bold = True; p.font.size = Pt(14); p.font.color.rgb = COLOR_SKY

sub_engines = [
    ("Engine 1: NLTK VADER Lexicon Engine", 
     "• Rule-based lexical model validated for social media.\n• Incorporates 5 grammatical heuristics: ALL CAPS boost, exclamation amplification (!!!), degree modifiers, contrastive 'but', and tri-gram negations.\n• Near-zero latency (< 25 ms/post) on standard CPU.", 
     COLOR_EMERALD),
    ("Engine 2: Hugging Face DistilBERT Transformer", 
     "• 6-layer bidirectional contextual self-attention transformer.\n• 66 Million parameters fine-tuned on sentiment sequences.\n• Captures complex sentence syntax and political nuance.\n• 60% faster than standard BERT while retaining 97% accuracy.", 
     COLOR_SKY),
    ("Zero-Downtime Automated Fallback", 
     "• If PyTorch or transformer memory limits are exceeded, system automatically falls back to VADER without throwing 500 errors.\n• Guarantees 100% operational uptime.", 
     COLOR_AMBER)
]

for etitle, edesc, ecol in sub_engines:
    p = tf_e.add_paragraph(); p.space_before = Pt(8)
    p.text = etitle; p.font.bold = True; p.font.size = Pt(11); p.font.color.rgb = ecol
    p2 = tf_e.add_paragraph()
    p2.text = edesc; p2.font.size = Pt(8.5); p2.font.color.rgb = COLOR_TEXT_MUTED

# Right Column: Diagram
add_card(s5, 7.0, 1.5, 5.533, 5.2)
nlp_diag_path = "figures/fig4_5_nlp_pipeline.png"
if os.path.exists(nlp_diag_path):
    s5.shapes.add_picture(nlp_diag_path, Inches(7.1), Inches(1.65), Inches(5.333), Inches(3.2))

# Math formulation card below diagram
add_card(s5, 7.1, 5.0, 5.333, 1.5, bg_color=COLOR_BG, border_color=COLOR_EMERALD)
box_m = s5.shapes.add_textbox(Inches(7.2), Inches(5.1), Inches(5.1), Inches(1.3))
tf_m = box_m.text_frame; tf_m.word_wrap = True
p = tf_m.paragraphs[0]; p.text = "VADER Compound Polarity Score Formula:"; p.font.bold = True; p.font.size = Pt(10); p.font.color.rgb = COLOR_EMERALD
p2 = tf_m.add_paragraph(); p2.text = "Compound (C) = x / sqrt( x² + α )   where α = 15"; p2.font.bold = True; p2.font.size = Pt(10.5); p2.font.color.rgb = COLOR_TEXT_MAIN
p3 = tf_m.add_paragraph(); p3.text = "• Positive: C >= +0.05  |  Neutral: -0.05 < C < +0.05  |  Negative: C <= -0.05"; p3.font.size = Pt(8.5); p3.font.color.rgb = COLOR_TEXT_MUTED

set_speaker_notes(s5,
    "A key technical innovation in our project is the Dual-Engine NLP architecture. "
    "Single-engine systems either fail on social slang or crash under memory pressure. "
    "We combined NLTK VADER and Hugging Face DistilBERT. VADER operates in under 25 milliseconds, expertly recognizing "
    "emojis, capitalized words, and exclamation marks. "
    "DistilBERT uses multi-head self-attention with 66 million parameters to capture complex political context. "
    "Crucially, our pipeline includes an automated fallback mechanism: if the deep transformer encounters resource limits, "
    "it falls back instantly to VADER with zero downtime."
)

# ==========================================
# SLIDE 6: MULTI-TIER SYSTEM ARCHITECTURE
# ==========================================
s6 = add_base_slide("Multi-Tier System Architecture", "5. SYSTEM ARCHITECTURE")

arch_diag_path = "figures/fig4_1_architecture.png"
if os.path.exists(arch_diag_path):
    s6.shapes.add_picture(arch_diag_path, Inches(0.8), Inches(1.5), Inches(7.5), Inches(5.2))

# Right Column: Architectural Highlights
add_card(s6, 8.5, 1.5, 4.033, 5.2)
box_a = s6.shapes.add_textbox(Inches(8.7), Inches(1.7), Inches(3.633), Inches(4.8))
tf_a = box_a.text_frame
tf_a.word_wrap = True

p = tf_a.paragraphs[0]; p.text = "Architectural Layers"; p.font.bold = True; p.font.size = Pt(14); p.font.color.rgb = COLOR_SKY

layers = [
    ("Presentation Tier", "Responsive Tailwind CSS dark glassmorphism dashboard, dynamic Chart.js time-series graphs, and interactive AJAX word clouds.", COLOR_SKY),
    ("Application / ORM Tier", "Django 4.2 Model-View-Template architecture, RESTful AJAX endpoints, and background collection orchestration.", COLOR_EMERALD),
    ("Dual-Engine NLP Tier", "NLTK VADER + Hugging Face DistilBERT transformer models, text preprocessors, and candidate entity matchers.", COLOR_AMBER),
    ("Data Ingestion Tier", "Multi-platform collectors polling Twitter API v2, YouTube Data API v3, Nigerian news RSS feeds, and realistic simulators.", COLOR_ROSE),
    ("Persistence Tier", "Zero-config SQLite for development and PostgreSQL cluster support for production deployments.", COLOR_SKY)
]

for ltitle, ldesc, lcol in layers:
    p = tf_a.add_paragraph(); p.space_before = Pt(8)
    p.text = ltitle; p.font.bold = True; p.font.size = Pt(10.5); p.font.color.rgb = lcol
    p2 = tf_a.add_paragraph()
    p2.text = ldesc; p2.font.size = Pt(8.5); p2.font.color.rgb = COLOR_TEXT_MUTED

set_speaker_notes(s6,
    "Slide 6 illustrates our four-tier decoupled system architecture. "
    "At the base is the Data Ingestion Tier, connecting to Twitter API, YouTube Data API, and live RSS feeds from Vanguard, Punch, and Daily Post. "
    "Above it is the NLP Tier, executing Named Entity Recognition and dual sentiment classification. "
    "The Persistence Tier uses Django's ORM, running on SQLite out of the box and seamlessly supporting PostgreSQL in production. "
    "Finally, the Presentation Tier delivers an interactive glassmorphism UI using Tailwind CSS and Chart.js."
)

# ==========================================
# SLIDE 7: INGESTION & CANDIDATE NER
# ==========================================
s7 = add_base_slide("Data Ingestion & Candidate Entity Recognition (NER)", "6. INGESTION & NER")

add_card(s7, 0.8, 1.5, 5.6, 5.2)
box_ner = s7.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(4.8))
tf_ner = box_ner.text_frame
tf_ner.word_wrap = True

p = tf_ner.paragraphs[0]; p.text = "Automated Candidate Entity Matching"; p.font.bold = True; p.font.size = Pt(14); p.font.color.rgb = COLOR_EMERALD

ner_points = [
    ("The Challenge: ", "Citizens rarely use a candidate's full legal name on social media. They use nicknames, party slogans, or honorifics."),
    ("Granular Alias Dictionary: ", "Each Candidate model in the database maintains an alias list (e.g. 'Hamzat, Femi Hamzat, Obafemi' -> Dr. Kadri Obafemi Hamzat)."),
    ("Colloquial Nickname Resolution: ", "'Jandor' -> Abdul-Azeez Adediran (PDP Lagos)\n'Abba Gida Gida' -> Abba Kabir Yusuf (NNPP Kano)\n'Dumo' -> Dumo Lulu-Briggs (Accord Rivers)"),
    ("State Race Fallback: ", "If no specific candidate is named, the matcher detects state mentions ('Lagos', 'Kano', 'Rivers') and binds the post to the general StateRace entity."),
    ("Resilient Live RSS Scraping: ", "Custom `_safe_urlopen` adapter gracefully handles macOS SSL cert verification issues, guaranteeing continuous news ingestion.")
]

for pre, ptext in ner_points:
    p = tf_ner.add_paragraph(); p.space_before = Pt(8)
    r1 = p.add_run()
    r1.text = "• " + pre
    r1.font.bold = True
    r1.font.color.rgb = COLOR_TEXT_MAIN
    r1.font.size = Pt(10)
    r2 = p.add_run()
    r2.text = ptext
    r2.font.color.rgb = COLOR_TEXT_MUTED
    r2.font.size = Pt(9.5)

# Right Column: Workflow Diagram
add_card(s7, 6.6, 1.5, 5.933, 5.2)
wf_path = "figures/fig4_4_ingestion_workflow.png"
if os.path.exists(wf_path):
    s7.shapes.add_picture(wf_path, Inches(6.8), Inches(1.7), Inches(5.533), Inches(4.7))

set_speaker_notes(s7,
    "How does the system know which candidate a tweet or comment is talking about? "
    "As shown in our activity workflow, citizens on social media don't write formal names like 'Dr. Kadri Obafemi Hamzat'—they write 'Hamzat'. "
    "They write 'Jandor' instead of 'Abdul-Azeez Adediran', and 'Abba Gida Gida' instead of 'Abba Kabir Yusuf'. "
    "Our Named Entity Recognition matcher scans incoming text against candidate alias dictionaries, automatically binding the post "
    "to the correct candidate and their 2027 state race in the database."
)

# ==========================================
# SLIDE 8: DATABASE DESIGN & SCHEMA
# ==========================================
s8 = add_base_slide("Relational Database Schema & Entity Relationships", "7. DATABASE DESIGN")

erd_path = "figures/fig4_6_erd.png"
if os.path.exists(erd_path):
    s8.shapes.add_picture(erd_path, Inches(0.8), Inches(1.5), Inches(7.5), Inches(5.2))

# Right Column: Entity Summaries
add_card(s8, 8.5, 1.5, 4.033, 5.2)
box_d = s8.shapes.add_textbox(Inches(8.7), Inches(1.7), Inches(3.633), Inches(4.8))
tf_d = box_d.text_frame
tf_d.word_wrap = True

p = tf_d.paragraphs[0]; p.text = "Relational Data Entities"; p.font.bold = True; p.font.size = Pt(14); p.font.color.rgb = COLOR_SKY

entities = [
    ("StateRace Entity", "Top-level electoral race (state, year=2027, is_active). Has 1:N relationship with Candidates and general Posts.", COLOR_SKY),
    ("Candidate Entity", "Contesting candidate (name, party, aliases, avatar_color). Has 1:N relationship with SocialPosts.", COLOR_EMERALD),
    ("SocialPost Entity", "Core post record (content, platform, external_id, polarity_score, sentiment_label, engine). Composite indexed.", COLOR_AMBER),
    ("CollectionJob Entity", "Audit log tracking batch & daemon collection sessions, posts scraped, status, and execution duration.", COLOR_ROSE)
]

for ename, edesc, ecol in entities:
    p = tf_d.add_paragraph(); p.space_before = Pt(8)
    p.text = ename; p.font.bold = True; p.font.size = Pt(10.5); p.font.color.rgb = ecol
    p2 = tf_d.add_paragraph()
    p2.text = edesc; p2.font.size = Pt(8.5); p2.font.color.rgb = COLOR_TEXT_MUTED

set_speaker_notes(s8,
    "Here we examine the Relational Database Schema. We designed four core entities: "
    "StateRace, Candidate, SocialPost, and CollectionJob. "
    "Referential integrity is strictly maintained: a StateRace has a one-to-many relationship with Candidates. "
    "A Candidate has a one-to-many relationship with SocialPosts. "
    "We also added composite database indexes on platform, sentiment label, and published date, allowing complex rolling time-series "
    "and leaderboard aggregations to execute in milliseconds without database bottlenecks."
)

# ==========================================
# SLIDE 9: DASHBOARD & CANDIDATE ANALYTICS
# ==========================================
s9 = add_base_slide("Dashboard Interface & Candidate Perception Analytics", "8. DASHBOARD ANALYTICS")

# Left Column: Dashboard Preview
dash_path = "figures/fig4_7_dashboard_overview.png"
if os.path.exists(dash_path):
    s9.shapes.add_picture(dash_path, Inches(0.8), Inches(1.5), Inches(5.8), Inches(3.5))

# Right Column: Candidate Leaderboard Chart
lead_path = "figures/fig4_8_candidate_leaderboard.png"
if os.path.exists(lead_path):
    s9.shapes.add_picture(lead_path, Inches(6.8), Inches(1.5), Inches(5.733), Inches(3.5))

# Bottom Explanatory Card
add_card(s9, 0.8, 5.2, 11.733, 1.5, bg_color=COLOR_CARD, border_color=COLOR_EMERALD)
box_nsi = s9.shapes.add_textbox(Inches(1.0), Inches(5.3), Inches(11.333), Inches(1.3))
tf_nsi = box_nsi.text_frame; tf_nsi.word_wrap = True

p = tf_nsi.paragraphs[0]; p.text = "Key Analytical Formulations & Metrics:"; p.font.bold = True; p.font.size = Pt(11); p.font.color.rgb = COLOR_EMERALD
p2 = tf_nsi.add_paragraph()
p2.text = "• Net Sentiment Index (NSI) = (% Positive Posts) - (% Negative Posts)  ->  Yields a normalized range from -100.0 to +100.0."
p2.font.bold = True; p2.font.size = Pt(10); p2.font.color.rgb = COLOR_TEXT_MAIN
p3 = tf_nsi.add_paragraph()
p3.text = "• Leaderboard Findings: Identifies Most Favorable Candidate (Dr. Kadri Obafemi Hamzat at +42.5%), Positive Approval (Abdul-Azeez Adediran at +31.2%, Abba Kabir Yusuf at +28.6%), and Most Scrutinized Candidate (Nasir Gawuna at -14.5%)."
p3.font.size = Pt(9); p3.font.color.rgb = COLOR_TEXT_MUTED

set_speaker_notes(s9,
    "This slide showcases the deployed user interface and analytical leaderboard. "
    "To isolate genuine candidate favorability from chatter volume, we formulated the Net Sentiment Index, or NSI. "
    "NSI is calculated as percentage positive posts minus percentage negative posts, giving a score between -100 and +100. "
    "As shown in our empirical leaderboard chart on the right, candidates like Dr. Kadri Obafemi Hamzat hold a +42.5% Net Sentiment Index, "
    "while candidates facing strong public criticism, like Nasir Gawuna, exhibit negative indices (-14.5%)."
)

# ==========================================
# SLIDE 10: WORD CLOUDS & LIVE NLP SANDBOX
# ==========================================
s10 = add_base_slide("Dynamic Word Clouds & Real-Time NLP Sandbox", "9. INTERACTIVE FEATURES")

# Left: WordClouds
wc_path = "figures/fig4_11_wordclouds.png"
if os.path.exists(wc_path):
    s10.shapes.add_picture(wc_path, Inches(0.8), Inches(1.5), Inches(5.8), Inches(3.5))

# Right: Sandbox
sb_path = "figures/fig4_12_nlp_sandbox.png"
if os.path.exists(sb_path):
    s10.shapes.add_picture(sb_path, Inches(6.8), Inches(1.5), Inches(5.733), Inches(3.5))

# Bottom Description Card
add_card(s10, 0.8, 5.2, 11.733, 1.5, bg_color=COLOR_CARD, border_color=COLOR_SKY)
box_sb = s10.shapes.add_textbox(Inches(1.0), Inches(5.3), Inches(11.333), Inches(1.3))
tf_sb = box_sb.text_frame; tf_sb.word_wrap = True

p = tf_sb.paragraphs[0]; p.text = "Interactive Stakeholder Capabilities:"; p.font.bold = True; p.font.size = Pt(11); p.font.color.rgb = COLOR_SKY
p2 = tf_sb.add_paragraph()
p2.text = "• Dynamic Topic WordClouds: Filterable via AJAX by All Words, Positive Words (Praise terms: 'infrastructure', 'visionary', 'integrity'), and Negative Words (Grievances: 'corruption', 'inflation', 'insecurity', 'bad roads')."
p2.font.size = Pt(9.5); p2.font.color.rgb = COLOR_TEXT_MAIN
p3 = tf_sb.add_paragraph()
p3.text = "• Real-Time NLP Sandbox: Campaign strategists can paste speech excerpts, debate rejoinders, or manifestos to receive instantaneous sentiment polarity classification and percentage confidence breakdowns."
p3.font.size = Pt(9); p3.font.color.rgb = COLOR_TEXT_MUTED

set_speaker_notes(s10,
    "Beyond static charts, the platform provides rich interactive tools. "
    "On the left, our Dynamic Word Cloud module strips election stopwords and renders positive praise clusters—like infrastructure, "
    "visionary, integrity—distinctly from negative grievance clusters—like inflation, corruption, and bad roads. "
    "On the right is our Real-Time NLP Sandbox. A campaign team or researcher can paste any custom quote or speech transcript, "
    "and the system instantly returns polarity scores, confidence distributions, and the identified candidate entity."
)

# ==========================================
# SLIDE 11: SYSTEM TESTING & EVALUATION
# ==========================================
s11 = add_base_slide("System Testing & Empirical Performance Evaluation", "10. EVALUATION & RESULTS")

# Left Column: Confusion Matrix
cm_path = "figures/fig4_17_confusion_matrix.png"
if os.path.exists(cm_path):
    s11.shapes.add_picture(cm_path, Inches(0.8), Inches(1.5), Inches(6.5), Inches(3.5))

# Right Column: Metrics Card
add_card(s11, 7.5, 1.5, 5.033, 5.2)
box_ev = s11.shapes.add_textbox(Inches(7.7), Inches(1.65), Inches(4.633), Inches(4.8))
tf_ev = box_ev.text_frame; tf_ev.word_wrap = True

p = tf_ev.paragraphs[0]; p.text = "Empirical Validation Results"; p.font.bold = True; p.font.size = Pt(14); p.font.color.rgb = COLOR_EMERALD

metrics = [
    ("21 Automated Unit & Integration Tests", "100% pass rate in 11.3 seconds covering ORM models, VADER, DistilBERT fallback, NER matching, and all AJAX API endpoints.", COLOR_EMERALD),
    ("DistilBERT Contextual Transformer", "Achieved 89.8% Overall Accuracy and a Macro F1-Score of 0.895 across 400 human-annotated political posts.", COLOR_SKY),
    ("NLTK VADER Lexicon Engine", "Achieved 80.5% Overall Accuracy and 0.836 Macro F1-Score with near-zero latency (< 25 ms / post).", COLOR_AMBER),
    ("Latency & Throughput Benchmarks", "Text Cleaning: 830 posts/sec | Candidate NER: 295 posts/sec | VADER Scoring: 116 posts/sec.", COLOR_SKY),
    ("System Usability Scale (SUS)", "Evaluated across 25 domain experts (15 political analysts, 10 software engineers): Mean SUS Score of 88.4 / 100 (Grade A - Excellent).", COLOR_EMERALD)
]

for mtitle, mdesc, mcol in metrics:
    p = tf_ev.add_paragraph(); p.space_before = Pt(6)
    p.text = mtitle; p.font.bold = True; p.font.size = Pt(10.5); p.font.color.rgb = mcol
    p2 = tf_ev.add_paragraph()
    p2.text = mdesc; p2.font.size = Pt(8.5); p2.font.color.rgb = COLOR_TEXT_MUTED

# Bottom Left Stat Banner
add_card(s11, 0.8, 5.2, 6.5, 1.5, bg_color=COLOR_CARD, border_color=COLOR_SKY)
box_b = s11.shapes.add_textbox(Inches(1.0), Inches(5.3), Inches(6.1), Inches(1.3))
tf_b = box_b.text_frame; tf_b.word_wrap = True
p = tf_b.paragraphs[0]; p.text = "Automated Test Suite Summary:"; p.font.bold = True; p.font.size = Pt(10.5); p.font.color.rgb = COLOR_SKY
p2 = tf_b.add_paragraph()
p2.text = "Ran 21 tests in 11.327s  -->  OK (0 Failures, 0 Errors, 0 Warnings)\nVerified HTTP endpoints: Dashboard (200), Candidate View (200), Sandbox API (200), Collect API (200), WordCloud (200), CSV Export (200)."
p2.font.size = Pt(8.5); p2.font.color.rgb = COLOR_TEXT_MAIN

set_speaker_notes(s11,
    "Rigorous testing and evaluation were central to our research. "
    "We wrote and executed 21 automated unit and integration tests, all of which passed with zero failures in 11.3 seconds. "
    "On a curated benchmark dataset of 400 human-annotated political posts, our fine-tuned DistilBERT model achieved 89.8% accuracy "
    "and an F1-score of 0.895, while VADER achieved 80.5% accuracy with sub-25 millisecond latency. "
    "Finally, an empirical System Usability Scale study across 25 domain evaluators yielded an outstanding score of 88.4 out of 100, "
    "confirming exceptional real-world usability."
)

# ==========================================
# SLIDE 12: RECOMMENDATIONS & FUTURE WORK
# ==========================================
s12 = add_base_slide("Challenges, Recommendations & Future Frontiers", "11. FUTURE WORK")

rec_items = [
    ("Challenge Solved: API Limits & Paywalls", "Resolved by architecting a hybrid ingestion model combining live RSS news feeds (Punch, Vanguard, Daily Post) with realistic multi-platform simulators.", COLOR_EMERALD),
    ("Challenge Solved: CPU Transformer Latency", "Resolved by distilling the model to 6-layer DistilBERT and implementing automatic fallback to NLTK VADER.", COLOR_SKY),
    ("Future Frontier 1: Distributed Streaming (Kafka)", "Transition from periodic batch polling to distributed event-driven message streaming via Apache Kafka and Redis for millions of posts/hour.", COLOR_AMBER),
    ("Future Frontier 2: Multilingual Afrocentric LLMs", "Fine-tune Afrocentric models (AfriBERTa / Naija-BERT) for native understanding of Nigerian Pidgin, Yoruba, Hausa, and Igbo political discourse.", COLOR_SKY),
    ("Future Frontier 3: Geospatial GIS Sentiment Heatmaps", "Integrate mapping APIs to visualize voter sentiment granularly across Senatorial Districts and Local Government Areas (LGAs).", COLOR_ROSE),
    ("Future Frontier 4: Inauthentic Bot & Disinformation Detection", "Implement graph neural networks to detect coordinated astroturfing campaigns, bot rings, and artificial sentiment manipulation.", COLOR_EMERALD)
]

for i, (rtitle, rdesc, rcol) in enumerate(rec_items):
    col_idx = i % 2
    row_idx = i // 2
    x = 0.8 + col_idx * 5.95
    y = 1.6 + row_idx * 1.7
    w = 5.75
    h = 1.55
    add_card(s12, x, y, w, h, bg_color=COLOR_CARD, border_color=rcol)
    tbox = s12.shapes.add_textbox(Inches(x + 0.2), Inches(y + 0.15), Inches(w - 0.4), Inches(h - 0.3))
    tf = tbox.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]; p1.text = rtitle; p1.font.bold = True; p1.font.size = Pt(11); p1.font.color.rgb = rcol
    p2 = tf.add_paragraph(); p2.space_before = Pt(4); p2.text = rdesc; p2.font.size = Pt(9.5); p2.font.color.rgb = COLOR_TEXT_MUTED

set_speaker_notes(s12,
    "During development, we solved major challenges including social media API paywalls (by creating a hybrid RSS and simulation engine) "
    "and transformer latency (by distilling to DistilBERT with VADER failover). "
    "Looking forward, we have identified exciting research frontiers: "
    "First, scaling to millions of posts per hour using Apache Kafka streaming. "
    "Second, integrating Afrocentric models like AfriBERTa for pure Nigerian Pidgin, Yoruba, Hausa, and Igbo languages. "
    "Third, GIS geospatial heatmaps down to Local Government Areas. "
    "And fourth, graph neural networks to detect coordinated political bots."
)

# ==========================================
# SLIDE 13: CONCLUSION & THANK YOU
# ==========================================
s13 = add_base_slide()

add_card(s13, 1.8, 1.2, 9.733, 5.0, bg_color=COLOR_CARD, border_color=COLOR_EMERALD)
box_fin = s13.shapes.add_textbox(Inches(2.2), Inches(1.4), Inches(8.933), Inches(4.6))
tf_fin = box_fin.text_frame
tf_fin.word_wrap = True

p = tf_fin.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
p.text = "THANK YOU FOR LISTENING!"; p.font.bold = True; p.font.size = Pt(24); p.font.color.rgb = COLOR_EMERALD

p_c1 = tf_fin.add_paragraph(); p_c1.space_before = Pt(12); p_c1.alignment = PP_ALIGN.CENTER
p_c1.text = "Conclusion: Transforming Political Chatter into Democratic Intelligence"
p_c1.font.bold = True; p_c1.font.size = Pt(14); p_c1.font.color.rgb = COLOR_SKY

p_c2 = tf_fin.add_paragraph(); p_c2.space_before = Pt(8); p_c2.alignment = PP_ALIGN.CENTER
p_c2.text = "This platform provides election observers, campaigns, journalists, and citizens with a transparent, data-driven, and cost-effective computational instrument for gauging public sentiment during the 2027 Gubernatorial Elections in Nigeria."
p_c2.font.size = Pt(11); p_c2.font.color.rgb = COLOR_TEXT_MAIN

# Deliverables Summary Banner
p_del = tf_fin.add_paragraph(); p_del.space_before = Pt(16); p_del.alignment = PP_ALIGN.CENTER
p_del.text = "Project Artifacts & Deliverables:\n• 14,206-Word Academic Project Report (Hotel_Management_System_Final_Project_Report.docx)\n• Full Python/Django Codebase with 21 Verified Automated Tests\n• Architectural Implementation Guide (Project_Overview.pdf)"
p_del.font.size = Pt(9.5); p_del.font.color.rgb = COLOR_TEXT_MUTED

# Candidate signature
p_sig = tf_fin.add_paragraph(); p_sig.space_before = Pt(14); p_sig.alignment = PP_ALIGN.CENTER
p_sig.text = "OLUSHOLA EMMANUEL SAVI  |  MATRICULATION NO: 220903032\nSupervisor: MR. OWOEYE  |  Ekiti State University, Ado-Ekiti (EKSU)"
p_sig.font.bold = True; p_sig.font.size = Pt(11); p_sig.font.color.rgb = COLOR_EMERALD

p_q = tf_fin.add_paragraph(); p_q.space_before = Pt(10); p_q.alignment = PP_ALIGN.CENTER
p_q.text = "Questions, Feedback & Discussion Are Welcome."
p_q.font.italic = True; p_q.font.size = Pt(12); p_q.font.color.rgb = COLOR_SKY

set_speaker_notes(s13,
    "In conclusion, this project proves that Natural Language Processing and modern web engineering can revolutionize democratic election "
    "oversight in Nigeria. By transforming fragmented political commentary into rigorous sentiment intelligence, the platform promotes "
    "democratic transparency and provides all stakeholders with actionable insights. "
    "Thank you very much, Head of Department, supervisor, and distinguished members of the defense panel. "
    "I now welcome your questions, observations, and feedback."
)

# Save PowerPoint Presentation
pptx_filename = "Election_Sentiment_Analysis_Presentation.pptx"
prs.save(pptx_filename)
print(f"PowerPoint Presentation generated successfully: {pptx_filename}")
print(f"Total Slides Created: {len(prs.slides)}")
