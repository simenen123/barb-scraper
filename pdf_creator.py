# Write PDF imports
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
import textwrap
import chapters

def create_pdf(the_raw_text, chapter_nr):
    fileName = f'pdfs/chapter-{chapter_nr}.pdf'
    documentTitle = f'chapter-{chapter_nr}'
    title = f'chapter-{chapter_nr}'

    wrapped_lines = []
    for paragraph in the_raw_text.strip().split("\n"):
        wrapped_lines.extend(textwrap.wrap(paragraph, width=90))  # 90 tegn per linje
        wrapped_lines.append("")  # tom linje mellom avsnitt


    # Opprett PDF
    pdf = canvas.Canvas(fileName)
    pdf.setTitle(documentTitle)

    # Tegn tittel øverst
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawCentredString(300, 800, title)  # Y-posisjonen er høyere

    # Tegn linje under tittelen
    pdf.setLineWidth(1)
    pdf.line(30, 790, 570, 790)

    # Plasser tekstinnhold under linjen
    y = 770  # Start rett under linjen
    pdf.setFont("Helvetica", 12)
    for line in wrapped_lines:
        if y < 50:  # Gå til ny side hvis vi er for langt ned
            pdf.showPage()
            y = 800
            pdf.setFont("Helvetica", 12)
        pdf.drawString(50, y, line)
        y -= 16  # Linjeavstand

    # Lagre PDF
    pdf.save()

# create_pdf(chapters.test_chapter)