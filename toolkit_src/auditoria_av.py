import subprocess
import json
import datetime
import platform

def check_windows_defender():
    """Verifica estado de Antivirus usando PowerShell/WMI (SecurityCenter2)."""
    if platform.system() != 'Windows':
        return {"error": "Solo compatible con Windows"}

    # Comando para consultar SecurityCenter2
    # Nota: productState es un bitmask complejo, simplificamos la salida bruta
    ps_cmd = "Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct | Select-Object displayName, productState, pathToSignedProductExe | ConvertTo-Json"
    
    try:
        result = subprocess.run(["powershell", "-Command", ps_cmd], capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            # A veces devuelve objeto único o array, json.loads lo maneja
            return json.loads(result.stdout)
        else:
            return {"status": "Unknown", "raw_output": result.stderr}
    except Exception as e:
        return {"error": str(e)}

def main():
    print("[-] Verificando estado de la protección Antivirus...")
    
    av_status = check_windows_defender()
    
    data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "categoria": "Defensa contra Malware (CIS IG1)",
        "antivirus_detected": av_status,
        "interpretacion": "Si 'productState' existe, el AV está registrado. Verificar 'hex' code para estado activo/desactualizado."
    }
    
    filename = 'auditoria_antivirus.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"[+] Éxito: Estado AV guardado en '{filename}'.")

if __name__ == '__main__':
    main()
