import json
import platform
import subprocess
import datetime
import os
import sys

def get_system_info():
    """Obtiene información básica del sistema sin dependencias externas."""
    try:
        info = {
            'hostname': platform.node(),
            'os': platform.system(),
            'os_release': platform.release(),
            'os_version': platform.version(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'python_version': platform.python_version()
        }
        return info
    except Exception as e:
        return {'error': str(e)}

def get_installed_software_win():
    """Obtiene software instalado vía PowerShell (más rápido y seguro que wmic)."""
    if platform.system() != 'Windows':
        return ["Solo disponible en Windows"]
    
    # Comando PowerShell para obtener software (filtrando nombre y versión)
    ps_cmd = "Get-CimInstance -ClassName Win32_Product | Select-Object -Property Name, Version | ConvertTo-Json"
    
    try:
        result = subprocess.run(["powershell", "-Command", ps_cmd], capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            return json.loads(result.stdout)
        else:
            return ["No se pudo obtener la lista o permiso denegado."]
    except Exception as e:
        return [f"Error ejecutando PowerShell: {str(e)}"]

def main():
    print("[-] Iniciando inventario de activos...")
    
    timestamp = datetime.datetime.now().isoformat()
    dispositivos = get_system_info()
    
    print("[-] Obteniendo lista de software (esto puede tardar unos segundos)...")
    software = get_installed_software_win()

    data = {
        'timestamp': timestamp,
        'categoria': 'Inventario Activos (CIS IG1)',
        'sistema': dispositivos,
        'software_instalado': software
    }

    filename = f'inventario_{dispositivos["hostname"]}.json'
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"[+] Éxito: Archivo generado '{filename}'.")
        print("[*] Instrucción: Suba este archivo a la carpeta raíz de Evidencias en OneDrive.")
    except IOError as e:
        print(f"[!] Error escribiendo archivo: {e}")

if __name__ == '__main__':
    main()