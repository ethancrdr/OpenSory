import zipfile
import shutil
import os
import generate_enhanced_pdf

def main():
    print("[-] Generando PDF mejorado...")
    generate_enhanced_pdf.create_pdf()
    
    files_to_zip = [
        'inventario_activos.py',
        'auditoria_politicas.py',
        'auditoria_red.py',
        'auditoria_av.py',
        'Guia_Uso_OpenSory.pdf'
    ]
    
    zip_name = 'toolkit_opensory_v1.zip'
    print(f"[-] Creando archivo ZIP: {zip_name}...")
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_zip:
            if os.path.exists(file):
                zipf.write(file)
                print(f"    Agregado: {file}")
            else:
                print(f"    [!] Advertencia: {file} no encontrado.")

    # Move to public
    public_dir = 'public'
    if not os.path.exists(public_dir):
        os.makedirs(public_dir)
        
    print("[-] Moviendo archivos a public/...")
    shutil.copy(zip_name, os.path.join(public_dir, zip_name))
    shutil.copy('Guia_Uso_OpenSory.pdf', os.path.join(public_dir, 'Guia_Uso_OpenSory.pdf'))
    
    print("[+] Éxito. Assets generados y movidos.")

if __name__ == '__main__':
    main()
