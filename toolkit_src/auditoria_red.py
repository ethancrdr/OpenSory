import socket
import json
import datetime
import concurrent.futures

def scan_port(port):
    """Intenta conectar a un puerto local para ver si está abierto."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1) # Timeout rápido para localhost
            result = s.connect_ex(('127.0.0.1', port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                return port, service
    except:
        pass
    return None

def main():
    print("[-] Iniciando escaneo de puertos locales (Top 1000)...")
    
    open_ports = []
    # Escaneamos puertos comunes (0-1024) + algunos conocidos
    common_ports = list(range(1, 1025)) + [3389, 8080, 8443, 8000, 27017, 3306, 5432]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(scan_port, port): port for port in common_ports}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                open_ports.append({"port": result[0], "service": result[1]})
                print(f"    [!] Puerto Abierto: {result[0]} ({result[1]})")

    data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "categoria": "Red y Puertos (CIS IG1)",
        "target": "localhost",
        "open_ports": sorted(open_ports, key=lambda x: x['port']),
        "total_scanned": len(common_ports),
        "note": "Este script solo detecta puertos escuchando en interfaz loopback."
    }

    filename = 'auditoria_red_puertos.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    print(f"[+] Éxito: Reporte de puertos generado en '{filename}'.")

if __name__ == '__main__':
    main()
