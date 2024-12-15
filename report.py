import webbrowser
import os
from fpdf import FPDF
from pathlib import Path

class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill.
    """
    def __init__(self,filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        # Calculate payments with proper rounding to ensure they sum to total
        flatmate1_pay = round(flatmate1.pays(bill, flatmate2), 2)
        flatmate2_pay = round(bill.amount - flatmate1_pay, 2)  # Ensure exact total

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Use relative path for the house image
        image_path = Path(__file__).parent / 'files' / 'house.png'
        if image_path.exists():
            pdf.image(name=str(image_path), w=50, h=50, x=300.0)

        pdf.set_font(family='Times', size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        pdf.cell(w=100,h=40, txt="Period", border=0)
        pdf.cell(w=200,h=40, txt=bill.period, border=0, ln=1)

        pdf.cell(w=100,h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=200,h=40, txt=f"${flatmate1_pay:.2f}", border=0, ln=1)

        pdf.cell(w=100,h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=200,h=40, txt=f"${flatmate2_pay:.2f}", border=0)

        # Create Reports directory if it doesn't exist
        reports_dir = Path(__file__).parent / 'Reports'
        reports_dir.mkdir(exist_ok=True)
        
        # Save the PDF in the Reports directory
        pdf_path = reports_dir / self.filename
        pdf.output(str(pdf_path))
        webbrowser.open(str(pdf_path))
