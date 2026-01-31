import json
import subprocess
import platform
import datetime

def get_password_policy():
    """Obtiene la política de contraseñas local usando 'net accounts'."""
    if platform.system() != 'Windows':
        return {"error": "Solo Windows soportado para chequeo de políticas locales"}
    
    try:
        # Ejecuta net accounts
        result = subprocess.run(["net", "accounts"], capture_output=True, text=True)
        if result.returncode != 0:
            return {"error": "No se pudo ejecutar net accounts"}
        
        # Parsea la salida simple
        policy = {}
        for line in result.stdout.splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                policy[key.strip()] = val.strip()
        
        return policy
    except Exception as e:
        return {"error": str(e)}

def main():
    print("[-] Iniciando auditoría de políticas de identidad...")
    
    # 1. Chequeo real de políticas locales (Password length, complexity logic inferred)
    local_policy = get_password_policy()
    
    # 2. Mock MFA Status (Ya que requiere acceso a API Cloud/AD que no tenemos en local script básico)
    # Se deja explicito en el JSON que es un valor manual/mock
    mfa_status = {
        "status": "MANUAL_CHECK_REQUIRED",
        "description": "La verificación de MFA (Azure/Okta) no se puede realizar desde script local.",
        "compliance_note": "Verificar manualmente en portal administrativo si MFA está forzado."
    }

    data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "categoria": "Gestión Identidad (CIS IG2)",
        "politica_local_password": local_policy,
        "mfa_check": mfa_status
    }
    
    filename = 'auditoria_identidad_local.json'
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"[+] Éxito: Política local extraída en '{filename}'.")
        print("[*] Instrucción: Sube este archivo a la carpeta 'Evidencias'.")
    except IOError as e:
        print(f"[!] Error escribiendo archivo: {e}")

if __name__ == '__main__':
    main()
