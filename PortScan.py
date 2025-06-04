import socket
import argparse
import threading
import csv

# Pour le verrou lors de l’écriture dans un fichier ou de l'affichage
lock = threading.Lock()


def scan_port(ip, port, timeout, verbose, results):
    """Scan un port pour vérifier s'il est ouvert."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        with lock:
            print(f"[+] Port {port} ouvert")
            results['open'].append(port)
    except (socket.timeout, ConnectionRefusedError):
        if verbose:
            with lock:
                print(f"[-] Port {port} fermé")
        with lock:
            results['closed'].append(port)
    except Exception as e:
        with lock:
            print(f"[!] Erreur sur le port {port}: {e}")
    finally:
        s.close()


def main():
    parser = argparse.ArgumentParser(description="Mini-scanner de ports TCP")
    parser.add_argument('--ip', required=True, help="Adresse IP à scanner (ex: 192.168.1.1)")
    parser.add_argument('--start-port', required=True, type=int, help="Premier port à scanner")
    parser.add_argument('--end-port', required=True, type=int, help="Dernier port à scanner")
    parser.add_argument('--timeout', type=float, default=0.5, help="Timeout en secondes (défaut: 0.5)")
    parser.add_argument('--threads', type=int, default=50, help="Nb de threads pour accélérer le scan (défaut: 50)")
    parser.add_argument('--verbose', action='store_true', help="Afficher aussi les ports fermés")
    parser.add_argument('--output', type=str, help="Exporter résultat vers fichier texte (.txt) ou CSV (.csv)")
    args = parser.parse_args()

    results = {'open': [], 'closed': []}

    threads = []

    try:
        socket.inet_aton(args.ip)  # Vérifie la validité de l'IP
    except socket.error:
        print("Adresse IP invalide !")
        return

    print(f"Début du scan sur l'hôte {args.ip} de {args.start_port} à {args.end_port}...")

    for port in range(args.start_port, args.end_port + 1):
        t = threading.Thread(target=scan_port, args=(args.ip, port, args.timeout, args.verbose, results))
        t.start()
        threads.append(t)
        # Limite le nombre de threads actifs pour éviter une surcharge mémoire
        if len(threads) >= args.threads:
            for th in threads:
                th.join()
            threads = []

    # S'assurer que tous les threads sont terminés
    for th in threads:
        th.join()

    print("\nScan terminé !")
    print("Ports ouverts :")
    for port in sorted(results['open']):
        print(port)

    # BONUS: Sauvegarde dans un fichier
    if args.output:
        if args.output.endswith('.csv'):
            with open(args.output, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Port', 'Etat'])
                for port in sorted(results['open']):
                    writer.writerow([port, 'Ouvert'])
                if args.verbose:
                    for port in sorted(results['closed']):
                        writer.writerow([port, 'Fermé'])
            print(f"Résultats exportés vers {args.output}")
        else:
            with open(args.output, 'w') as f:
                f.write("Ports ouverts:\n")
                for port in sorted(results['open']):
                    f.write(f"{port}\n")
                if args.verbose:
                    f.write("\nPorts fermés:\n")
                    for port in sorted(results['closed']):
                        f.write(f"{port}\n")
            print(f"Résultats exportés vers {args.output}")


if __name__ == "__main__":
    main()
