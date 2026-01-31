import zipfile
import shutil
import os
import sys

# Add toolkit_src to path to import the generator
sys.path.append(os.path.join(os.path.dirname(__file__), 'toolkit_src'))
import generate_enhanced_pdf

def main():
    print("[-] Generando PDF mejorado...")
    # This generates 'Guia_Uso_OpenSory.pdf' in the current working directory (root)
    generate_enhanced_pdf.create_pdf()
    
    # Scripts are now in toolkit_src
    src_dir = 'toolkit_src'
    
    files_to_zip = [
        'inventario_activos.py',
        'auditoria_politicas.py',
        'auditoria_red.py',
        'auditoria_av.py'
    ]
    
    zip_name = 'toolkit_opensory_v1.zip'
    pdf_name = 'Guia_Uso_OpenSory.pdf'
    
    print(f"[-] Creando archivo ZIP: {zip_name}...")
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add Scripts
        for file in files_to_zip:
            file_path = os.path.join(src_dir, file)
            if os.path.exists(file_path):
                # arcname=file ensures they are at the root of the zip, not in a toolkit_src folder
                zipf.write(file_path, arcname=file)
                print(f"    Agregado: {file}")
            else:
                print(f"    [!] Advertencia: {file} no encontrado en {src_dir}.")
        
        # Add PDF (from root)
        if os.path.exists(pdf_name):
            zipf.write(pdf_name, arcname=pdf_name)
            print(f"    Agregado: {pdf_name}")
        else:
            print(f"    [!] Advertencia: {pdf_name} no encontrado.")

    # Move to public
    public_dir = 'public'
    if not os.path.exists(public_dir):
        os.makedirs(public_dir)
        
    print("[-] Copiando archivos a public/...")
    shutil.copy(zip_name, os.path.join(public_dir, zip_name))
    shutil.copy(pdf_name, os.path.join(public_dir, pdf_name))
    
    # Cleanup root artifacts
    print("[-] Limpiando archivos temporales en raiz...")
    try:
        os.remove(zip_name)
        os.remove(pdf_name)
    except OSError as e:
        print(f"    [!] Error borrando temporales: {e}")
    
    print("[+] Éxito. Assets generados y desplegados en public/")

if __name__ == '__main__':
    main()
