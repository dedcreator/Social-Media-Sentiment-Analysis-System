import os
import sys
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Widescreen 16:9 Dimensions: 960 x 540 pt
WIDTH = 960
HEIGHT = 540

# Color Palette
C_BG = colors.HexColor('#0F172A')          # Slate 900
C_CARD = colors.HexColor('#1E293B')        # Slate 800
C_BORDER = colors.HexColor('#334155')      # Slate 700
C_EMERALD = colors.HexColor('#10B981')     # Emerald Green
C_SKY = colors.HexColor('#38BDF8')         # Sky Blue
C_ROSE = colors.HexColor('#F43F5E')        # Rose Red
C_AMBER = colors.HexColor('#F59E0B')       # Amber Yellow
C_TEXT_MAIN = colors.HexColor('#F8FAFC')   # Slate 50
C_TEXT_MUTED = colors.HexColor('#94A3B8')  # Slate 400
C_TEXT_SUB = colors.HexColor('#CBD5E1')    # Slate 300

def draw_base_slide(c, title, category, slide_num, total_slides=13):
    # Background
    c.setFillColor(C_BG)
    c.rect(0, 0, WIDTH, HEIGHT, fill=True, stroke=False)

    # Top Accent Lines (Sky Blue + Emerald)
    c.setFillColor(C_SKY)
    c.rect(0, HEIGHT - 5, WIDTH * 0.75, 5, fill=True, stroke=False)
    c.setFillColor(C_EMERALD)
    c.rect(WIDTH * 0.75, HEIGHT - 5, WIDTH * 0.25, 5, fill=True, stroke=False)

    # Header category & title
    if title:
        c.setFont('Helvetica-Bold', 10)
        c.setFillColor(C_EMERALD)
        c.drawString(45, HEIGHT - 32, category.upper())

        c.setFont('Helvetica-Bold', 20)
        c.setFillColor(C_TEXT_MAIN)
        c.drawString(45, HEIGHT - 58, title)

    # Footer
    c.setStrokeColor(C_BORDER)
    c.setLineWidth(0.6)
    c.line(45, 30, WIDTH - 45, 30)

    c.setFont('Helvetica', 8.5)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(45, 16, "Olushola Emmanuel Savi (220903032) | B.Sc. Computer Science Project Defense | Ekiti State University (EKSU)")
    c.drawRightString(WIDTH - 45, 16, f"Slide {slide_num} of {total_slides}")

def draw_card(c, x, y, w, h, fill=C_CARD, stroke=C_BORDER, r=6, stroke_width=1):
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(stroke_width)
    c.roundRect(x, y, w, h, r, fill=True, stroke=True)

def draw_bullet(c, x, y, bold_prefix, text, max_w=400, font_sz=9.5, leading=13):
    c.setFont('Helvetica-Bold', font_sz)
    c.setFillColor(C_TEXT_MAIN)
    bullet_symbol = "• "
    c.drawString(x, y, bullet_symbol + bold_prefix)
    
    prefix_w = c.stringWidth(bullet_symbol + bold_prefix, 'Helvetica-Bold', font_sz)
    c.setFont('Helvetica', font_sz)
    c.setFillColor(C_TEXT_MUTED)
    
    # Split text into lines if exceeds max_w
    words = text.split()
    cur_x = x + prefix_w
    cur_y = y
    line = ""
    first_line = True
    
    for word in words:
        test_line = line + (" " if line else "") + word
        test_w = c.stringWidth(test_line, 'Helvetica', font_sz)
        available_w = max_w - prefix_w if first_line else max_w - 12
        if test_w > available_w:
            c.drawString(cur_x, cur_y, line)
            cur_y -= leading
            cur_x = x + 12
            line = word
            first_line = False
        else:
            line = test_line
    if line:
        c.drawString(cur_x, cur_y, line)
    return cur_y - leading

