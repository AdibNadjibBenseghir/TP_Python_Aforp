import re
import matplotlib.pyplot as plt

def analyser_log(fichier_log):
    ips = []
    echecs = []
    succes = []

    with open(fichier_log, "r") as fichier:
        for ligne in fichier:
            if "Failed password" in ligne or "Accepted password" in ligne:
                match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", ligne)
                if match:
                    ip = match.group(1)
                    if ip not in ips:
                        ips.append(ip)
                        echecs.append(0)
                        succes.append(0)
                    
                    index = ips.index(ip)
                    if "Failed password" in ligne:
                        echecs[index] += 1
                    elif "Accepted password" in ligne:
                        succes[index] += 1
    return ips, echecs, succes

def afficher_graphique(ips, echecs, succes):
    # Sélection des 5 IPs avec le plus d’échecs
    top_indexes = sorted(range(len(echecs)), key=lambda i: echecs[i], reverse=True)[:5]
    
    top_ips = [ips[i] for i in top_indexes]
    top_echecs = [echecs[i] for i in top_indexes]
    top_succes = [succes[i] for i in top_indexes]

    x = list(range(len(top_ips)))
    bar_width = 0.4

    plt.figure(figsize=(10, 6))
    plt.bar([i - bar_width/2 for i in x], top_echecs, width=bar_width, color='red', label='Échecs')
    plt.bar([i + bar_width/2 for i in x], top_succes, width=bar_width, color='green', label='Réussites')

    plt.xticks(x, top_ips, rotation=45)
    plt.xlabel("Adresse IP")
    plt.ylabel("Nombre de tentatives")
    plt.title("Top 5 IPs – Connexions SSH (Échecs vs Réussites)")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

def main():
    ips, echecs, succes = analyser_log("auth.log")
    afficher_graphique(ips, echecs, succes)

if __name__ == "__main__":
    main()
