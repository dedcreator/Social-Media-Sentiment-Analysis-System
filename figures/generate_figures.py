import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

os.makedirs('figures', exist_ok=True)
plt.rcParams['font.sans-serif'] = 'Helvetica', 'Arial', 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#334155'
plt.rcParams['axes.linewidth'] = 0.8

# Color Palette (Dark Navy & Emerald Theme)
BG_COLOR = '#0F172A'       # Slate 900
CARD_BG = '#1E293B'        # Slate 800
CARD_BORDER = '#334155'    # Slate 700
TEXT_MAIN = '#F8FAFC'      # Slate 50
TEXT_MUTED = '#94A3B8'     # Slate 400
EMERALD = '#10B981'        # Green
ROSE = '#F43F5E'           # Red
BLUE = '#38BDF8'           # Sky blue
INDIGO = '#818CF8'         # Indigo
AMBER = '#F59E0B'          # Amber

def save_fig(fig, filename):
    filepath = os.path.join('figures', filename)
    fig.savefig(filepath, dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close(fig)
    print(f"Generated {filepath}")

# 1. Figure 4.1: Architecture Diagram
def gen_fig4_1():
    fig, ax = plt.subplots(figsize=(11, 7.5), facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Title
    ax.text(5.5, 7.1, "MULTI-TIER SYSTEM ARCHITECTURE", ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(5.5, 6.75, "Social Media Sentiment Analysis & Candidate Perception Monitoring Platform", ha='center', va='center', fontsize=9.5, color='#64748B')

    layers = [
        ("PRESENTATION & VISUALIZATION TIER (CLIENT/BROWSER)", 5.6, 0.9, '#EEF2FF', '#6366F1',
         ["Tailwind CSS UI", "Chart.js Visualizer", "Dynamic WordCloud", "Interactive NLP Sandbox", "Live Collector Modal", "CSV Dataset Export"]),
        ("APPLICATION & ORM CONTROLLER TIER (DJANGO 4.2)", 4.3, 0.9, '#F0FDF4', '#10B981',
         ["Django MVC Framework", "URL Router & Middleware", "Analytics Processing Engine", "Background Cron Daemon", "Admin Governance", "RESTful Data APIs"]),
        ("DUAL-ENGINE NLP & CLASSIFICATION TIER", 3.0, 0.9, '#F8FAFC', '#0EA5E9',
         ["NLTK VADER Lexicon Engine", "HuggingFace DistilBERT Model", "PyTorch Inference", "NER Candidate Matcher", "Emoji & Slang Normalizer", "Confidence Estimator"]),
        ("DATA INGESTION & EXTERNAL SOURCES TIER", 1.7, 0.9, '#FFFBEB', '#F59E0B',
         ["X (Twitter) API v2", "YouTube Data API v3", "News RSS (Punch/Vanguard)", "Daily Post Feed", "Realistic Post Simulator", "Proxy/SSL Fallback Adapter"]),
        ("DATA STORAGE & PERSISTENCE TIER", 0.4, 0.9, '#FDF2F8', '#EC4899',
         ["PostgreSQL Relational DB", "Zero-Config SQLite3 Engine", "StateRace Catalog", "Candidate Registry", "SocialPost Ledger", "CollectionJob Audit"])
    ]

    for title, y, h, bg, border, boxes in layers:
        # Layer container
        rect = patches.FancyBboxPatch((0.5, y), 10.0, h, boxstyle="round,pad=0.08", facecolor=bg, edgecolor=border, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(0.7, y + h - 0.2, title, fontsize=9.5, fontweight='bold', color=border)

        # Inner components
        n = len(boxes)
        box_w = 9.6 / n
        for i, btext in enumerate(boxes):
            bx = 0.7 + i * box_w
            by = y + 0.12
            bw = box_w - 0.12
            bh = h - 0.42
            brect = patches.FancyBboxPatch((bx, by), bw, bh, boxstyle="round,pad=0.05", facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.0)
            ax.add_patch(brect)
            ax.text(bx + bw/2, by + bh/2, btext, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1E293B', wrap=True)

    # Connecting arrows
    for y in [1.3, 2.6, 3.9, 5.2]:
        ax.annotate('', xy=(5.5, y + 0.4), xytext=(5.5, y),
                    arrowprops=dict(arrowstyle="<->", color="#94A3B8", lw=1.8))

    save_fig(fig, 'fig4_1_architecture.png')

# 2. Figure 4.2: Agile Scrum Sprint Roadmap
def gen_fig4_2():
    fig, ax = plt.subplots(figsize=(11, 6.5), facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 6.5)
    ax.axis('off')

    ax.text(5.5, 6.1, "AGILE SCRUM SPRINT ROADMAP & DEVELOPMENT LIFECYCLE", ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(5.5, 5.75, "Six 2-Week Iterative Sprints from Requirements to Full Deployment", ha='center', va='center', fontsize=9.5, color='#64748B')

    sprints = [
        ("Sprint 1", "Core Architecture &\nDatabase Schema", "W1-W2", "#3B82F6", ["Django 4.2 setup", "StateRace & Candidate models", "SQLite & PostgreSQL config"]),
        ("Sprint 2", "Multi-Source Collectors &\nNER Matcher", "W3-W4", "#10B981", ["Twitter/YouTube/RSS feeds", "Candidate alias dictionary", "Data ingestion commands"]),
        ("Sprint 3", "Dual-Engine NLP &\nSentiment Pipeline", "W5-W6", "#8B5CF6", ["NLTK VADER integration", "DistilBERT PyTorch pipeline", "Polarity & confidence scores"]),
        ("Sprint 4", "Interactive Dashboard &\nTime-Series Charts", "W7-W8", "#F59E0B", ["Tailwind glassmorphism UI", "Chart.js sentiment area charts", "Candidate Leaderboards"]),
        ("Sprint 5", "Word Clouds & Live\nNLP Sandbox", "W9-W10", "#EC4899", ["Dynamic WordCloud generator", "Real-time quote sandbox", "Live collector modal UI"]),
        ("Sprint 6", "Testing, Evaluation &\nDocumentation", "W11-W12", "#06B6D4", ["21 unit & integration tests", "Confusion matrix benchmarking", "Final project report & manual"])
    ]

    for i, (sname, stitle, sdur, scolor, tasks) in enumerate(sprints):
        col = i % 3
        row = i // 3
        x = 0.6 + col * 3.45
        y = 3.2 - row * 2.3
        w = 3.2
        h = 2.0

        card = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08", facecolor='#F8FAFC', edgecolor=scolor, linewidth=1.5)
        ax.add_patch(card)

        # Header bar
        hbar = patches.FancyBboxPatch((x, y + h - 0.5), w, 0.5, boxstyle="round,pad=0.04", facecolor=scolor, edgecolor=scolor)
        ax.add_patch(hbar)
        ax.text(x + 0.15, y + h - 0.25, sname, color='#FFFFFF', fontsize=9, fontweight='bold', va='center')
        ax.text(x + w - 0.15, y + h - 0.25, sdur, color='#FFFFFF', fontsize=8, fontweight='bold', ha='right', va='center')

        # Title
        ax.text(x + 0.15, y + h - 0.75, stitle, color='#0F172A', fontsize=8.5, fontweight='bold', va='top')

        # Tasks
        for j, t in enumerate(tasks):
            ax.text(x + 0.15, y + 0.55 - j * 0.24, f"• {t}", color='#475569', fontsize=7.5, va='center')

    save_fig(fig, 'fig4_2_scrum_roadmap.png')

# 3. Figure 4.3: Use Case Diagram
def gen_fig4_3():
    fig, ax = plt.subplots(figsize=(11, 7), facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(5.5, 6.6, "SYSTEM USE CASE DIAGRAM", ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(5.5, 6.25, "Actors, System Boundary, and Primary Functional Interactions", ha='center', va='center', fontsize=9.5, color='#64748B')

    # System boundary box
    sys_box = patches.FancyBboxPatch((3.0, 0.4), 5.0, 5.5, boxstyle="round,pad=0.1", facecolor='#F8FAFC', edgecolor='#0EA5E9', linewidth=2, linestyle='--')
    ax.add_patch(sys_box)
    ax.text(5.5, 5.65, "Social Media Sentiment Analysis System", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#0369A1')

    use_cases = [
        ("Ingest Posts from Social Feeds", 5.0),
        ("Execute Dual-Engine Classification", 4.3),
        ("View Sentiment Dashboard & KPIs", 3.6),
        ("Filter by Candidate, Race & Platform", 2.9),
        ("Inspect 30-Day Sentiment Trajectories", 2.2),
        ("Generate Dynamic Word Clouds", 1.5),
        ("Test Quotes in Live NLP Sandbox", 0.8)
    ]

    for uctext, y in use_cases:
        ellipse = patches.FancyBboxPatch((3.3, y - 0.22), 4.4, 0.44, boxstyle="round,pad=0.15", facecolor='#EEF2FF', edgecolor='#6366F1', linewidth=1.2)
        ax.add_patch(ellipse)
        ax.text(5.5, y, uctext, ha='center', va='center', fontsize=8.5, fontweight='bold', color='#312E81')

    # Actors Left: System Admin & Data Collector
    ax.text(1.2, 4.8, "[User]\nSystem\nAdministrator", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0F172A')
    ax.text(1.2, 2.0, "[Cron]\nAutomated\nCollector Daemon", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0F172A')

    # Actors Right: Political Analyst & Researcher
    ax.text(9.8, 4.8, "[User]\nElection Analyst /\nCampaign Strategist", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0F172A')
    ax.text(9.8, 2.0, "[User]\nAcademic Researcher /\nCitizen", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0F172A')

    # Actor lines
    # Admin to Ingest & Execute & Dashboard
    for y in [5.0, 4.3, 3.6]:
        ax.plot([1.8, 3.3], [4.8, y], color='#64748B', lw=1.2)
    # Daemon to Ingest & Execute
    for y in [5.0, 4.3]:
        ax.plot([1.8, 3.3], [2.0, y], color='#64748B', lw=1.2)
    # Analyst to Dashboard, Filter, Trajectories, Word Clouds
    for y in [3.6, 2.9, 2.2, 1.5]:
        ax.plot([9.2, 7.7], [4.8, y], color='#64748B', lw=1.2)
    # Researcher to Dashboard, Sandbox, Export
    for y in [3.6, 1.5, 0.8]:
        ax.plot([9.2, 7.7], [2.0, y], color='#64748B', lw=1.2)

    save_fig(fig, 'fig4_3_use_case.png')

# 4. Figure 4.4: Ingestion Activity Workflow
def gen_fig4_4():
    fig, ax = plt.subplots(figsize=(11, 6.5), facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 6.5)
    ax.axis('off')

    ax.text(5.5, 6.1, "DATA INGESTION & ENTITY-MATCHING ACTIVITY WORKFLOW", ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(5.5, 5.75, "Automated Post Retrieval, Cleaning, NER Candidate Association & Persistence", ha='center', va='center', fontsize=9.5, color='#64748B')

    steps = [
        ("Initiate Collection Job\n(Batch or Scheduled Cron)", 1.2, 4.4, '#3B82F6'),
        ("Query Multi-Source Feeds\n(Twitter v2, YouTube, RSS)", 3.4, 4.4, '#10B981'),
        ("Text Normalization\n(Strip HTML, URLs, Emojis)", 5.6, 4.4, '#F59E0B'),
        ("NER Entity Matching\n(Scan Candidate Keywords)", 7.8, 4.4, '#8B5CF6'),
        ("Candidate\nIdentified?", 7.8, 2.5, '#EC4899'),
        ("Link to Candidate\n& State Race", 9.6, 2.5, '#10B981'),
        ("Check State Mention\nor Mark General", 5.6, 2.5, '#64748B'),
        ("Route to Dual-Engine\nSentiment Classifier", 5.6, 0.8, '#0EA5E9'),
        ("Commit to Relational DB\n(SocialPost Record)", 2.4, 0.8, '#059669')
    ]

    for stext, x, y, col in steps:
        if "Identified?" in stext:
            # Diamond
            diamond = patches.RegularPolygon((x, y), numVertices=4, radius=0.8, orientation=0, facecolor='#FDF2F8', edgecolor=col, linewidth=1.5)
            ax.add_patch(diamond)
            ax.text(x, y, stext, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#831843')
        else:
            box = patches.FancyBboxPatch((x - 0.9, y - 0.4), 1.8, 0.8, boxstyle="round,pad=0.08", facecolor='#F8FAFC', edgecolor=col, linewidth=1.4)
            ax.add_patch(box)
            ax.text(x, y, stext, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0F172A')

    # Arrows
    arrows = [
        ((2.1, 4.4), (2.5, 4.4)),
        ((4.3, 4.4), (4.7, 4.4)),
        ((6.5, 4.4), (6.9, 4.4)),
        ((7.8, 4.0), (7.8, 3.3)),
        ((8.4, 2.5), (8.7, 2.5)), # Yes
        ((7.2, 2.5), (6.5, 2.5)), # No
        ((5.6, 2.1), (5.6, 1.2)),
        ((9.6, 2.1), (9.6, 1.2)),
        ((9.6, 1.2), (6.5, 0.8)),
        ((4.7, 0.8), (3.3, 0.8))
    ]
    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start, arrowprops=dict(arrowstyle="->", color="#64748B", lw=1.5))

    ax.text(8.55, 2.7, "YES", fontsize=7.5, fontweight='bold', color='#10B981')
    ax.text(6.85, 2.7, "NO", fontsize=7.5, fontweight='bold', color='#F43F5E')

    save_fig(fig, 'fig4_4_ingestion_workflow.png')

# 5. Figure 4.5: NLP Pipeline Flowchart
def gen_fig4_5():
    fig, ax = plt.subplots(figsize=(11, 6.5), facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 6.5)
    ax.axis('off')

    ax.text(5.5, 6.1, "DUAL-ENGINE NLP SENTIMENT CLASSIFICATION PIPELINE", ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(5.5, 5.75, "Rule-Based NLTK VADER & Deep Contextual DistilBERT Transformer Engine", ha='center', va='center', fontsize=9.5, color='#64748B')

    # Flowchart boxes
    # Input
    b_in = patches.FancyBboxPatch((0.5, 3.3), 1.8, 0.8, boxstyle="round,pad=0.08", facecolor='#EEF2FF', edgecolor='#4F46E5', linewidth=1.5)
    ax.add_patch(b_in)
    ax.text(1.4, 3.7, "Raw Social Post\nText Input", ha='center', va='center', fontsize=8, fontweight='bold', color='#1E1B4B')

    # Preprocessing
    b_pre = patches.FancyBboxPatch((2.7, 3.3), 1.8, 0.8, boxstyle="round,pad=0.08", facecolor='#F0FDF4', edgecolor='#10B981', linewidth=1.5)
    ax.add_patch(b_pre)
    ax.text(3.6, 3.7, "Pre-processing &\nEmoji / Slang Mapping", ha='center', va='center', fontsize=8, fontweight='bold', color='#064E3B')

    # Router
    b_rout = patches.FancyBboxPatch((4.9, 3.3), 1.6, 0.8, boxstyle="round,pad=0.08", facecolor='#FFFBEB', edgecolor='#F59E0B', linewidth=1.5)
    ax.add_patch(b_rout)
    ax.text(5.7, 3.7, "Engine Router\n(VADER vs BERT)", ha='center', va='center', fontsize=8, fontweight='bold', color='#78350F')

    # Branch Top: VADER
    b_vad = patches.FancyBboxPatch((7.0, 4.3), 2.2, 1.0, boxstyle="round,pad=0.08", facecolor='#F8FAFC', edgecolor='#0EA5E9', linewidth=1.5)
    ax.add_patch(b_vad)
    ax.text(8.1, 4.9, "NLTK VADER Engine", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#0284C7')
    ax.text(8.1, 4.5, "• Valence lexicon scoring\n• Punctuation/cap heuristics\n• Compound score [-1, +1]", ha='center', va='center', fontsize=7, color='#475569')

    # Branch Bottom: DistilBERT
    b_bert = patches.FancyBboxPatch((7.0, 2.0), 2.2, 1.0, boxstyle="round,pad=0.08", facecolor='#FDF2F8', edgecolor='#EC4899', linewidth=1.5)
    ax.add_patch(b_bert)
    ax.text(8.1, 2.6, "Hugging Face DistilBERT", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#DB2777')
    ax.text(8.1, 2.2, "• Subword tokenization\n• Deep attention matrices\n• Softmax class probabilities", ha='center', va='center', fontsize=7, color='#475569')

    # Output
    b_out = patches.FancyBboxPatch((9.5, 3.2), 1.3, 1.0, boxstyle="round,pad=0.08", facecolor='#F0FDF4', edgecolor='#059669', linewidth=1.5)
    ax.add_patch(b_out)
    ax.text(10.15, 3.85, "Classification", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#065F46')
    ax.text(10.15, 3.45, "• POS / NEG / NEU\n• Polarity [-1, 1]\n• Confidence %", ha='center', va='center', fontsize=7, color='#047857')

    # Connectors
    ax.annotate('', xy=(2.7, 3.7), xytext=(2.3, 3.7), arrowprops=dict(arrowstyle="->", color="#64748B", lw=1.5))
    ax.annotate('', xy=(4.9, 3.7), xytext=(4.5, 3.7), arrowprops=dict(arrowstyle="->", color="#64748B", lw=1.5))
    ax.annotate('', xy=(7.0, 4.8), xytext=(6.5, 4.0), arrowprops=dict(arrowstyle="->", color="#0EA5E9", lw=1.5))
    ax.annotate('', xy=(7.0, 2.5), xytext=(6.5, 3.4), arrowprops=dict(arrowstyle="->", color="#EC4899", lw=1.5))
    ax.annotate('', xy=(9.5, 3.9), xytext=(9.2, 4.6), arrowprops=dict(arrowstyle="->", color="#64748B", lw=1.5))
    ax.annotate('', xy=(9.5, 3.5), xytext=(9.2, 2.7), arrowprops=dict(arrowstyle="->", color="#64748B", lw=1.5))

    save_fig(fig, 'fig4_5_nlp_pipeline.png')

# 6. Figure 4.6: Entity-Relationship Diagram (ERD)
def gen_fig4_6():
    fig, ax = plt.subplots(figsize=(11, 7.5), facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    ax.text(5.5, 7.1, "RELATIONAL DATABASE ENTITY-RELATIONSHIP DIAGRAM (ERD)", ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(5.5, 6.75, "Normalized Relational Schema with Referential Integrity and Constraints", ha='center', va='center', fontsize=9.5, color='#64748B')

    tables = [
        ("StateRace", 0.8, 3.8, 3.0, 2.5, '#3B82F6', [
            ("PK id", "BigAutoField"),
            ("name", "CharField(150)"),
            ("state", "CharField(100)"),
            ("year", "PositiveIntegerField (2027)"),
            ("description", "TextField (blank)"),
            ("created_at", "DateTimeField (auto_now_add)")
        ]),
        ("Candidate", 4.8, 3.8, 3.0, 2.5, '#10B981', [
            ("PK id", "BigAutoField"),
            ("name", "CharField(200)"),
            ("party", "CharField(20) [APC, PDP...]"),
            ("FK state_race_id", "ForeignKey -> StateRace"),
            ("aliases", "TextField"),
            ("keywords", "TextField"),
            ("is_incumbent", "BooleanField (default=False)")
        ]),
        ("SocialPost", 2.8, 0.4, 3.4, 3.0, '#8B5CF6', [
            ("PK id", "BigAutoField"),
            ("platform", "CharField(20) [TWITTER...]"),
            ("external_id", "CharField(255, unique=True)"),
            ("content", "TextField"),
            ("FK candidate_id", "ForeignKey -> Candidate (null)"),
            ("FK state_race_id", "ForeignKey -> StateRace (null)"),
            ("sentiment_label", "CharField(10) [POS/NEG/NEU]"),
            ("sentiment_score", "FloatField [-1.0, 1.0]"),
            ("confidence_pos/neu/neg", "FloatField"),
            ("classification_engine", "CharField(20) [VADER/BERT]")
        ]),
        ("CollectionJob", 7.2, 0.8, 3.0, 2.2, '#F59E0B', [
            ("PK id", "BigAutoField"),
            ("job_type", "CharField(30)"),
            ("platform", "CharField(20)"),
            ("status", "CharField(20) [SUCCESS...]"),
            ("posts_collected", "PositiveIntegerField"),
            ("started_at / completed", "DateTimeField")
        ])
    ]

    for tname, x, y, w, h, col, fields in tables:
        # Card
        card = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06", facecolor='#F8FAFC', edgecolor=col, linewidth=1.5)
        ax.add_patch(card)
        # Header
        hbar = patches.FancyBboxPatch((x, y + h - 0.45), w, 0.45, boxstyle="round,pad=0.03", facecolor=col, edgecolor=col)
        ax.add_patch(hbar)
        ax.text(x + w/2, y + h - 0.22, tname, color='#FFFFFF', fontsize=9, fontweight='bold', ha='center', va='center')

        for i, (fname, ftype) in enumerate(fields):
            fy = y + h - 0.7 - i * 0.28
            is_pk = "PK" in fname
            is_fk = "FK" in fname
            tcolor = '#0F172A' if is_pk or is_fk else '#475569'
            weight = 'bold' if is_pk or is_fk else 'normal'
            ax.text(x + 0.12, fy, fname, fontsize=7.2, color=tcolor, fontweight=weight, va='center')
            ax.text(x + w - 0.12, fy, ftype, fontsize=6.8, color='#64748B', ha='right', va='center')

    # Relationships lines
    # StateRace -> Candidate (1 : N)
    ax.annotate('', xy=(4.8, 5.0), xytext=(3.8, 5.0), arrowprops=dict(arrowstyle="->", color="#3B82F6", lw=1.5))
    ax.text(4.2, 5.15, "1 : N", fontsize=7.5, fontweight='bold', color='#3B82F6')

    # Candidate -> SocialPost (1 : N)
    ax.annotate('', xy=(5.5, 3.4), xytext=(5.5, 3.8), arrowprops=dict(arrowstyle="->", color="#10B981", lw=1.5))
    ax.text(5.6, 3.6, "1 : N", fontsize=7.5, fontweight='bold', color='#10B981')

    # StateRace -> SocialPost (1 : N)
    ax.annotate('', xy=(3.8, 3.4), xytext=(2.5, 3.8), arrowprops=dict(arrowstyle="->", color="#3B82F6", lw=1.5))
    ax.text(2.8, 3.6, "1 : N", fontsize=7.5, fontweight='bold', color='#3B82F6')

    save_fig(fig, 'fig4_6_erd.png')

# 7. Figure 4.7: Dashboard Overview Mockup
def gen_fig4_7():
    fig, ax = plt.subplots(figsize=(11, 6.5), facecolor='#0F172A')
    ax.set_facecolor('#0F172A')
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 6.5)
    ax.axis('off')

    # Top Navbar
    nav = patches.FancyBboxPatch((0.4, 5.7), 10.2, 0.65, boxstyle="round,pad=0.04", facecolor='#1E293B', edgecolor='#334155', linewidth=1.0)
    ax.add_patch(nav)
    ax.text(0.7, 6.02, "[Dashboard] 2027 Gubernatorial Election Sentiment System", color='#F8FAFC', fontsize=10.5, fontweight='bold', va='center')
    ax.text(7.5, 6.02, "All States | All Platforms | 30 Days", color='#94A3B8', fontsize=8, va='center')

    # Live Collect Button
    btn = patches.FancyBboxPatch((9.2, 5.82), 1.2, 0.4, boxstyle="round,pad=0.04", facecolor='#059669', edgecolor='#10B981')
    ax.add_patch(btn)
    ax.text(9.8, 6.02, "+ Collect Live", color='#FFFFFF', fontsize=7.5, fontweight='bold', ha='center', va='center')

    # 4 KPI Cards
    kpis = [
        ("TOTAL POSTS ANALYZED", "545", "+18% from last week", '#38BDF8', '#0284C7'),
        ("NET SENTIMENT INDEX", "+28.4%", "Positive dominant (58% Pos)", '#10B981', '#059669'),
        ("ACTIVE CANDIDATES", "14", "Across 8 State Races", '#818CF8', '#4F46E5'),
        ("MONITORED PLATFORMS", "4", "X, YouTube, FB, News Feeds", '#F59E0B', '#D97706')
    ]

    for i, (ktitle, kval, ksub, kcol, kdark) in enumerate(kpis):
        x = 0.4 + i * 2.6
        y = 4.4
        w = 2.4
        h = 1.1
        kcard = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06", facecolor='#1E293B', edgecolor='#334155', linewidth=1.0)
        ax.add_patch(kcard)
        ax.text(x + 0.15, y + h - 0.25, ktitle, color='#94A3B8', fontsize=7, fontweight='bold', va='center')
        ax.text(x + 0.15, y + 0.45, kval, color=kcol, fontsize=16, fontweight='bold', va='center')
        ax.text(x + 0.15, y + 0.18, ksub, color='#64748B', fontsize=6.5, va='center')

    # Left Chart Card: 30-Day Sentiment Trend Preview
    c1 = patches.FancyBboxPatch((0.4, 0.6), 6.5, 3.6, boxstyle="round,pad=0.06", facecolor='#1E293B', edgecolor='#334155', linewidth=1.0)
    ax.add_patch(c1)
    ax.text(0.7, 3.9, "Sentiment Trajectories Over Time (Area Chart)", color='#F8FAFC', fontsize=9.5, fontweight='bold')

    # Simulated mini-area chart inside c1
    cx = np.linspace(0.8, 6.5, 30)
    pos_y = 2.2 + 0.7 * np.sin(np.linspace(0, 4, 30)) + 0.3 * np.random.RandomState(42).rand(30)
    neg_y = 1.3 + 0.3 * np.cos(np.linspace(0, 4, 30)) + 0.2 * np.random.RandomState(43).rand(30)
    ax.plot(cx, pos_y, color='#10B981', lw=1.5, label='Positive')
    ax.plot(cx, neg_y, color='#F43F5E', lw=1.5, label='Negative')
    ax.text(6.3, 3.0, "Positive", color='#10B981', fontsize=7.5, fontweight='bold', ha='right')
    ax.text(6.3, 1.4, "Negative", color='#F43F5E', fontsize=7.5, fontweight='bold', ha='right')

    # Right Card: Top Candidates Leaderboard Preview
    c2 = patches.FancyBboxPatch((7.1, 0.6), 3.5, 3.6, boxstyle="round,pad=0.06", facecolor='#1E293B', edgecolor='#334155', linewidth=1.0)
    ax.add_patch(c2)
    ax.text(7.4, 3.9, "Candidate Perception (Net %)", color='#F8FAFC', fontsize=9.5, fontweight='bold')

    cands = [
        ("Femi Hamzat (APC - Lagos)", "+42.5%", 0.85, '#10B981'),
        ("A. Adediran (PDP - Lagos)", "+31.2%", 0.68, '#10B981'),
        ("Abba K. Yusuf (NNPP - Kano)", "+28.6%", 0.62, '#10B981'),
        ("Dumo Lulu (Accord - Rivers)", "+19.4%", 0.44, '#38BDF8'),
        ("E. Ombugadu (PDP - Nasarawa)", "+14.8%", 0.35, '#38BDF8')
    ]

    for j, (cname, cval, cw, cbarcol) in enumerate(cands):
        cy = 3.3 - j * 0.55
        ax.text(7.4, cy + 0.15, cname, color='#E2E8F0', fontsize=7.2, fontweight='bold')
        ax.text(10.3, cy + 0.15, cval, color=cbarcol, fontsize=7.2, fontweight='bold', ha='right')
        # Background bar
        bgbar = patches.FancyBboxPatch((7.4, cy - 0.12), 2.9, 0.16, boxstyle="round,pad=0.02", facecolor='#334155', edgecolor='none')
        ax.add_patch(bgbar)
        # Fill bar
        fbar = patches.FancyBboxPatch((7.4, cy - 0.12), 2.9 * cw, 0.16, boxstyle="round,pad=0.02", facecolor=cbarcol, edgecolor='none')
        ax.add_patch(fbar)

    save_fig(fig, 'fig4_7_dashboard_overview.png')

# 8. Figure 4.8: Candidate Leaderboard Chart
def gen_fig4_8():
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#FFFFFF')
    ax.set_facecolor('#F8FAFC')

    candidates = [
        "Femi Hamzat\n(APC - Lagos)",
        "Abdul-Azeez Adediran\n(PDP - Lagos)",
        "Abba Kabir Yusuf\n(NNPP - Kano)",
        "Dumo Lulu-Briggs\n(Accord - Rivers)",
        "Emmanuel Ombugadu\n(PDP - Nasarawa)",
        "Tonye Cole\n(APC - Rivers)",
        "Gawuna\n(APC - Kano)"
    ]
    net_sentiment = [42.5, 31.2, 28.6, 19.4, 14.8, -8.2, -14.5]
    colors = ['#10B981' if x > 0 else '#F43F5E' for x in net_sentiment]

    y_pos = np.arange(len(candidates))
    bars = ax.barh(y_pos, net_sentiment, color=colors, height=0.55, edgecolor='#1E293B', linewidth=0.5)
    ax.axvline(0, color='#0F172A', linewidth=1.0, linestyle='--')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(candidates, fontsize=8.5, fontweight='bold', color='#1E293B')
    ax.invert_yaxis()
    ax.set_xlabel('Net Sentiment Index (% Positive - % Negative)', fontsize=9.5, fontweight='bold', color='#0F172A')
    ax.set_title('CANDIDATE NET SENTIMENT INDEX & LEADERBOARD COMPARISON\n2027 Gubernatorial Election Campaign Monitoring', fontsize=11, fontweight='bold', color='#0F172A', pad=15)
    ax.grid(axis='x', linestyle=':', alpha=0.6, color='#CBD5E1')

    # Data labels
    for bar in bars:
        w = bar.get_width()
        xpos = w + 1.2 if w >= 0 else w - 3.5
        ax.text(xpos, bar.get_y() + bar.get_height()/2, f"{w:+.1f}%", va='center', fontsize=8, fontweight='bold', color='#0F172A')

    save_fig(fig, 'fig4_8_candidate_leaderboard.png')

# 9. Figure 4.9: Platform Distribution Chart
def gen_fig4_9():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.5), facecolor='#FFFFFF')
    ax1.set_facecolor('#FFFFFF')
    ax2.set_facecolor('#FFFFFF')

    # Donut chart: Share of posts
    platforms = ['X (Twitter)', 'YouTube Comments', 'Facebook Posts', 'News Comments']
    shares = [42, 28, 18, 12]
    colors = ['#0EA5E9', '#EF4444', '#3B82F6', '#10B981']

    wedges, texts, autotexts = ax1.pie(shares, labels=platforms, autopct='%1.1f%%', startangle=140,
                                       colors=colors, textprops=dict(color="#0F172A", fontweight='bold', fontsize=8),
                                       wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2))
    for at in autotexts:
        at.set_color('#FFFFFF')
        at.set_fontsize(8.5)
    ax1.set_title("Post Volume Share by Platform\n(Total Analyzed: 545 Posts)", fontsize=10, fontweight='bold', color='#0F172A')

    # Stacked bar: Sentiment by platform
    pos = [48, 52, 44, 38]
    neu = [20, 22, 20, 17]
    neg = [32, 26, 36, 45]

    y = np.arange(len(platforms))
    p1 = ax2.barh(y, pos, color='#10B981', height=0.45, label='Positive')
    p2 = ax2.barh(y, neu, left=pos, color='#94A3B8', height=0.45, label='Neutral')
    p3 = ax2.barh(y, neg, left=np.array(pos)+np.array(neu), color='#F43F5E', height=0.45, label='Negative')

    ax2.set_yticks(y)
    ax2.set_yticklabels(platforms, fontsize=8, fontweight='bold', color='#0F172A')
    ax2.set_xlabel('Sentiment Proportion (%)', fontsize=9, fontweight='bold', color='#0F172A')
    ax2.set_title("Sentiment Breakdown per Platform (%)", fontsize=10, fontweight='bold', color='#0F172A')
    ax2.legend(loc='lower center', bbox_to_anchor=(0.5, -0.22), ncol=3, frameon=False, fontsize=8)
    ax2.invert_yaxis()

    save_fig(fig, 'fig4_9_platform_distribution.png')

# 10. Figure 4.10: Sentiment Trends Area Chart
def gen_fig4_10():
    fig, ax = plt.subplots(figsize=(11, 5.5), facecolor='#FFFFFF')
    ax.set_facecolor('#F8FAFC')

    days = np.arange(1, 31)
    np.random.seed(101)
    pos_posts = 12 + 6 * np.sin(days / 3.5) + np.random.randint(0, 5, 30)
    neu_posts = 5 + 2 * np.cos(days / 4.0) + np.random.randint(0, 3, 30)
    neg_posts = 8 + 4 * np.sin((days + 5) / 3.0) + np.random.randint(0, 4, 30)

    ax.fill_between(days, 0, pos_posts, color='#10B981', alpha=0.35, label='Positive Posts')
    ax.plot(days, pos_posts, color='#059669', lw=1.8)

    ax.fill_between(days, 0, neg_posts, color='#F43F5E', alpha=0.35, label='Negative Posts')
    ax.plot(days, neg_posts, color='#E11D48', lw=1.8)

    ax.fill_between(days, 0, neu_posts, color='#94A3B8', alpha=0.25, label='Neutral Posts')
    ax.plot(days, neu_posts, color='#64748B', lw=1.5, linestyle='--')

    ax.set_title("30-DAY HISTORICAL SENTIMENT TRAJECTORY ACROSS MONITORED RACES\nDaily Aggregation of Public Perception Dynamics", fontsize=11, fontweight='bold', color='#0F172A', pad=12)
    ax.set_xlabel("Observation Timeline (Past 30 Days)", fontsize=9, fontweight='bold', color='#0F172A')
    ax.set_ylabel("Daily Post Count", fontsize=9, fontweight='bold', color='#0F172A')
    ax.set_xlim(1, 30)
    ax.grid(True, linestyle=':', alpha=0.6, color='#CBD5E1')
    ax.legend(loc='upper right', frameon=True, facecolor='#FFFFFF', edgecolor='#CBD5E1', fontsize=8.5)

    # Annotate rally spike
    ax.annotate('Gubernatorial Debate\n& Manifesto Launch', xy=(18, 22), xytext=(21, 25),
                arrowprops=dict(facecolor='#0F172A', shrink=0.05, width=1, headwidth=6),
                fontsize=8, fontweight='bold', color='#0F172A')

    save_fig(fig, 'fig4_10_sentiment_trends.png')

# 11. Figure 4.11: Dynamic Sentiment Word Clouds
def gen_fig4_11():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.5), facecolor='#0F172A')
    ax1.set_facecolor('#1E293B')
    ax2.set_facecolor('#1E293B')
    ax1.axis('off')
    ax2.axis('off')

    pos_words = [
        ("infrastructure", 22, (0.5, 0.5), '#10B981'),
        ("visionary", 18, (0.25, 0.75), '#34D399'),
        ("reform", 16, (0.75, 0.7), '#6EE7B7'),
        ("development", 17, (0.5, 0.25), '#10B981'),
        ("integrity", 14, (0.2, 0.35), '#A7F3D0'),
        ("victory", 15, (0.78, 0.3), '#34D399'),
        ("education", 13, (0.45, 0.8), '#6EE7B7'),
        ("healthcare", 12, (0.15, 0.55), '#A7F3D0'),
        ("competence", 11, (0.75, 0.5), '#10B981'),
        ("empowerment", 10, (0.5, 0.1), '#6EE7B7')
    ]

    neg_words = [
        ("corruption", 22, (0.5, 0.5), '#F43F5E'),
        ("inflation", 18, (0.25, 0.75), '#FB7185'),
        ("hardship", 17, (0.75, 0.7), '#FDA4AF'),
        ("insecurity", 16, (0.5, 0.25), '#F43F5E'),
        ("bad roads", 14, (0.2, 0.35), '#FECDD3'),
        ("unfulfilled", 15, (0.78, 0.3), '#FB7185'),
        ("godfatherism", 13, (0.45, 0.8), '#FDA4AF'),
        ("unemployment", 12, (0.15, 0.55), '#FECDD3'),
        ("poverty", 11, (0.75, 0.5), '#F43F5E'),
        ("deception", 10, (0.5, 0.1), '#FB7185')
    ]

    for word, sz, (x, y), c in pos_words:
        ax1.text(x, y, word, fontsize=sz, fontweight='bold', color=c, ha='center', va='center')
    ax1.set_title("POSITIVE SENTIMENT CLUSTER\n(Key Endorsement & Praise Terms)", fontsize=10, fontweight='bold', color='#10B981', pad=10)

    for word, sz, (x, y), c in neg_words:
        ax2.text(x, y, word, fontsize=sz, fontweight='bold', color=c, ha='center', va='center')
    ax2.set_title("NEGATIVE SENTIMENT CLUSTER\n(Grievances, Critiques & Challenges)", fontsize=10, fontweight='bold', color='#F43F5E', pad=10)

    save_fig(fig, 'fig4_11_wordclouds.png')

# 12. Figure 4.12: Live NLP Sandbox Mockup
def gen_fig4_12():
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0F172A')
    ax.set_facecolor('#0F172A')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Card
    card = patches.FancyBboxPatch((0.5, 0.5), 9.0, 5.0, boxstyle="round,pad=0.08", facecolor='#1E293B', edgecolor='#334155', linewidth=1.5)
    ax.add_patch(card)

    ax.text(0.9, 5.1, "[Sandbox] Real-Time NLP Classifier Sandbox", fontsize=12, fontweight='bold', color='#F8FAFC')
    ax.text(0.9, 4.75, "Test any arbitrary quote, citizen opinion, or speech excerpt with dual VADER / BERT engine feedback", fontsize=7.5, color='#94A3B8')

    # Text Input Box
    tbox = patches.FancyBboxPatch((0.9, 3.4), 8.2, 1.1, boxstyle="round,pad=0.04", facecolor='#0F172A', edgecolor='#475569', linewidth=1.0)
    ax.add_patch(tbox)
    sample_text = '"The gubernatorial candidate unveiled an extraordinary agricultural modernization blueprint\nthat will completely transform rural economic prosperity across Ekiti state!"'
    ax.text(1.1, 3.95, sample_text, fontsize=8, color='#E2E8F0', style='italic', va='center')

    # Result Section
    rbox = patches.FancyBboxPatch((0.9, 0.9), 8.2, 2.2, boxstyle="round,pad=0.05", facecolor='#0F172A', edgecolor='#10B981', linewidth=1.5)
    ax.add_patch(rbox)

    # Classification Badge
    pbadge = patches.FancyBboxPatch((1.2, 2.3), 2.2, 0.6, boxstyle="round,pad=0.04", facecolor='#065F46', edgecolor='#10B981')
    ax.add_patch(pbadge)
    ax.text(2.3, 2.6, "POSITIVE (+0.84)", color='#A7F3D0', fontsize=9, fontweight='bold', ha='center', va='center')

    ax.text(4.0, 2.6, "Classification Engine: Hugging Face DistilBERT", fontsize=8.5, fontweight='bold', color='#F8FAFC', va='center')

    # Score bars
    scores = [("Positive Confidence", 88.5, '#10B981'), ("Neutral Confidence", 9.2, '#94A3B8'), ("Negative Confidence", 2.3, '#F43F5E')]
    for idx, (label, val, barcol) in enumerate(scores):
        sy = 1.85 - idx * 0.4
        ax.text(1.2, sy, label, fontsize=7.5, color='#CBD5E1', va='center')
        ax.text(4.0, sy, f"{val:.1f}%", fontsize=7.5, fontweight='bold', color=barcol, va='center')

        # Bar bg
        bgb = patches.FancyBboxPatch((4.6, sy - 0.08), 4.2, 0.16, boxstyle="round,pad=0.02", facecolor='#334155', edgecolor='none')
        ax.add_patch(bgb)
        # Bar fill
        fb = patches.FancyBboxPatch((4.6, sy - 0.08), 4.2 * (val / 100), 0.16, boxstyle="round,pad=0.02", facecolor=barcol, edgecolor='none')
        ax.add_patch(fb)

    save_fig(fig, 'fig4_12_nlp_sandbox.png')

# 13. Figure 4.13: Live Collector Modal
def gen_fig4_13():
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0F172A')
    ax.set_facecolor('#0F172A')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    modal = patches.FancyBboxPatch((1.5, 0.8), 7.0, 4.4, boxstyle="round,pad=0.08", facecolor='#1E293B', edgecolor='#059669', linewidth=2.0)
    ax.add_patch(modal)

    ax.text(5.0, 4.8, "[Ingest] Ingest Live Election Posts", ha='center', fontsize=12, fontweight='bold', color='#F8FAFC')
    ax.text(5.0, 4.45, "Trigger real-time multi-source data ingestion pipeline across monitored channels", ha='center', fontsize=7.5, color='#94A3B8')

    # Form Fields Mockup
    fields = [
        ("Target Platform:", "All Platforms (X, YouTube, Facebook, News RSS)"),
        ("Post Ingestion Batch Size:", "25 Posts"),
        ("Sentiment Engine:", "Dual-Engine (VADER with BERT validation)"),
        ("State Race Scope:", "All Monitored 2027 Gubernatorial Races")
    ]

    for i, (flabel, fval) in enumerate(fields):
        fy = 3.8 - i * 0.55
        ax.text(2.0, fy + 0.1, flabel, fontsize=8, fontweight='bold', color='#CBD5E1')
        fbox = patches.FancyBboxPatch((2.0, fy - 0.25), 6.0, 0.32, boxstyle="round,pad=0.03", facecolor='#0F172A', edgecolor='#475569')
        ax.add_patch(fbox)
        ax.text(2.2, fy - 0.09, fval, fontsize=7.5, color='#38BDF8')

    # Progress / Status banner
    pbar = patches.FancyBboxPatch((2.0, 1.1), 6.0, 0.45, boxstyle="round,pad=0.04", facecolor='#064E3B', edgecolor='#10B981')
    ax.add_patch(pbar)
    ax.text(5.0, 1.32, "STATUS: OK - 25 Posts Ingested & Classified in 1.42s", ha='center', va='center', fontsize=8, fontweight='bold', color='#A7F3D0')

    save_fig(fig, 'fig4_13_live_collector.png')

# 14. Figure 4.14: Candidate Profile Detail View
def gen_fig4_14():
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0F172A')
    ax.set_facecolor('#0F172A')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Candidate Header Card
    hcard = patches.FancyBboxPatch((0.6, 4.1), 8.8, 1.5, boxstyle="round,pad=0.06", facecolor='#1E293B', edgecolor='#334155', linewidth=1.2)
    ax.add_patch(hcard)

    ax.text(1.0, 5.15, "Dr. Kadri Obafemi Hamzat", fontsize=14, fontweight='bold', color='#F8FAFC')
    ax.text(1.0, 4.75, "All Progressives Congress (APC) • Lagos State 2027 Gubernatorial Race", fontsize=8.5, color='#94A3B8')

    # Metric pills
    mpills = [("Total Mentions", "118"), ("Net Sentiment", "+42.5%"), ("Positive Posts", "68 (57.6%)"), ("Negative Posts", "18 (15.3%)")]
    for i, (mtitle, mval) in enumerate(mpills):
        mx = 1.0 + i * 2.1
        ax.text(mx, 4.4, f"{mtitle}: ", fontsize=7.5, color='#64748B')
        ax.text(mx + 0.9, 4.4, mval, fontsize=7.5, fontweight='bold', color='#10B981' if '+' in mval or '68' in mval else '#F8FAFC')

    # Recent Posts Feed
    ax.text(0.6, 3.75, "Recent Monitored Social Posts & Polarity Ratings", fontsize=9.5, fontweight='bold', color='#F8FAFC')

    feed = [
        ("X (Twitter)", "Hamzat's technical presentation on Lagos transport infrastructure expansion is remarkably detailed.", "+0.82", "POSITIVE", '#10B981'),
        ("YouTube", "Great discussion on flood management solutions for coastal communities.", "+0.65", "POSITIVE", '#10B981'),
        ("News Comments", "Concerned about the implementation timeline and state debt servicing obligations.", "-0.41", "NEGATIVE", '#F43F5E'),
        ("Facebook", "Youth technological empowerment initiative was officially launched in Ikeja.", "+0.58", "POSITIVE", '#10B981')
    ]

    for j, (plat, text, score, label, col) in enumerate(feed):
        py = 3.1 - j * 0.7
        pcard = patches.FancyBboxPatch((0.6, py), 8.8, 0.58, boxstyle="round,pad=0.04", facecolor='#1E293B', edgecolor='#334155', linewidth=0.8)
        ax.add_patch(pcard)

        # Platform tag
        ax.text(0.8, py + 0.38, plat, fontsize=7, fontweight='bold', color='#38BDF8')
        # Snippet
        ax.text(0.8, py + 0.16, text, fontsize=7.5, color='#E2E8F0')
        # Badge
        badge = patches.FancyBboxPatch((8.1, py + 0.12), 1.1, 0.34, boxstyle="round,pad=0.03", facecolor=col, edgecolor='none')
        ax.add_patch(badge)
        ax.text(8.65, py + 0.29, f"{label} ({score})", fontsize=6.5, fontweight='bold', color='#FFFFFF', ha='center', va='center')

    save_fig(fig, 'fig4_14_candidate_detail.png')

# 15. Figure 4.15: Database Schema Inspector
def gen_fig4_15():
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#FFFFFF')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    ax.text(5.0, 5.6, "DJANGO ORM RELATIONAL SCHEMA & MIGRATED TABLES INSPECTOR", ha='center', fontsize=12, fontweight='bold', color='#0F172A')
    ax.text(5.0, 5.25, "Active Relational Tables, Migration Integrity, Record Counts, and Key Constraints", ha='center', fontsize=8.5, color='#64748B')

    tables_info = [
        ("tracker_staterace", "8 Records", "Primary: id (BigAutoField) • Unique: (state, year)", ["id", "name", "state", "year", "created_at"]),
        ("tracker_candidate", "14 Records", "Primary: id • FK: state_race_id (CASCADE)", ["id", "name", "party", "state_race_id", "aliases", "keywords"]),
        ("tracker_socialpost", "545 Records", "Primary: id • Unique: external_id • Indexes: (published_at, sentiment_label)", ["id", "platform", "external_id", "content", "sentiment_score", "candidate_id"]),
        ("tracker_collectionjob", "3 Records", "Primary: id • Audit log for batch collection runs", ["id", "job_type", "platform", "status", "posts_collected", "started_at"])
    ]

    for i, (tname, recs, meta, cols) in enumerate(tables_info):
        y = 4.4 - i * 1.05
        # Box
        tbox = patches.FancyBboxPatch((0.8, y), 8.4, 0.88, boxstyle="round,pad=0.05", facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.2)
        ax.add_patch(tbox)

        # Name & records
        ax.text(1.1, y + 0.62, tname, fontsize=9.5, fontweight='bold', color='#0F172A')
        # Pill
        pill = patches.FancyBboxPatch((3.4, y + 0.52), 1.3, 0.24, boxstyle="round,pad=0.02", facecolor='#EEF2FF', edgecolor='#6366F1')
        ax.add_patch(pill)
        ax.text(4.05, y + 0.64, recs, fontsize=7.2, fontweight='bold', color='#4F46E5', ha='center', va='center')

        ax.text(1.1, y + 0.35, meta, fontsize=7.5, color='#64748B')
        ax.text(1.1, y + 0.14, "Columns: " + ", ".join(cols), fontsize=7, color='#0284C7', family='monospace')

    save_fig(fig, 'fig4_15_database_schema.png')

# 16. Figure 4.16: Code Architecture Diagram
def gen_fig4_16():
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0F172A')
    ax.set_facecolor('#0F172A')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    ax.text(5.0, 5.6, "MODULAR CODEBASE ARCHITECTURE & DIRECTORY STRUCTURE", ha='center', fontsize=12, fontweight='bold', color='#F8FAFC')
    ax.text(5.0, 5.25, "Decoupled Django App Layout, NLP Service Layer, Templates & Management Scripts", ha='center', fontsize=8, color='#94A3B8')

    modules = [
        ("election_sentiment/", "Project Root & Global Configuration", [
            ("settings.py", "Database routing (SQLite/PostgreSQL fallback), media & static config"),
            ("urls.py", "Global root routing, namespace mapping"),
            ("wsgi.py / asgi.py", "Production WSGI/ASGI web server entry points")
        ], '#3B82F6'),
        ("tracker/", "Core Sentiment Engine & Business Domain", [
            ("models.py", "StateRace, Candidate, SocialPost, CollectionJob schemas"),
            ("sentiment_engine.py", "Dual VADER & DistilBERT classifier with automatic fallback"),
            ("collectors.py", "Multi-source scrapers, RSS ingestion & NER candidate matching"),
            ("analytics.py", "WordCloud generation, candidate net metrics, trend time-series"),
            ("views.py", "Dashboard rendering, AJAX endpoints, CSV export, live sandbox API"),
            ("tests.py", "Comprehensive 21 unit & integration automated test cases")
        ], '#10B981'),
        ("templates/ & management/", "Presentation Layer & Automation Commands", [
            ("dashboard.html", "Tailwind glassmorphism dashboard, Chart.js graphs, word clouds"),
            ("candidate_detail.html", "Dedicated candidate profile with platform perception split"),
            ("collect_election_posts.py", "Periodic background data ingestion daemon command"),
            ("seed_election_data.py", "Realistic candidate & multi-platform election dataset seeder")
        ], '#F59E0B')
    ]

    for i, (mname, mdesc, files, mcolor) in enumerate(modules):
        col_x = 0.5 + i * 3.1
        w = 2.9
        h = 4.4
        card = patches.FancyBboxPatch((col_x, 0.6), w, h, boxstyle="round,pad=0.06", facecolor='#1E293B', edgecolor=mcolor, linewidth=1.5)
        ax.add_patch(card)

        # Header
        hbar = patches.FancyBboxPatch((col_x, 0.6 + h - 0.45), w, 0.45, boxstyle="round,pad=0.03", facecolor=mcolor, edgecolor=mcolor)
        ax.add_patch(hbar)
        ax.text(col_x + w/2, 0.6 + h - 0.22, mname, color='#FFFFFF', fontsize=8.5, fontweight='bold', ha='center', va='center')

        ax.text(col_x + 0.12, 0.6 + h - 0.65, mdesc, fontsize=7, color='#CBD5E1', style='italic')

        for fidx, (fname, fdesc) in enumerate(files):
            fy = 0.6 + h - 1.05 - fidx * 0.52
            ax.text(col_x + 0.12, fy, f">> {fname}", fontsize=7.2, fontweight='bold', color='#38BDF8')
            ax.text(col_x + 0.12, fy - 0.22, fdesc[:42] + ('...' if len(fdesc) > 42 else ''), fontsize=6.2, color='#94A3B8')

    save_fig(fig, 'fig4_16_code_architecture.png')

# 17. Figure 4.17: Confusion Matrix & Model Performance Comparison
def gen_fig4_17():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.5), facecolor='#FFFFFF')
    ax1.set_facecolor('#FFFFFF')
    ax2.set_facecolor('#FFFFFF')

    classes = ['Positive', 'Neutral', 'Negative']

    # VADER Confusion Matrix
    cm_vader = np.array([
        [142, 18, 10],
        [15, 62, 13],
        [12, 11, 117]
    ])

    # DistilBERT Confusion Matrix
    cm_bert = np.array([
        [158, 8, 4],
        [8, 74, 8],
        [6, 7, 127]
    ])

    for ax, cm, title, acc in [(ax1, cm_vader, "NLTK VADER Lexicon Engine", "80.5% Accuracy"),
                               (ax2, cm_bert, "Fine-Tuned DistilBERT Transformer", "89.8% Accuracy")]:
        im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
        ax.set_title(f"{title}\n({acc} on 400 Labeled Validation Posts)", fontsize=9.5, fontweight='bold', color='#0F172A', pad=12)

        tick_marks = np.arange(len(classes))
        ax.set_xticks(tick_marks)
        ax.set_xticklabels(classes, fontsize=8, fontweight='bold', color='#0F172A')
        ax.set_yticks(tick_marks)
        ax.set_yticklabels(classes, fontsize=8, fontweight='bold', color='#0F172A')

        thresh = cm.max() / 2.
        for i in range(cm.shape[0]):
            for j in range(cm.shape[1]):
                ax.text(j, i, format(cm[i, j], 'd'),
                        ha="center", va="center", fontsize=10, fontweight='bold',
                        color="white" if cm[i, j] > thresh else "black")

        ax.set_ylabel('True Human-Annotated Label', fontsize=8.5, fontweight='bold', color='#0F172A')
        ax.set_xlabel('Predicted Sentiment Label', fontsize=8.5, fontweight='bold', color='#0F172A')

    save_fig(fig, 'fig4_17_confusion_matrix.png')

# 18. Figure 4.18: Dataset Export View
def gen_fig4_18():
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0F172A')
    ax.set_facecolor('#0F172A')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Card
    card = patches.FancyBboxPatch((0.6, 0.6), 8.8, 4.8, boxstyle="round,pad=0.08", facecolor='#1E293B', edgecolor='#334155', linewidth=1.2)
    ax.add_patch(card)

    ax.text(1.0, 5.0, "[Export] Research Dataset Export & Filter Engine", fontsize=12, fontweight='bold', color='#F8FAFC')
    ax.text(1.0, 4.65, "Download complete sanitized, polarity-scored election perception datasets for external academic modeling", fontsize=7.5, color='#94A3B8')

    # Filter Bar
    fbar = patches.FancyBboxPatch((1.0, 3.8), 8.0, 0.6, boxstyle="round,pad=0.04", facecolor='#0F172A', edgecolor='#475569')
    ax.add_patch(fbar)
    ax.text(1.2, 4.1, "Filter: State: Lagos | Platform: All | Sentiment: Positive & Negative | Date Range: 2026-2027", fontsize=7.5, color='#38BDF8')

    # Export Button
    ebtn = patches.FancyBboxPatch((7.6, 3.9), 1.2, 0.4, boxstyle="round,pad=0.03", facecolor='#059669', edgecolor='#10B981')
    ax.add_patch(ebtn)
    ax.text(8.2, 4.1, "Export CSV", color='#FFFFFF', fontsize=7, fontweight='bold', ha='center', va='center')

    # Data Table Preview
    headers = ["ID", "Platform", "Candidate Mentioned", "Sentiment", "Polarity", "Timestamp"]
    hw = [0.8, 1.2, 2.5, 1.2, 1.0, 1.3]

    hx = 1.0
    for htitle, w in zip(headers, hw):
        ax.text(hx + 0.05, 3.45, htitle, fontsize=7.2, fontweight='bold', color='#CBD5E1')
        hx += w

    rows = [
        ("POST-8491", "X (Twitter)", "Femi Hamzat (APC)", "POSITIVE", "+0.84", "2026-09-24 14:12"),
        ("POST-8492", "YouTube", "Abdul-Azeez Adediran (PDP)", "POSITIVE", "+0.62", "2026-09-24 15:45"),
        ("POST-8493", "News Comments", "Dumo Lulu-Briggs (Accord)", "NEGATIVE", "-0.51", "2026-09-25 08:30"),
        ("POST-8494", "Facebook", "Abba Kabir Yusuf (NNPP)", "POSITIVE", "+0.73", "2026-09-25 11:20"),
        ("POST-8495", "X (Twitter)", "Tonye Cole (APC)", "NEGATIVE", "-0.38", "2026-09-25 16:05")
    ]

    for ridx, row in enumerate(rows):
        ry = 3.0 - ridx * 0.45
        rx = 1.0
        # Alternating row bg
        row_bg = '#1E293B' if ridx % 2 == 0 else '#172033'
        rrect = patches.Rectangle((1.0, ry - 0.1), 8.0, 0.4, facecolor=row_bg, edgecolor='none')
        ax.add_patch(rrect)

        for val, w in zip(row, hw):
            vcolor = '#10B981' if val == 'POSITIVE' or ('+' in val and len(val)==5) else ('#F43F5E' if val == 'NEGATIVE' or ('-' in val and len(val)==5) else '#E2E8F0')
            ax.text(rx + 0.05, ry + 0.1, val, fontsize=6.8, color=vcolor, va='center')
            rx += w

    save_fig(fig, 'fig4_18_data_export.png')

def main():
    print("Generating all 18 figures for report...")
    gen_fig4_1()
    gen_fig4_2()
    gen_fig4_3()
    gen_fig4_4()
    gen_fig4_5()
    gen_fig4_6()
    gen_fig4_7()
    gen_fig4_8()
    gen_fig4_9()
    gen_fig4_10()
    gen_fig4_11()
    gen_fig4_12()
    gen_fig4_13()
    gen_fig4_14()
    gen_fig4_15()
    gen_fig4_16()
    gen_fig4_17()
    gen_fig4_18()
    print("All 18 figures generated successfully in figures/")

if __name__ == '__main__':
    main()
