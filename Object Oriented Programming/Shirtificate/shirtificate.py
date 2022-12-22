from PIL import Image, ImageOps
from fpdf import FPDF


class pdf:
    def __init__(self, name):
        self.pdf = FPDF('P', 'mm', 'A4')
        self.pdf.add_page()
        self.pdf.set_font("helvetica", "B", 15)
        self.pdf.cell(60, 10, 'CS50 Shirtificate', 0, 1, 'C')
        self.pdf.image("shirtificate.png", w=self.pdf.epw)
        self.pdf.set_font_size(30)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.text(x=50, y=95, txt=f'{name} took CS50')

    def save_writing(self, name):
        self.pdf.output(name)


name = input("Name: ")
PDF = pdf(name)
PDF.save_writing("shirtificate.pdf")
