from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from reportlab.lib.styles import getSampleStyleSheet


def create_report(analysis, report_path):

    documents = SimpleDocTemplate(report_path, pagesize = A4)
    styles = getSampleStyleSheet()
    story = []


    # Title

    story.append(Paragraph("E-Commerce EDA Report",styles["Title"]))
    story.append(Spacer(1,20))


    # Business Insights

    story.append(Paragraph("Business Insights",styles["Heading2"]))
    story.append(Spacer(1,10))

    for key,value in analysis.items():
        if isinstance(value,float):
            value = round(value,2)
        text = (f"<b>{key}:</b>{value}")

        story.append(Paragraph(text,styles["Normal"]))

        story.append(Spacer(1,8))

    documents.build(story)

