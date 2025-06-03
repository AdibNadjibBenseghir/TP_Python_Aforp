import re
from collections import defaultdict

def main():
    # lecture du fichier
    with open("auth.log", "r") as fichier:
        lignes = fichier.readlines()

    ip_counts = defaultdict(int)

    # Parcourir les lignes et extraire les IPs avec "Failed password"
    for ligne in lignes:
        if "Failed password" in ligne:
            # Extraire l'IP avec une regex
            resultat = re.search(r"from (\d+\.\d+\.\d+\.\d+)", ligne)
            if resultat:
                ip = resultat.group(1)
                ip_counts[ip] += 1

    #  Trier et afficher les 5 IPs avec le plus d’échecs
    top_ips = sorted(ip_counts.items(), key=lambda item: item[1], reverse=True)

    print("\nTop 5 des IPs avec le plus d'échecs SSH :")
    for ip, count in top_ips[:5]:
        print(f"{ip} → {count} échec(s)")

if __name__ == "__main__":
    main()
