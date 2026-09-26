import os
import sys
import docx

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from build_report.helpers import init_document
from build_report.preliminaries import (
    add_title_page, add_certification, add_dedication,
    add_acknowledgments, add_table_of_contents,
    add_list_of_figures, add_list_of_tables, add_abstract
)
from build_report.chapter1 import add_chapter_one
from build_report.chapter2 import add_chapter_two
from build_report.chapter3 import add_chapter_three
from build_report.chapter4 import add_chapter_four
from build_report.chapter5 import add_chapter_five
from build_report.references import add_references

def compile_document():
    print("Initializing document styles and margins...")
    doc = init_document()

    print("Adding Preliminary Pages...")
    add_title_page(doc)
    add_certification(doc)
    add_dedication(doc)
    add_acknowledgments(doc)
    add_table_of_contents(doc)
    add_list_of_figures(doc)
    add_list_of_tables(doc)
    add_abstract(doc)

    print("Adding Chapter One: Introduction...")
    add_chapter_one(doc)

    print("Adding Chapter Two: Literature Review...")
    add_chapter_two(doc)

    print("Adding Chapter Three: Research Methodology...")
    add_chapter_three(doc)

    print("Adding Chapter Four: System Design, Implementation, and Evaluation...")
    add_chapter_four(doc)

    print("Adding Chapter Five: Summary, Recommendations, and Conclusion...")
    add_chapter_five(doc)

    print("Adding References...")
    add_references(doc)

    target_name_1 = "Hotel_Management_System_Final_Project_Report.docx"
    target_name_2 = "Social_Media_Sentiment_Analysis_System_Final_Project_Report.docx"

    print(f"Saving compiled document to '{target_name_1}'...")
    doc.save(target_name_1)

    print(f"Saving companion document to '{target_name_2}'...")
    doc.save(target_name_2)

    # Document statistics
    total_words = sum(len(p.text.split()) for p in doc.paragraphs)
    for t in doc.tables:
        for r in t.rows:
            for c in r.cells:
                total_words += len(c.text.split())

    print("=" * 60)
    print("FINAL YEAR PROJECT REPORT GENERATED SUCCESSFULLY!")
    print(f"Total Paragraphs: {len(doc.paragraphs)}")
    print(f"Total Tables: {len(doc.tables)}")
    print(f"Total Inline Shapes / Figures Embedded: {len(doc.inline_shapes)}")
    print(f"Estimated Total Word Count: {total_words:,} words")
    print(f"Primary Output File: {os.path.abspath(target_name_1)}")
    print(f"Companion File: {os.path.abspath(target_name_2)}")
    print("=" * 60)

if __name__ == '__main__':
    compile_document()
