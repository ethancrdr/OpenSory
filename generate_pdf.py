from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo placeholder or Title
        self.set_font('Arial', 'B', 15)
        self.set_text_color(0, 255, 65) # Matrix Green
        self.cell(0, 10, 'OpenSory Security Toolkit', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

def create_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Title
    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, 'Guía de Ejecución y Diagnóstico', 0, 1, 'L')
    pdf.ln(5)

    # Content
    pdf.set_font('Arial', '', 11)
    
    with open('README.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Simple markdown-like parsing for headers
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            pdf.ln(2)
            continue
            
        if line.startswith('###'):
            pdf.ln(3)
            pdf.set_font('Arial', 'B', 12)
            pdf.set_text_color(0, 100, 0)
            pdf.multi_cell(0, 10, line.replace('###', '').strip())
            pdf.set_font('Arial', '', 11)
            pdf.set_text_color(0, 0, 0)
        elif line.startswith('##'):
            pdf.ln(5)
            pdf.set_font('Arial', 'B', 14)
            pdf.set_text_color(0, 0, 0)
            pdf.multi_cell(0, 10, line.replace('##', '').strip())
            pdf.set_font('Arial', '', 11)
        elif line.startswith('#'):
            # Main title already handled but just in case
            pdf.ln(5)
            pdf.set_font('Arial', 'B', 16)
            pdf.multi_cell(0, 10, line.replace('#', '').strip())
            pdf.set_font('Arial', '', 11)
        else:
            pdf.multi_cell(0, 6, line)

    pdf.output('Guia_Uso_OpenSory.pdf')
    print("PDF Generado: Guia_Uso_OpenSory.pdf")

if __name__ == '__main__':
    create_pdf()
