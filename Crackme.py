import random



def main():
    
    # Fonction pour la lecture du fichier 
    def charger_mots_depuis_fichier(nom_fichier):
        mots = []
        with open(nom_fichier, 'r') as fichier:
            for ligne in fichier:
                mots.append(ligne.strip())
        return mots
    
    mots = charger_mots_depuis_fichier('motdepasse_faible.txt')
    mot_a_deviner = random.choice(mots)

    # initialisation des essais a 0
    essais = 0
    trouve = False
    # Nombre d'essais maximum
    max_essais = 10
    # Tableau pour l'historique
    historique = []
    
    # ici le jeu Commence 
    print("Devinez le mot de passe faible.")

    while not trouve and essais < max_essais:
        proposition = input("Entrez un mot de passe : ")
        
        if proposition.lower() == "triche":
            print(f"Triche activée ! Le mot de passe est : {mot_a_deviner}")
            continue
        
        essais += 1
        historique.append(proposition)
        
        if proposition == mot_a_deviner:
            trouve = True
            print(f"Vous avez trouvé le mot de passe en {essais} essai.")
        else:
            #  Donner un indice
            print("Mauvais mot de passe.")
            if len(proposition) < len(mot_a_deviner):
                print("Indice : Le mot à deviner est plus long.")
            elif len(proposition) > len(mot_a_deviner):
                print("Indice : Le mot à deviner est plus court.")
            
            if proposition and proposition[0] == mot_a_deviner[0]:
                print("Indice : Il commence par la même lettre.")

            lettres_communes = 0
            for lettre in proposition:
                if lettre in mot_a_deviner:
                    lettres_communes += 1
            print(f"Indice : Il y a {lettres_communes} lettre(s) en commun.")
            
            if essais == max_essais:
                print("Maximum des essaies ATTEIN")

    if not trouve:
        print(f"💥 Mot de passe non trouvé. C'était : {mot_a_deviner}")

    # 5. Afficher l’historique
    print("Historique des tentatives :")
    for i, tentative in enumerate(historique, start=1):
        print(f"{i}. {tentative}")
        
if __name__ == "__main__":
    main()