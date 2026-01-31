from fpdf import FPDF
import datetime

class PDF(FPDF):
    def header(self):
        # Header Background
        self.set_fill_color(37, 150, 190) # OpenLock Blue #2596be
        self.rect(0, 0, 210, 40, 'F')
        
        # Title
        self.set_font('Arial', 'B', 20)
        self.set_text_color(255, 255, 255)
        self.set_xy(15, 12)
        self.cell(0, 10, 'OpenLock Security Suite', 0, 1, 'L')
        
        self.set_font('Arial', '', 10)
        self.set_xy(15, 22)
        self.cell(0, 10, 'Guía Técnica de Ejecución y Diagnóstico CIS v8.1', 0, 1, 'L')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Confidencial - OpenLock 2026 - Página {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, label):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(37, 150, 190)
        self.cell(0, 10, label, 0, 1, 'L')
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.set_text_color(50)
        self.multi_cell(0, 6, body)
        self.ln()

    def info_box(self, title, content):
        self.set_fill_color(240, 248, 255) # Light AliceBlue
        self.set_draw_color(37, 150, 190)
        self.set_font('Arial', 'B', 11)
        self.set_text_color(0, 0, 0)
        
        # Title
        self.cell(0, 8, title, 0, 1, 'L', True)
        
        # Body
        self.set_font('Arial', '', 10)
        self.set_text_color(60)
        self.multi_cell(0, 6, content, 1, 'L', True)
        self.ln(5)

    def code_box(self, text):
        self.set_fill_color(245, 245, 245)
        self.set_draw_color(200, 200, 200)
        self.set_font('Courier', '', 10)
        self.set_text_color(50)
        self.multi_cell(0, 5, text, 1, 'L', True)
        self.ln(5)

def create_pdf():
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Intro
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Introducción', 0, 1)
    pdf.chapter_body(
        "Este documento detalla el procedimiento técnico para la recolección de evidencia de ciberseguridad. "
        "Las herramientas suministradas (OpenLock Toolkit) son scripts de auditoría de solo lectura diseñados para "
        "evaluar la postura de seguridad frente a los Controles CIS v8.1 sin impactar la disponibilidad del servicio."
    )
    
    # Tools Detail
    pdf.ln(5)
    pdf.chapter_title("1. Análisis de Inventario (CIS 1 & 2)")
    pdf.chapter_body(
        "El primer paso para la defensa es conocer qué se está defendiendo. El script `inventario_activos.py` realiza un levantamiento "
        "detallado del hardware y software."
    )
    pdf.info_box("🔧 Detalle Técnico", 
                 "• Software: Lista todas las aplicaciones instaladas vía WMI/Registry.\n"
                 "• Objetivo: Detectar software no autorizado, versiones obsoletas o 'Shadow IT'.\n"
                 "• Archivo generado: inventario_[hostname].json")

    pdf.chapter_title("2. Auditoría de Identidad (CIS 5 & 6)")
    pdf.chapter_body(
        "Los ataques de identidad son el vector más común actual. `auditoria_politicas.py` examina la configuración "
        "local de seguridad de Windows."
    )
    pdf.info_box("🔧 Detalle Técnico", 
                 "• Políticas Password: Verifica longitud mínima, complejidad y bloqueo de cuentas.\n"
                 "• Interpretación: Si la longitud es < 14 caracteres o no hay bloqueo, el riesgo de fuerza bruta es Alto.\n"
                 "• Archivo generado: auditoria_identidad_local.json")

    pdf.chapter_title("3. Superficie de Ataque de Red (CIS 4)")
    pdf.chapter_body(
        "Es crítico minimizar los servicios expuestos. `auditoria_red.py` realiza un escaneo de puertos TCP "
        "en la interfaz local (loopback) para identificar servicios escuchando."
    )
    pdf.info_box("🔧 Detalle Técnico", 
                 "• Escaneo: Top 1000 puertos + puertos críticos (RDP 3389, SQL 1433, SMB 445).\n"
                 "• Riesgo: Puertos como 3389 (RDP) abiertos innecesariamente aumentan el riesgo de Ransomware.\n"
                 "• Archivo generado: auditoria_red_puertos.json")

    pdf.chapter_title("4. Estado de Protección Malware (CIS 10)")
    pdf.chapter_body(
        "Verificación de la eficacia de las herramientas EDR/Antivirus instaladas mediante `auditoria_av.py`."
    )
    pdf.info_box("🔧 Detalle Técnico", 
                 "• Consulta WMI root\\SecurityCenter2.\n"
                 "• Verifica: Que el AV esté registrado, habilitado y con firmas actualizadas.\n"
                 "• Archivo generado: auditoria_antivirus.json")

    # Instructions
    pdf.add_page()
    pdf.chapter_title("Instrucciones de Entrega")
    pdf.chapter_body(
        "Una vez ejecutados los 4 scripts, siga estos pasos para asegurar la cadena de custodia de la evidencia:"
    )
    
    steps = (
        "1. Verifique que se hayan generado los 4 archivos .json en la carpeta del toolkit.\n"
        "2. Comprima los archivos JSON en un único archivo ZIP llamado 'Evidencia_[NombreCliente].zip'.\n"
        "3. Acceda al portal OpenLock y navegue a la Misión 4.\n"
        "4. Use el enlace seguro de OneDrive para cargar el archivo ZIP.\n"
        "5. Haga clic en 'Notificar Finalización' para alertar a nuestro SOC."
    )
    pdf.code_box(steps)  # Reusing code_box style if I implement it, or just plain text
    
    pdf.chapter_body(
        "\nSi encuentra errores durante la ejecución (ej. 'Access Denied'), asegúrese de estar ejecutando "
        "los scripts con privilegios de Administrador (Clic derecho -> Ejecutar como Administrador)."
    )

    pdf.output('Guia_Uso_OpenSory.pdf')
    print("PDF Mejorado Generado: Guia_Uso_OpenSory.pdf")

if __name__ == '__main__':
    create_pdf()
