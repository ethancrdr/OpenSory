from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Green header bar
        self.set_fill_color(0, 0, 0)
        self.rect(0, 0, 210, 20, 'F')
        
        # Title in header
        self.set_font('Arial', 'B', 12)
        self.set_text_color(0, 255, 65) # Neon Green
        self.set_xy(10, 5)
        self.cell(0, 10, 'OPEN SORY | Security Toolkit', 0, 0, 'L')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'OpenSory Confidential - Pagina {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, label):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln(2)
        # Green underline
        self.set_draw_color(0, 200, 50)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.set_text_color(20)
        self.multi_cell(0, 6, body)
        self.ln()

    def code_box(self, text):
        self.set_fill_color(245, 245, 245)
        self.set_draw_color(220, 220, 220)
        self.set_font('Courier', '', 10)
        self.set_text_color(50)
        self.multi_cell(0, 5, text, 1, 'L', True)
        self.ln(5)

def create_pdf():
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Hero Title
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(0, 20, 'Guía de Ejecución y Diagnóstico', 0, 1, 'C')
    pdf.ln(10)

    # Read content
    with open('README.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Manual Parsing for better styling
    buffer = ""
    for line in lines:
        line = line.strip()
        if not line:
            if buffer:
                pdf.chapter_body(buffer)
                buffer = ""
            continue
            
        if line.startswith('###'):
            if buffer:
                pdf.chapter_body(buffer)
                buffer = ""
            # Subsection
            pdf.set_font('Arial', 'B', 12)
            pdf.set_text_color(0, 100, 0)
            pdf.cell(0, 8, line.replace('###', '').strip().upper(), 0, 1)
            
        elif line.startswith('##'):
             if buffer:
                pdf.chapter_body(buffer)
                buffer = ""
             pdf.chapter_title(line.replace('##', '').strip())
             
        elif line.startswith('1. ') or line.startswith('2. ') or line.startswith('3. '):
             if buffer:
                pdf.chapter_body(buffer)
                buffer = ""
             # Highlighted Steps
             pdf.set_font('Arial', 'B', 11)
             pdf.cell(10) # Indent
             pdf.cell(0, 8, "• " + line, 0, 1)
             
        elif "py" in line and "Qué hace:" in line:
            # Script description block attempt
            if buffer: pdf.chapter_body(buffer)
            buffer = ""
            pdf.code_box(line)
            
        else:
            buffer += line + " "

    if buffer:
        pdf.chapter_body(buffer)

    pdf.output('Guia_Uso_OpenSory.pdf')
    print("PDF Estilizado Generado: Guia_Uso_OpenSory.pdf")

if __name__ == '__main__':
    create_pdf()
