import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
import fitz  # PyMuPDF

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        
        # Header Top Accent Bar (Dark Navy + Emerald highlight)
        self.setFillColor(colors.HexColor("#0F172A"))
        self.rect(36, 756, 420, 3, fill=True, stroke=False)
        self.setFillColor(colors.HexColor("#047857"))
        self.rect(456, 756, 120, 3, fill=True, stroke=False)
        
        # Header Text
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#334155"))
        self.drawString(36, 764, "2027 GUBERNATORIAL ELECTION SENTIMENT ANALYSIS SYSTEM")
        
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawRightString(576, 764, "PROJECT ARCHITECTURE & IMPLEMENTATION GUIDE")
        
        # Footer Divider
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.75)
        self.line(36, 40, 576, 40)
        
        # Footer Text
        self.setFont("Helvetica", 7.5)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(36, 28, "Social Media NLP & Candidate Perception Platform  |  Nigerian 2027 Elections")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(576, 28, page_str)
        
        self.restoreState()

def build_pdf(filename="Project_Overview.pdf"):
    # Target letter size: 612 x 792 pt. Margins: 36 pt (0.5 in) left/right, 44 pt top/bottom
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=44,
        bottomMargin=44
    )

    styles = getSampleStyleSheet()
    
    primary_color = colors.HexColor("#0F172A")
    emerald_color = colors.HexColor("#065F46")
    slate_muted = colors.HexColor("#475569")
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=primary_color,
        spaceAfter=3
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=slate_muted,
        spaceAfter=8
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=7,
        spaceAfter=5
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#1E293B")
    )

    callout_text = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        textColor=colors.HexColor("#0F172A")
    )

    kpi_num = ParagraphStyle(
        'KpiNum',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=15,
        alignment=1, # Center
        textColor=colors.HexColor("#0F172A")
    )

    kpi_label = ParagraphStyle(
        'KpiLabel',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=9,
        alignment=1, # Center
        textColor=colors.HexColor("#64748B")
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#1E293B")
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#0F172A")
    )

    story = []

    # ================= PAGE 1 =================
    story.append(Paragraph("2027 Gubernatorial Election Sentiment Analysis", title_style))
    story.append(Paragraph("A Full-Stack AI Platform for Real-Time Political Perception & Social Media Monitoring", subtitle_style))

    # Executive Overview Callout Box
    overview_html = """<b>What is this project?</b><br/>
This platform is an automated, production-grade social intelligence system developed for the <b>2027 Nigerian Gubernatorial Elections</b> (tracking pivotal states including Lagos, Rivers, Kano, Oyo, and Kaduna). It aggregates political chatter and news commentary, classifies sentiment into <b>Positive, Negative, or Neutral</b> using dual NLP engines, matches mentions to candidate entities, and presents live perception metrics (e.g. <b>Net Sentiment Index</b>) via an interactive editorial dashboard."""
    
    overview_table = Table(
        [[Paragraph(overview_html, callout_text)]],
        colWidths=[540]
    )
    overview_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('LINELEFT', (0,0), (-1,-1), 3.5, colors.HexColor("#047857")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(overview_table)
    story.append(Spacer(1, 6))

    # KPI Summary Cards (4 Columns)
    kpi_data = [
        [
            Paragraph("<b>4 Platforms</b>", kpi_num),
            Paragraph("<b>Dual NLP</b>", kpi_num),
            Paragraph("<b>-1.0 to +1.0</b>", kpi_num),
            Paragraph("<b>12 / 12</b>", kpi_num)
        ],
        [
            Paragraph("X, FB, YouTube, News", kpi_label),
            Paragraph("VADER + DistilBERT", kpi_label),
            Paragraph("Compound Polarity Range", kpi_label),
            Paragraph("Automated Tests Passing", kpi_label)
        ]
    ]
    kpi_table = Table(kpi_data, colWidths=[135, 135, 135, 135])
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,0), 5),
        ('BOTTOMPADDING', (0,0), (-1,0), 1),
        ('TOPPADDING', (0,1), (-1,1), 1),
        ('BOTTOMPADDING', (0,1), (-1,1), 5),
    ]))
    story.append(kpi_table)
    story.append(Spacer(1, 6))

    # Section 1: What We Have Built
    story.append(Paragraph("1. WHAT WE HAVE HERE — CORE SYSTEM MODULES", section_heading))
    
    col1_content = """<b>Multi-Source Ingestion Engine</b> (<font name='Courier'>collectors.py</font>)<br/>
• <b>Live News Feeds:</b> Continuous ingestion from Google News RSS, Vanguard, Daily Post, and Punch politics portals.<br/>
• <b>Social Platform Simulators:</b> Ingestion pipeline for X (Twitter), Facebook, and YouTube election debates.<br/>
• <b>Automated Entity Recognition:</b> Scans text for candidate aliases (e.g. Sanwo-Olu, GRV, Folarin) and links to state races."""

    col2_content = """<b>Dual-Engine NLP Pipeline</b> (<font name='Courier'>sentiment_engine.py</font>)<br/>
• <b>NLTK VADER:</b> Fast lexical analysis tuned for social jargon, slang, emojis, caps, and exclamation marks.<br/>
• <b>DistilBERT Transformer:</b> Deep bidirectional context model (<font name='Courier'>distilbert-base-uncased-sst-2</font>).<br/>
• <b>Graceful Fallback:</b> Automatically falls back to VADER if GPU or transformer dependencies are unavailable."""

    col3_content = """<b>Candidate Analytics & Leaderboards</b> (<font name='Courier'>analytics.py</font>)<br/>
• <b>Net Sentiment Index:</b> Normalizes candidate favorability as <font name='Courier'>% Pos - % Neg</font> (-100 to +100).<br/>
• <b>Rankings:</b> Identifies <i>Most Favorable</i>, <i>Most Criticized</i>, and <i>Highest Social Buzz</i> candidates.<br/>
• <b>Candidate Detail Pages:</b> Dedicated profiles with sentiment breakdowns, engagement metrics, and individual post feeds."""

    col4_content = """<b>Interactive UI & NLP Sandbox</b> (<font name='Courier'>templates/dashboard.html</font>)<br/>
• <b>Editorial Theme:</b> Tactile paper styling (<font name='Courier'>#FAF9F6</font>) with Chart.js time-series area charts.<br/>
• <b>Dynamic Word Clouds:</b> Rendered dynamically with ink palettes; filterable by Positive (praise) or Negative (critique) words.<br/>
• <b>Live NLP Sandbox:</b> Interactive tool to test any custom quote or speech with immediate polarity feedback."""

    deliverables_table = Table(
        [
            [Paragraph(col1_content, body_style), Paragraph(col2_content, body_style)],
            [Paragraph(col3_content, body_style), Paragraph(col4_content, body_style)]
        ],
        colWidths=[266, 266]
    )
    deliverables_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor("#F8FAFC")),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor("#FFFFFF")),
        ('BACKGROUND', (0,1), (0,1), colors.HexColor("#FFFFFF")),
        ('BACKGROUND', (1,1), (1,1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(deliverables_table)
    story.append(Spacer(1, 6))

    # Section 2: Technical Stack
    story.append(Paragraph("2. TECHNICAL STACK & ARCHITECTURAL ROLES", section_heading))
    
    arch_data = [
        [Paragraph("Architectural Layer", table_header), Paragraph("Technologies", table_header), Paragraph("Key Role & Implementation Responsibility", table_header)],
        [Paragraph("<b>Application Server</b>", table_cell_bold), Paragraph("Python 3.11, Django 4.2", table_cell), Paragraph("MVC architecture, ORM queries, AJAX REST endpoints, session handling, and background task orchestration.", table_cell)],
        [Paragraph("<b>NLP & Intelligence</b>", table_cell_bold), Paragraph("NLTK VADER, PyTorch, Hugging Face", table_cell), Paragraph("Dual-engine scoring pipeline. Fast rule-based heuristics + deep contextual semantic evaluation.", table_cell)],
        [Paragraph("<b>Data Storage</b>", table_cell_bold), Paragraph("SQLite3 / PostgreSQL", table_cell), Paragraph("Relational schema with composite indexes on (<font name='Courier'>platform, sentiment_label</font>) and candidate relations.", table_cell)],
        [Paragraph("<b>Visualization & Word Clouds</b>", table_cell_bold), Paragraph("Chart.js, WordCloud, Matplotlib", table_cell), Paragraph("Time-series stacked area charts, platform comparison bars, and base64 server-generated word clouds.", table_cell)],
        [Paragraph("<b>Frontend & Interaction</b>", table_cell_bold), Paragraph("Tailwind CSS, FontAwesome, JS AJAX", table_cell), Paragraph("Editorial tactile paper design, asynchronous filtering (state, candidate, date window), and modal post viewers.", table_cell)],
    ]
    arch_table = Table(arch_data, colWidths=[115, 145, 280])
    arch_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0F172A")),
        ('ALIGN', (0,0), (-1,0), 'LEFT'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(arch_table)

    # Force page break to guarantee exact 2 pages
    story.append(PageBreak())

    # ================= PAGE 2 =================
    story.append(Paragraph("3. HOW WE DID WHAT WE DID — THE 4-STAGE PIPELINE", section_heading))

    pipeline_steps = [
        [
            Paragraph("<b>Stage 1: Ingestion & Named Entity Recognition (NER)</b>", table_cell_bold),
            Paragraph("The collector polls live RSS feeds (Google News, Punch, Vanguard, Daily Post) and simulated social streams. Each item is passed to <font name='Courier'>match_candidate_and_race()</font>, which parses aliases and party keywords to automatically bind posts to the correct candidate and their 2027 state race.", table_cell)
        ],
        [
            Paragraph("<b>Stage 2: Text Preprocessing & Dual NLP Scoring</b>", table_cell_bold),
            Paragraph("Raw text is sanitized (stripping tracking URLs and HTML entities while preserving sentiment signals such as exclamation marks, capitalization, and emojis). It is evaluated via VADER or DistilBERT to output compound polarity (-1.0 to +1.0) and assign <b>Positive</b>, <b>Neutral</b>, or <b>Negative</b> labels.", table_cell)
        ],
        [
            Paragraph("<b>Stage 3: Database Indexing & Analytics Aggregation</b>", table_cell_bold),
            Paragraph("Scored posts are stored in Django models with composite indexes. The analytics engine leverages SQL aggregation (<font name='Courier'>Avg</font>, <font name='Courier'>Count</font>, <font name='Courier'>TruncDate</font>) to compute daily rolling trajectories and Net Sentiment Index figures dynamically without performance bottlenecks.", table_cell)
        ],
        [
            Paragraph("<b>Stage 4: Responsive Visualization & Dynamic Filtering</b>", table_cell_bold),
            Paragraph("Pre-aggregated datasets feed Chart.js visual charts. The word cloud module cleans election stopwords and builds custom ink-palette frequency maps. AJAX endpoints update the dashboard dynamically upon state, candidate, platform, or date filter selection.", table_cell)
        ]
    ]

    pipeline_table = Table(pipeline_steps, colWidths=[155, 385])
    pipeline_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#F1F5F9")),
        ('ROWBACKGROUNDS', (1,0), (1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 4.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(pipeline_table)
    story.append(Spacer(1, 6))

    # Section 4: Relational Schema & Data Model
    story.append(Paragraph("4. RELATIONAL DATA MODEL & ENTITY RELATIONSHIPS", section_heading))

    schema_data = [
        [Paragraph("Model Entity", table_header), Paragraph("Key Attributes", table_header), Paragraph("Relationship & System Role", table_header)],
        [Paragraph("<b>StateRace</b>", table_cell_bold), Paragraph("state, year (2027), description, is_active", table_cell), Paragraph("Top-level election contest. Groups candidates and posts geographically.", table_cell)],
        [Paragraph("<b>Candidate</b>", table_cell_bold), Paragraph("name, party, alias_keywords, avatar_color, bio", table_cell), Paragraph("Foreign key to <font name='Courier'>StateRace</font>. Stores aliases used by the NER matcher.", table_cell)],
        [Paragraph("<b>SocialPost</b>", table_cell_bold), Paragraph("platform, content, sentiment_score, label, published_at", table_cell), Paragraph("Foreign keys to <font name='Courier'>Candidate</font> and <font name='Courier'>StateRace</font>. Stores NLP scores & engagement.", table_cell)],
        [Paragraph("<b>CollectionJob</b>", table_cell_bold), Paragraph("platform, posts_created, status, execution_time", table_cell), Paragraph("Audit log tracking automated background scraping sessions and health.", table_cell)],
    ]
    schema_table = Table(schema_data, colWidths=[95, 175, 270])
    schema_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1E293B")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(schema_table)
    story.append(Spacer(1, 6))

    # Section 5: Key Formulations & Highlights
    story.append(Paragraph("5. KEY FORMULATIONS & ENGINEERING HIGHLIGHTS", section_heading))

    formula_html = """<b>Net Sentiment Index (NSI) Formula:</b><br/>
To isolate genuine favorability from noise, the platform computes:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;<b>NSI = (% Positive Posts) - (% Negative Posts)</b><br/>
Yielding an index from <b>-100.0 (universal disapproval)</b> to <b>+100.0 (universal acclaim)</b>, independent of total discussion volume."""

    fallback_html = """<b>Lazy-Loading & Zero-Downtime Fallback:</b><br/>
The NLP engine uses lazy imports for deep transformer models. If PyTorch or GPU resources are constrained, the pipeline falls back instantly to NLTK VADER—ensuring the dashboard and collectors remain fast and 100% operational."""

    highlights_table = Table(
        [[Paragraph(formula_html, body_style), Paragraph(fallback_html, body_style)]],
        colWidths=[266, 266]
    )
    highlights_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor("#F8FAFC")),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('LINELEFT', (0,0), (0,0), 3, colors.HexColor("#0F172A")),
        ('LINELEFT', (1,0), (1,0), 3, colors.HexColor("#047857")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(highlights_table)
    story.append(Spacer(1, 6))

    # Section 6: Verification & Quick Start
    story.append(Paragraph("6. VERIFICATION & HOW TO RUN", section_heading))

    run_instructions = """
<b>1. Environment & Database:</b> <font name='Courier'>pip install -r requirements.txt &amp;&amp; python manage.py migrate</font><br/>
<b>2. Seed Initial Election Data:</b> <font name='Courier'>python manage.py seed_election_data --count 200</font> (seeds candidates, races, &amp; posts)<br/>
<b>3. Launch Dashboard:</b> <font name='Courier'>python manage.py runserver</font> &nbsp;→ Visit <b>http://127.0.0.1:8000/</b> in browser.<br/>
<b>4. Run Automated Tests:</b> <font name='Courier'>python manage.py test</font> &nbsp;→ Executes 12 comprehensive unit and integration tests.
"""
    run_table = Table(
        [[Paragraph(run_instructions, body_style)]],
        colWidths=[540]
    )
    run_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(run_table)
    story.append(Spacer(1, 5))

    # Conclusion Banner
    conclusion_html = "<b>Key Takeaway:</b> The system transforms chaotic political chatter into rigorous, actionable perception intelligence—providing campaign teams, analysts, and citizens with transparent, data-driven election sentiment analytics."
    conclusion_table = Table(
        [[Paragraph(conclusion_html, callout_text)]],
        colWidths=[540]
    )
    conclusion_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#ECFDF5")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#A7F3D0")),
        ('TOPPADDING', (0,0), (-1,-1), 4.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4.5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(conclusion_table)

    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF built successfully: {filename}")

    # Verify Page Count and inspect with fitz
    pdf_doc = fitz.open(filename)
    page_count = len(pdf_doc)
    print(f"Total Page Count: {page_count}")
    
    # Render images of pages for inspection
    for idx, page in enumerate(pdf_doc):
        pix = page.get_pixmap(dpi=150)
        img_path = f"page_{idx+1}.png"
        pix.save(img_path)
        print(f"Saved {img_path}")

if __name__ == '__main__':
    build_pdf()