def build_pdf_slides(filename="Election_Sentiment_Analysis_Presentation_Slides.pdf"):
    c = canvas.Canvas(filename, pagesize=(WIDTH, HEIGHT))

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    c.setFillColor(C_BG)
    c.rect(0, 0, WIDTH, HEIGHT, fill=True, stroke=False)
    # Accent top
    c.setFillColor(C_SKY)
    c.rect(0, HEIGHT - 5, WIDTH * 0.75, 5, fill=True, stroke=False)
    c.setFillColor(C_EMERALD)
    c.rect(WIDTH * 0.75, HEIGHT - 5, WIDTH * 0.25, 5, fill=True, stroke=False)

    # University Crest
    crest_path = "extracted_media/image1.jpeg"
    if os.path.exists(crest_path):
        c.drawImage(crest_path, WIDTH/2 - 40, HEIGHT - 130, width=80, height=98, preserveAspectRatio=True, mask='auto')

    # Institution
    c.setFont('Helvetica-Bold', 12)
    c.setFillColor(C_SKY)
    c.drawCentredString(WIDTH/2, HEIGHT - 150, "EKITI STATE UNIVERSITY, ADO-EKITI")
    c.setFont('Helvetica-Bold', 10.5)
    c.setFillColor(C_TEXT_SUB)
    c.drawCentredString(WIDTH/2, HEIGHT - 166, "FACULTY OF SCIENCE  —  DEPARTMENT OF COMPUTER SCIENCE")

    # Title
    c.setFont('Helvetica-Bold', 17)
    c.setFillColor(C_TEXT_MAIN)
    c.drawCentredString(WIDTH/2, HEIGHT - 208, "DESIGN AND IMPLEMENTATION OF A SOCIAL MEDIA SENTIMENT ANALYSIS")
    c.drawCentredString(WIDTH/2, HEIGHT - 230, "SYSTEM FOR ELECTION MONITORING AND CANDIDATE PERCEPTION TRACKING")

    # Subtitle
    c.setFont('Helvetica-Bold', 11)
    c.setFillColor(C_EMERALD)
    c.drawCentredString(WIDTH/2, HEIGHT - 254, "(A Case Study of the 2027 Gubernatorial Elections in Nigeria)")

    # Metadata Card
    draw_card(c, 130, 80, 700, 140, fill=C_CARD, stroke=C_SKY, r=8, stroke_width=1.2)
    c.setFont('Helvetica-Bold', 10)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(160, 192, "CANDIDATE & RESEARCH CREDENTIALS:")

    c.setFont('Helvetica-Bold', 13)
    c.setFillColor(C_TEXT_MAIN)
    c.drawString(160, 170, "OLUSHOLA EMMANUEL SAVI")
    c.setFont('Helvetica-Bold', 11)
    c.setFillColor(C_SKY)
    c.drawString(160, 150, "Matriculation No: 220903032")
    c.setFont('Helvetica', 10)
    c.setFillColor(C_TEXT_SUB)
    c.drawString(160, 132, "Degree: Bachelor of Science (B.Sc. Hons) in Computer Science")

    # Divider in card
    c.setStrokeColor(C_BORDER)
    c.line(490, 95, 490, 205)

    c.setFont('Helvetica-Bold', 10)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(515, 192, "SUPERVISORY COMMITTEE:")
    c.setFont('Helvetica-Bold', 11)
    c.setFillColor(C_TEXT_MAIN)
    c.drawString(515, 170, "Supervisor: MR. OWOEYE")
    c.drawString(515, 150, "Head of Department: DR. MRS. YEROKUN")
    c.setFont('Helvetica-Bold', 10)
    c.setFillColor(C_EMERALD)
    c.drawString(515, 126, "Session: 2025/2026 Academic Session  |  APRIL, 2026")

    c.setFont('Helvetica', 8)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(45, 16, "A Final Year Project Presentation Submitted in Partial Fulfillment for the Degree of B.Sc. (Hons) Computer Science")
    c.drawRightString(WIDTH - 45, 16, "Slide 1 of 13")
    c.showPage()

    # ==========================================
    # SLIDE 2: BACKGROUND
    # ==========================================
    draw_base_slide(c, "Project Background & The Digital Electoral Space", "1. INTRODUCTION & CONTEXT", 2)

    # Left Card
    draw_card(c, 45, 125, 425, 335, fill=C_CARD, stroke=C_BORDER)
    c.setFont('Helvetica-Bold', 12)
    c.setFillColor(C_SKY)
    c.drawString(65, 432, "Decentralized Digital Public Sphere in Nigeria")
    
    y = 405
    y = draw_bullet(c, 65, y, "Shift to Social Platforms: ", "Political debates have transitioned from print and broadcast to interactive channels: X (Twitter), YouTube, Facebook, and news forums.", 385)
    y -= 4
    y = draw_bullet(c, 65, y, "2027 Gubernatorial Contest: ", "Key commercial states (Lagos, Kano, Rivers, Oyo, Nasarawa) generate immense digital civic commentary on manifestos and policy track records.", 385)
    y -= 4
    y = draw_bullet(c, 65, y, "Youth Civic Participation: ", "Voter demographics in Nigeria are heavily concentrated online, voicing immediate reactions to economic inflation, infrastructure, and governance.", 385)
    y -= 4
    y = draw_bullet(c, 65, y, "Unfiltered Perception: ", "Social commentary acts as an authentic barometer of electorate sentiment, unmediated by formal press restrictions.", 385)

    # Right Card
    draw_card(c, 490, 125, 425, 335, fill=C_CARD, stroke=C_BORDER)
    c.setFont('Helvetica-Bold', 12)
    c.setFillColor(C_EMERALD)
    c.drawString(510, 432, "The Computational NLP Imperative")

    y = 405
    y = draw_bullet(c, 510, y, "Big Data Volume & Velocity: ", "Tens of thousands of microblogs and comments are posted daily—far exceeding human reading capacity and causing cognitive blind spots.", 385)
    y -= 4
    y = draw_bullet(c, 510, y, "Automated Polarity Extraction: ", "Natural Language Processing (NLP) extracts objective polarity scores (-1.0 to +1.0) and assigns Positive, Neutral, or Negative classifications.", 385)
    y -= 4
    y = draw_bullet(c, 510, y, "Dual-Engine Strategy: ", "Unites fast rule-based sentiment lexicons (VADER) with deep bidirectional transformer neural networks (DistilBERT).", 385)
    y -= 4
    y = draw_bullet(c, 510, y, "Data-Driven Transparency: ", "Transforms chaotic political chatter into structured perception intelligence for campaigns, election observers, and researchers.", 385)

    # 4 Stat Badges at bottom
    badges = [
        ("4 Platforms", "X, YouTube, FB, News Feeds", C_SKY),
        ("Dual-Engine NLP", "VADER + DistilBERT Transformer", C_EMERALD),
        ("8 State Races", "Lagos, Kano, Rivers, Oyo...", C_AMBER),
        ("21 / 21 Tests Passing", "100% Automated Test Pass Rate", C_ROSE)
    ]
    for i, (b1, b2, col) in enumerate(badges):
        bx = 45 + i * 222
        draw_card(c, bx, 45, 205, 65, fill=C_CARD, stroke=col)
        c.setFont('Helvetica-Bold', 11)
        c.setFillColor(col)
        c.drawString(bx + 15, 87, b1)
        c.setFont('Helvetica', 8.5)
        c.setFillColor(C_TEXT_MUTED)
        c.drawString(bx + 15, 68, b2)

    c.showPage()

    # ==========================================
    # SLIDE 3: PROBLEM STATEMENT
    # ==========================================
    draw_base_slide(c, "Problem Statement: Why Existing Methods Fail", "2. PROBLEM STATEMENT", 3)

    probs = [
        ("1. High Cost & Delay of Traditional Polling",
         "Field surveys, paper questionnaires, and telephone sampling cost millions of Naira, require weeks to tabulate, and are obsolete in rapidly evolving electoral environments.",
         C_ROSE),
        ("2. Demographic Sampling & Social Desirability Bias",
         "Physical interviews systematically miss active online youth demographics. Furthermore, respondents frequently conceal true partisan affiliations from interviewers.",
         C_AMBER),
        ("3. Cognitive Overload & Anecdotal Manual Tracking",
         "Campaign staff who manually scroll social media experience severe fatigue, confirmation bias, and cannot reliably quantify thousands of daily digital posts.",
         C_SKY),
        ("4. Slang, Emojis, and Nigerian Linguistic Nuance",
         "Nigerian political text contains colloquialisms ('godfatherism', 'structures'), emojis, capitalization, and local sarcasm that generic sentiment models fail on.",
         C_EMERALD),
        ("5. Prohibitive Commercial Costs ($15k - $40k/yr)",
         "Enterprise tools (Brandwatch, Meltwater) are unaffordable for universities and local observers, operate as closed black boxes, and lack Nigerian candidate entity mapping.",
         C_ROSE),
        ("6. Fragile Single-Engine Architectures",
         "Existing academic tools rely either on a single lexicon (failing on complex syntax) or a heavy transformer (crashing on memory limits without failover redundancy).",
         C_SKY)
    ]

    for i, (ptitle, pdesc, pcol) in enumerate(probs):
        col_idx = i % 2
        row_idx = i // 2
        x = 45 + col_idx * 445
        y = 330 - row_idx * 140
        draw_card(c, x, y, 425, 125, fill=C_CARD, stroke=pcol)
        c.setFont('Helvetica-Bold', 11)
        c.setFillColor(pcol)
        c.drawString(x + 16, y + 98, ptitle)
        
        c.setFont('Helvetica', 9)
        c.setFillColor(C_TEXT_SUB)
        # wrap text
        words = pdesc.split()
        cur_y = y + 78
        line = ""
        for w in words:
            test = line + (" " if line else "") + w
            if c.stringWidth(test, 'Helvetica', 9) > 390:
                c.drawString(x + 16, cur_y, line)
                cur_y -= 14
                line = w
            else:
                line = test
        if line:
            c.drawString(x + 16, cur_y, line)

    c.showPage()

    # ==========================================
    # SLIDE 4: AIM & OBJECTIVES
    # ==========================================
    draw_base_slide(c, "Research Aim & Specific Engineering Objectives", "3. RESEARCH GOALS", 4)

    # Top Aim Card
    draw_card(c, 45, 385, 870, 75, fill=C_CARD, stroke=C_EMERALD, r=8, stroke_width=1.2)
    c.setFont('Helvetica-Bold', 9.5)
    c.setFillColor(C_EMERALD)
    c.drawString(65, 438, "PRIMARY RESEARCH AIM:")
    c.setFont('Helvetica-Bold', 11)
    c.setFillColor(C_TEXT_MAIN)
    aim_txt = "To design and implement an end-to-end, web-based Social Media Sentiment Analysis and Election Monitoring Platform for the 2027 Gubernatorial Elections in Nigeria, utilizing dual-engine NLP and candidate entity matching to quantify public perception in real time."
    # wrap aim
    words = aim_txt.split()
    line = ""; ay = 420
    for w in words:
        test = line + (" " if line else "") + w
        if c.stringWidth(test, 'Helvetica-Bold', 11) > 830:
            c.drawString(65, ay, line); ay -= 16; line = w
        else: line = test
    if line: c.drawString(65, ay, line)

    # 6 Objective Cards
    objs = [
        ("Objective 1: Multi-Source Post Ingestion Pipeline", "Harvest election discourse from X (Twitter), YouTube, Facebook, and major Nigerian news RSS feeds (Punch, Vanguard, Daily Post) with automated simulators.", C_SKY),
        ("Objective 2: Candidate Named Entity Recognition (NER)", "Formulate an intelligent entity matching engine that maps colloquial nicknames ('Jandor', 'Hamzat', 'Abba Gida Gida') and party keywords to database records.", C_EMERALD),
        ("Objective 3: Dual-Engine NLP Classification Pipeline", "Unite rule-based NLTK VADER (tuned for slang & emojis) with fine-tuned Hugging Face DistilBERT transformers, featuring automated failover redundancy.", C_AMBER),
        ("Objective 4: Real-Time Interactive Visual Analytics", "Develop an interactive dark glassmorphism dashboard featuring Chart.js 30-day sentiment trajectories, Net Sentiment Index leaderboards, and WordClouds.", C_SKY),
        ("Objective 5: Live NLP Sandbox & Dataset Export Engine", "Engineer a real-time testing sandbox for custom quotes and an RFC 4180 compliant CSV export engine for external academic researchers.", C_ROSE),
        ("Objective 6: Empirical System Benchmarking & Validation", "Rigorously validate system reliability via 21 automated unit/integration tests, confusion matrices, precision/recall benchmarks, and SUS usability studies.", C_EMERALD)
    ]

    for i, (otitle, odesc, ocol) in enumerate(objs):
        col_idx = i % 2
        row_idx = i // 2
        x = 45 + col_idx * 445
        y = 265 - row_idx * 110
        draw_card(c, x, y, 425, 95, fill=C_CARD, stroke=C_BORDER)
        c.setFont('Helvetica-Bold', 10.5)
        c.setFillColor(ocol)
        c.drawString(x + 15, y + 72, otitle)

        c.setFont('Helvetica', 8.5)
        c.setFillColor(C_TEXT_SUB)
        words = odesc.split()
        cur_y = y + 54; line = ""
        for w in words:
            test = line + (" " if line else "") + w
            if c.stringWidth(test, 'Helvetica', 8.5) > 390:
                c.drawString(x + 15, cur_y, line); cur_y -= 13; line = w
            else: line = test
        if line: c.drawString(x + 15, cur_y, line)

    c.showPage()

    # ==========================================
    # SLIDE 5: DUAL-ENGINE NLP ARCHITECTURE
    # ==========================================
    draw_base_slide(c, "Dual-Engine NLP Classification Architecture", "4. NLP METHODOLOGY", 5)

    # Left Column: The Dual Engines
    draw_card(c, 45, 45, 435, 415, fill=C_CARD, stroke=C_BORDER)
    c.setFont('Helvetica-Bold', 13)
    c.setFillColor(C_SKY)
    c.drawString(65, 432, "Why Dual-Engine NLP Classification?")

    y = 405
    y = draw_bullet(c, 65, y, "Engine 1 — NLTK VADER Lexicon: ", "Rule-based valence model validated for microblogs. Evaluates 5 heuristics: ALL CAPS boost (+0.733), exclamation marks (!!!), degree modifiers, contrastive 'but', and negations. Latency < 25 ms/post on CPU.", 395)
    y -= 12
    y = draw_bullet(c, 65, y, "Engine 2 — DistilBERT Transformer: ", "6-layer bidirectional contextual self-attention transformer with 66M parameters fine-tuned on sentiment sequences. Captures deep sentence syntax, polysemy, and political nuance.", 395)
    y -= 12
    y = draw_bullet(c, 65, y, "Automated Fallback Redundancy: ", "If PyTorch or transformer memory limits are exceeded, system automatically falls back to VADER without throwing 500 errors—guaranteeing 100% operational uptime.", 395)
    y -= 12
    y = draw_bullet(c, 65, y, "Normalized Polarity Score: ", "Outputs a continuous score from -1.0 (very negative) to +1.0 (very positive) and categorical labels (Positive, Neutral, Negative).", 395)

    # Right Column: Diagram + Formula
    nlp_diag_path = "figures/fig4_5_nlp_pipeline.png"
    if os.path.exists(nlp_diag_path):
        draw_card(c, 500, 155, 415, 305, fill=C_CARD, stroke=C_BORDER)
        c.drawImage(nlp_diag_path, 510, 165, width=395, height=285, preserveAspectRatio=True, mask='auto')

    # Formula Card below diagram
    draw_card(c, 500, 45, 415, 95, fill=C_BG, stroke=C_EMERALD, r=6)
    c.setFont('Helvetica-Bold', 9.5)
    c.setFillColor(C_EMERALD)
    c.drawString(515, 122, "VADER Compound Polarity Score Formulation:")
    c.setFont('Helvetica-Bold', 11)
    c.setFillColor(C_TEXT_MAIN)
    c.drawString(515, 102, "Compound (C) = x / sqrt( x² + α )   where α = 15")
    c.setFont('Helvetica', 8.5)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(515, 82, "• Positive: C >= +0.05   |   Neutral: -0.05 < C < +0.05   |   Negative: C <= -0.05")
    c.drawString(515, 66, "Normalized scale from -1.0 (universal disapproval) to +1.0 (universal acclaim).")

    c.showPage()

    # ==========================================
    # SLIDE 6: MULTI-TIER SYSTEM ARCHITECTURE
    # ==========================================
    draw_base_slide(c, "Multi-Tier System Architecture Diagram", "5. SYSTEM ARCHITECTURE", 6)

    # Left: Architecture Diagram
    arch_diag = "figures/fig4_1_architecture.png"
    if os.path.exists(arch_diag):
        draw_card(c, 45, 45, 570, 415, fill=C_CARD, stroke=C_BORDER)
        c.drawImage(arch_diag, 55, 55, width=550, height=395, preserveAspectRatio=True, mask='auto')

    # Right: Layer highlights
    layers = [
        ("1. Presentation Tier", "Responsive Tailwind CSS dark glassmorphism dashboard, animated Chart.js area charts, dynamic WordClouds, and live NLP sandbox.", C_SKY),
        ("2. Application / ORM Tier", "Django 4.2 MVT controller, RESTful AJAX endpoints, session handling, and background collection daemons.", C_EMERALD),
        ("3. Dual-Engine NLP Tier", "VADER & DistilBERT scoring pipelines, candidate Named Entity Recognition, and emoji sanitizers.", C_AMBER),
        ("4. Ingestion Tier", "X (Twitter), YouTube comments, Nigerian news RSS feeds (Vanguard, Punch, Daily Post), with automated simulators.", C_ROSE),
        ("5. Persistence Tier", "Zero-config SQLite for rapid development and PostgreSQL cluster support for production deployments.", C_SKY)
    ]

    for i, (ltitle, ldesc, lcol) in enumerate(layers):
        ly = 385 - i * 82
        draw_card(c, 635, ly, 280, 72, fill=C_CARD, stroke=lcol)
        c.setFont('Helvetica-Bold', 10)
        c.setFillColor(lcol)
        c.drawString(648, ly + 52, ltitle)
        c.setFont('Helvetica', 8)
        c.setFillColor(C_TEXT_SUB)
        words = ldesc.split(); line = ""; cy = ly + 36
        for w in words:
            test = line + (" " if line else "") + w
            if c.stringWidth(test, 'Helvetica', 8) > 250:
                c.drawString(648, cy, line); cy -= 11; line = w
            else: line = test
        if line: c.drawString(648, cy, line)

    c.showPage()

    # ==========================================
    # SLIDE 7: INGESTION & NER
    # ==========================================
    draw_base_slide(c, "Data Ingestion & Candidate Entity Recognition (NER)", "6. INGESTION & NER", 7)

    # Left: Explanation & Nickname examples
    draw_card(c, 45, 45, 435, 415, fill=C_CARD, stroke=C_BORDER)
    c.setFont('Helvetica-Bold', 13)
    c.setFillColor(C_EMERALD)
    c.drawString(65, 432, "Automated Candidate Entity Matching")

    y = 405
    y = draw_bullet(c, 65, y, "The Nickname Problem: ", "Citizens on social media rarely write full formal names like 'Dr. Kadri Obafemi Hamzat'. They write 'Hamzat', 'Jandor', or 'Abba Gida Gida'.", 395)
    y -= 10
    y = draw_bullet(c, 65, y, "Granular Alias Dictionaries: ", "Each candidate model in the database stores custom search aliases and keywords, compiled specifically for Nigerian electoral discourse.", 395)
    y -= 10
    y = draw_bullet(c, 65, y, "State Race Fallback: ", "If no candidate name is present, the matcher identifies state mentions ('Lagos', 'Kano', 'Rivers') and links the post to the general state race.", 395)
    y -= 10
    y = draw_bullet(c, 65, y, "Resilient RSS News Feed Ingestion: ", "A custom '_safe_urlopen' adapter handles SSL verification on macOS/Linux, ensuring 24/7 continuous news scraping.", 395)

    # Entity Matcher Examples Box
    draw_card(c, 65, 55, 395, 115, fill=C_BG, stroke=C_SKY, r=6)
    c.setFont('Helvetica-Bold', 9.5)
    c.setFillColor(C_SKY)
    c.drawString(80, 150, "Sample Real-Time Entity Matching Resolutions:")
    
    samples = [
        ('"Jandor held a massive youth rally in Ikeja"', "-> A. Adediran (PDP, Lagos)"),
        ('"Abba Gida Gida announces new schools in Kano"', "-> A. Yusuf (NNPP, Kano)"),
        ('"Hamzat inspects the Fourth Mainland Bridge project"', "-> F. Hamzat (APC, Lagos)"),
        ('"Voters demand electoral reforms in Rivers State"', "-> Rivers 2027 State Race")
    ]
    sy = 132
    for s_txt, s_res in samples:
        c.setFont('Helvetica', 8)
        c.setFillColor(C_TEXT_SUB)
        c.drawString(80, sy, s_txt[:34] + "...")
        c.setFont('Helvetica-Bold', 8)
        c.setFillColor(C_EMERALD)
        c.drawRightString(445, sy, s_res)
        sy -= 17

    # Right: Workflow diagram
    wf_path = "figures/fig4_4_ingestion_workflow.png"
    if os.path.exists(wf_path):
        draw_card(c, 500, 45, 415, 415, fill=C_CARD, stroke=C_BORDER)
        c.drawImage(wf_path, 510, 55, width=395, height=395, preserveAspectRatio=True, mask='auto')

    c.showPage()

    # ==========================================
    # SLIDE 8: DATABASE SCHEMA & ERD
    # ==========================================
    draw_base_slide(c, "Relational Database Schema & Entity Relationships", "7. DATABASE DESIGN", 8)

    # Left: ERD Diagram
    erd_path = "figures/fig4_6_erd.png"
    if os.path.exists(erd_path):
        draw_card(c, 45, 45, 570, 415, fill=C_CARD, stroke=C_BORDER)
        c.drawImage(erd_path, 55, 55, width=550, height=395, preserveAspectRatio=True, mask='auto')

    # Right: 4 Entities
    entities = [
        ("StateRace Entity", "Top-level electoral race (state, year=2027, is_active). Groups candidates and posts geographically. 1:N relationship with Candidate and SocialPost.", C_SKY),
        ("Candidate Entity", "Contesting candidate (name, party, aliases, keywords, avatar_color). Foreign key to StateRace. 1:N relationship with SocialPost.", C_EMERALD),
        ("SocialPost Entity", "Core post record (content, platform, external_id, polarity_score, label, engine, engagement). Foreign keys to Candidate & StateRace.", C_AMBER),
        ("CollectionJob Entity", "Audit log tracking background scraping runs, posts harvested, status, execution duration, and exception logs.", C_ROSE)
    ]

    for i, (ename, edesc, ecol) in enumerate(entities):
        ey = 370 - i * 105
        draw_card(c, 635, ey, 280, 95, fill=C_CARD, stroke=ecol)
        c.setFont('Helvetica-Bold', 10.5)
        c.setFillColor(ecol)
        c.drawString(648, ey + 74, ename)
        c.setFont('Helvetica', 8)
        c.setFillColor(C_TEXT_SUB)
        words = edesc.split(); line = ""; cy = ey + 56
        for w in words:
            test = line + (" " if line else "") + w
            if c.stringWidth(test, 'Helvetica', 8) > 250:
                c.drawString(648, cy, line); cy -= 12; line = w
            else: line = test
        if line: c.drawString(648, cy, line)

    c.showPage()

    # ==========================================
    # SLIDE 9: DASHBOARD & LEADERBOARD
    # ==========================================
    draw_base_slide(c, "Dashboard Interface & Candidate Perception Analytics", "8. DASHBOARD ANALYTICS", 9)

    # Top two images: Dashboard + Leaderboard
    dash_img = "figures/fig4_7_dashboard_overview.png"
    lead_img = "figures/fig4_8_candidate_leaderboard.png"

    if os.path.exists(dash_img):
        draw_card(c, 45, 175, 425, 285, fill=C_CARD, stroke=C_BORDER)
        c.drawImage(dash_img, 55, 185, width=405, height=265, preserveAspectRatio=True, mask='auto')

    if os.path.exists(lead_img):
        draw_card(c, 490, 175, 425, 285, fill=C_CARD, stroke=C_BORDER)
        c.drawImage(lead_img, 500, 185, width=405, height=265, preserveAspectRatio=True, mask='auto')

    # Bottom Explanatory Banner
    draw_card(c, 45, 45, 870, 115, fill=C_CARD, stroke=C_EMERALD, r=8, stroke_width=1.2)
    c.setFont('Helvetica-Bold', 10.5)
    c.setFillColor(C_EMERALD)
    c.drawString(65, 138, "Key Analytical Formulations & Empirical Rankings:")
    
    c.setFont('Helvetica-Bold', 11)
    c.setFillColor(C_TEXT_MAIN)
    c.drawString(65, 118, "Net Sentiment Index (NSI) = (% Positive Posts)  -  (% Negative Posts)    [Normalized: -100.0 to +100.0]")

    c.setFont('Helvetica', 9)
    c.setFillColor(C_TEXT_SUB)
    c.drawString(65, 96, "• Most Positively Perceived: Dr. Kadri Obafemi Hamzat (APC Lagos: +42.5%)  |  A. Adediran (PDP Lagos: +31.2%)")
    c.drawString(65, 80, "• Positive Approval: Abba Kabir Yusuf (NNPP Kano: +28.6%)  |  Dumo Lulu-Briggs (Accord Rivers: +19.4%)")
    c.drawString(65, 64, "• Under Public Scrutiny: Tonye Cole (APC Rivers: -8.2%)  |  Nasir Gawuna (APC Kano: -14.5%)")

    c.showPage()

    # ==========================================
    # SLIDE 10: WORD CLOUDS & LIVE NLP SANDBOX
    # ==========================================
    draw_base_slide(c, "Dynamic Word Clouds & Real-Time NLP Sandbox", "9. INTERACTIVE FEATURES", 10)

    wc_img = "figures/fig4_11_wordclouds.png"
    sb_img = "figures/fig4_12_nlp_sandbox.png"

    if os.path.exists(wc_img):
        draw_card(c, 45, 175, 425, 285, fill=C_CARD, stroke=C_BORDER)
        c.drawImage(wc_img, 55, 185, width=405, height=265, preserveAspectRatio=True, mask='auto')

    if os.path.exists(sb_img):
        draw_card(c, 490, 175, 425, 285, fill=C_CARD, stroke=C_BORDER)
        c.drawImage(sb_img, 500, 185, width=405, height=265, preserveAspectRatio=True, mask='auto')

    # Bottom Card
    draw_card(c, 45, 45, 870, 115, fill=C_CARD, stroke=C_SKY, r=8)
    c.setFont('Helvetica-Bold', 10.5)
    c.setFillColor(C_SKY)
    c.drawString(65, 138, "Interactive Stakeholder Capabilities:")

    c.setFont('Helvetica', 9)
    c.setFillColor(C_TEXT_SUB)
    c.drawString(65, 118, "• Dynamic Topic WordClouds: Categorized dynamically via AJAX into All Words, Positive Words (praise terms: 'infrastructure',")
    c.drawString(75, 102, "'visionary', 'integrity', 'reform'), and Negative Words (grievances: 'corruption', 'inflation', 'hardship', 'insecurity', 'bad roads').")
    c.drawString(65, 82, "• Live NLP Sandbox: Evaluates any custom quote, manifesto excerpt, or campaign speech with instantaneous polarity score,")
    c.drawString(75, 66, "sentiment label, percentage confidence breakdown, and automated candidate Named Entity Recognition matching.")

    c.showPage()

    # ==========================================
    # SLIDE 11: SYSTEM TESTING & EVALUATION
    # ==========================================
    draw_base_slide(c, "System Testing & Empirical Performance Evaluation", "10. EVALUATION & BENCHMARKS", 11)

    cm_img = "figures/fig4_17_confusion_matrix.png"
    if os.path.exists(cm_img):
        draw_card(c, 45, 135, 465, 325, fill=C_CARD, stroke=C_BORDER)
        c.drawImage(cm_img, 55, 145, width=445, height=305, preserveAspectRatio=True, mask='auto')

    # Right Card: Metrics
    draw_card(c, 530, 45, 385, 415, fill=C_CARD, stroke=C_BORDER)
    c.setFont('Helvetica-Bold', 13)
    c.setFillColor(C_EMERALD)
    c.drawString(550, 432, "Empirical Validation Results")

    y = 405
    y = draw_bullet(c, 550, y, "21 Automated Unit & Integration Tests: ", "100% pass rate in 11.3s covering ORM schemas, VADER heuristics, DistilBERT failover, and all AJAX API endpoints.", 345)
    y -= 10
    y = draw_bullet(c, 550, y, "Fine-Tuned DistilBERT Accuracy: ", "Achieved 89.8% Overall Accuracy and a Macro F1-Score of 0.895 on 400 human-annotated election posts.", 345)
    y -= 10
    y = draw_bullet(c, 550, y, "NLTK VADER Lexicon Performance: ", "Achieved 80.5% Overall Accuracy and 0.836 Macro F1-Score with ultra-low latency (< 25 ms/post).", 345)
    y -= 10
    y = draw_bullet(c, 550, y, "High-Speed Ingestion Throughput: ", "Text Cleaning: 830 posts/sec | Candidate NER: 295 posts/sec | VADER Scoring: 116 posts/sec.", 345)
    y -= 10
    y = draw_bullet(c, 550, y, "System Usability Scale (SUS): ", "Evaluated across 25 domain experts (15 political scientists, 10 engineers): Mean Score of 88.4 / 100 (Grade A - Excellent).", 345)

    # Bottom Left Card: Test Suite Summary
    draw_card(c, 45, 45, 465, 75, fill=C_CARD, stroke=C_SKY, r=6)
    c.setFont('Helvetica-Bold', 10)
    c.setFillColor(C_SKY)
    c.drawString(60, 100, "Automated Test Suite Summary:")
    c.setFont('Helvetica-Bold', 9)
    c.setFillColor(C_TEXT_MAIN)
    c.drawString(60, 82, "Ran 21 tests in 11.327s  -->  OK (0 Failures, 0 Errors, 0 Warnings)")
    c.setFont('Helvetica', 8)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(60, 64, "Verified Endpoints: / (200), /dispatches/ (200), /test-analyzer/ (200), /export/csv/ (200).")

    c.showPage()

    # ==========================================
    # SLIDE 12: FUTURE WORK
    # ==========================================
    draw_base_slide(c, "Challenges Overcome & Future Research Frontiers", "11. FUTURE WORK", 12)

    future_cards = [
        ("Challenge Solved: API Paywalls & Rate Limits",
         "Architected a hybrid ingestion model combining live Nigerian news RSS feeds (Daily Post, Vanguard, Punch) with realistic multi-platform simulators.",
         C_EMERALD),
        ("Challenge Solved: Transformer CPU Latency",
         "Distilled the model to 6-layer DistilBERT and implemented zero-downtime automatic failover to NLTK VADER.",
         C_SKY),
        ("Future Frontier 1: Distributed Streaming via Kafka",
         "Transition from batch polling to real-time event-driven message streaming via Apache Kafka and Redis for millions of posts per hour.",
         C_AMBER),
        ("Future Frontier 2: Multilingual Afrocentric LLMs",
         "Fine-tune Afrocentric models (AfriBERTa / Naija-BERT) for native understanding of Nigerian Pidgin, Yoruba, Hausa, and Igbo political discourse.",
         C_SKY),
        ("Future Frontier 3: Geospatial GIS Sentiment Heatmaps",
         "Integrate mapping APIs to visualize voter sentiment granularly across Senatorial Districts and Local Government Areas (LGAs).",
         C_ROSE),
        ("Future Frontier 4: Inauthentic Bot & Disinformation Detection",
         "Implement graph neural networks to detect coordinated astroturfing campaigns, bot rings, and artificial sentiment manipulation.",
         C_EMERALD)
    ]

    for i, (rtitle, rdesc, rcol) in enumerate(future_cards):
        col_idx = i % 2
        row_idx = i // 2
        x = 45 + col_idx * 445
        y = 330 - row_idx * 140
        draw_card(c, x, y, 425, 125, fill=C_CARD, stroke=rcol)
        c.setFont('Helvetica-Bold', 11)
        c.setFillColor(rcol)
        c.drawString(x + 16, y + 98, rtitle)
        
        c.setFont('Helvetica', 9)
        c.setFillColor(C_TEXT_SUB)
        words = rdesc.split(); cur_y = y + 78; line = ""
        for w in words:
            test = line + (" " if line else "") + w
            if c.stringWidth(test, 'Helvetica', 9) > 390:
                c.drawString(x + 16, cur_y, line); cur_y -= 14; line = w
            else: line = test
        if line: c.drawString(x + 16, cur_y, line)

    c.showPage()

    # ==========================================
    # SLIDE 13: CONCLUSION & Q&A
    # ==========================================
    c.setFillColor(C_BG)
    c.rect(0, 0, WIDTH, HEIGHT, fill=True, stroke=False)
    # Accent top
    c.setFillColor(C_SKY)
    c.rect(0, HEIGHT - 5, WIDTH * 0.75, 5, fill=True, stroke=False)
    c.setFillColor(C_EMERALD)
    c.rect(WIDTH * 0.75, HEIGHT - 5, WIDTH * 0.25, 5, fill=True, stroke=False)

    draw_card(c, 130, 60, 700, 420, fill=C_CARD, stroke=C_EMERALD, r=8, stroke_width=1.5)

    c.setFont('Helvetica-Bold', 22)
    c.setFillColor(C_EMERALD)
    c.drawCentredString(WIDTH/2, 430, "THANK YOU FOR LISTENING!")

    c.setFont('Helvetica-Bold', 13)
    c.setFillColor(C_SKY)
    c.drawCentredString(WIDTH/2, 400, "Conclusion: Transforming Political Chatter into Democratic Intelligence")

    c.setFont('Helvetica', 10.5)
    c.setFillColor(C_TEXT_MAIN)
    c.drawCentredString(WIDTH/2, 375, "This platform provides election observers, campaigns, journalists, and citizens with an objective,")
    c.drawCentredString(WIDTH/2, 358, "transparent, and data-driven computational instrument for gauging public sentiment in 2027.")

    # Deliverables Box
    draw_card(c, 160, 215, 640, 115, fill=C_BG, stroke=C_BORDER, r=6)
    c.setFont('Helvetica-Bold', 9.5)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(180, 308, "PROJECT ARTIFACTS & DELIVERABLES:")

    c.setFont('Helvetica-Bold', 10)
    c.setFillColor(C_EMERALD)
    c.drawString(180, 288, "• 14,206-Word Academic Project Report:")
    c.setFont('Helvetica', 9.5)
    c.setFillColor(C_TEXT_SUB)
    c.drawString(410, 288, "Hotel_Management_System_Final_Project_Report.docx (18 Tables, 19 Figures)")

    c.setFont('Helvetica-Bold', 10)
    c.setFillColor(C_SKY)
    c.drawString(180, 266, "• Production Full-Stack Codebase:")
    c.setFont('Helvetica', 9.5)
    c.setFillColor(C_TEXT_SUB)
    c.drawString(390, 266, "Python 3.11, Django 4.2, PyTorch with 21 Verified Automated Tests")

    c.setFont('Helvetica-Bold', 10)
    c.setFillColor(C_AMBER)
    c.drawString(180, 244, "• Project Overview Guide & Slides:")
    c.setFont('Helvetica', 9.5)
    c.setFillColor(C_TEXT_SUB)
    c.drawString(385, 244, "Project_Overview.pdf  |  Election_Sentiment_Analysis_Presentation_Slides.pdf")

    # Author signoff
    c.setFont('Helvetica-Bold', 11)
    c.setFillColor(C_TEXT_MAIN)
    c.drawCentredString(WIDTH/2, 175, "OLUSHOLA EMMANUEL SAVI  |  MATRICULATION NO: 220903032")
    c.setFont('Helvetica', 9.5)
    c.setFillColor(C_TEXT_MUTED)
    c.drawCentredString(WIDTH/2, 155, "Supervisor: MR. OWOEYE  |  Head of Department: DR. MRS. YEROKUN")
    c.drawCentredString(WIDTH/2, 138, "Department of Computer Science • Ekiti State University, Ado-Ekiti (EKSU)")

    # Discussion Box
    draw_card(c, 320, 80, 320, 36, fill=C_BG, stroke=C_SKY, r=18)
    c.setFont('Helvetica-Bold', 10)
    c.setFillColor(C_SKY)
    c.drawCentredString(WIDTH/2, 92, "Questions, Feedback & Discussion Are Welcome.")

    c.setFont('Helvetica', 8)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(45, 16, "Olushola Emmanuel Savi (220903032) | B.Sc. Final Year Project Defense | Ekiti State University (EKSU)")
    c.drawRightString(WIDTH - 45, 16, "Slide 13 of 13")
    c.showPage()

    c.save()
    print(f"Generated widescreen presentation PDF: {filename}")

if __name__ == '__main__':
    build_pdf_slides()
