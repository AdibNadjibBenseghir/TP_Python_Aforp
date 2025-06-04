import re



def main():
    
    # Expression régulière IPv4
    ip_regex = r"^(25[0-5]|2[0-4][0-9]|1\d{2}|[1-9]?\d)(\.(25[0-5]|2[0-4][0-9]|1\d{2}|[1-9]?\d)){3}$"
    
    # Fonction pour la lecture du fichier des ips
    def charger_ips_depuis_fichier(nom_fichier):
        ips = []
        with open(nom_fichier, 'r') as fichier:
            for ligne in fichier:
                ips.append(ligne.strip())
        return ips
    
    ips = charger_ips_depuis_fichier('ips.txt')
    
    # V1 version avec tableau
    #ips = ["192.168.1.1",
    #"10.0.0.255",
    #"172.16.254.1",
    #"abc.def.ghi.jkl",
    #"256.256.256.256",
    #"192.168.1.",
    #"192.168.1.01",
    #"0.0.0.0"]
        
        # Test des adresses
    for ip in ips:
        if re.match(ip_regex, ip):
            print(f"{ip} est une @ IP valide.")
        else:
            print(f"{ip} n'est PAS une @ IP valide.")
        
if __name__ == "__main__":
    main()