m = open("requête.sql", "w") 
m.write(requete)
m.close() 
# Lecture d'un fichier CSV ligne par ligne
with open("books.csv", "r", encoding="utf-8") as fichier_csv:
    lignes = fichier_csv.readlines()  # Lire toutes les lignes

# Affichage du contenu
for ligne in lignes:
    print(ligne.strip())  # Affiche chaque ligne sans espaces superflus
requete = "CREATE TABLE auteur (nom VARCHAR(40));" 

ligne = "Auteur1;Titre1;2024;Éditeur1;Science-fiction"
champs = ligne.split(";")  # Découpe les champs
print(champs)  # ['Auteur1', 'Titre1', '2024', 'Éditeur1', 'Science-fiction']

def algorithme(fichier_csv):
    # Lecture du fichier CSV
    with open(fichier_csv, "r", encoding="utf-8") as csv_file:
        lignes = csv_file.readlines()

    # Création des fichiers SQL pour différentes tables
    with open("insertion_auteur.sql", "w") as fichier_auteur, \
         open("insertion_livre.sql", "w") as fichier_livre:
        
        for ligne in lignes[1:]:  # Sauter la première ligne (en-têtes)
            champs = ligne.strip().split(";")  # Adapter au séparateur
            nom_auteur, titre, annee, editeur, genre = champs
            
            # Requête pour la table "auteur"
            fichier_auteur.write(f"INSERT INTO auteur (nom) VALUES ('{nom_auteur}');\n")
            
            # Requête pour la table "livre"
            fichier_livre.write(f"INSERT INTO livre (titre, annee, editeur, genre) "
                                 f"VALUES ('{titre}', {annee}, '{editeur}', '{genre}');\n")
    
    print("Fichiers SQL générés avec succès.")


def algorithme_avec_clee(fichier_csv):
    # Dictionnaire pour stocker les auteurs et leurs IDs
    auteurs = {}
    id_auteur = 1

    with open(fichier_csv, "r", encoding="utf-8") as csv_file:
        lignes = csv_file.readlines()

    with open("insertion_auteur.sql", "w") as fichier_auteur, \
         open("insertion_livre.sql", "w") as fichier_livre:

        for ligne in lignes[1:]:  # Ignorer les entêtes
            champs = ligne.strip().split(";")
            nom_auteur, titre, annee, editeur, genre = champs

            # Ajouter un nouvel auteur s'il n'existe pas déjà
            if nom_auteur not in auteurs:
                auteurs[nom_auteur] = id_auteur
                fichier_auteur.write(f"INSERT INTO auteur (id, nom) VALUES ({id_auteur}, '{nom_auteur}');\n")
                id_auteur += 1

            # Insérer le livre avec la clé étrangère id_auteur
            fichier_livre.write(f"INSERT INTO livre (titre, annee, editeur, genre, id_auteur) "
                                 f"VALUES ('{titre}', {annee}, '{editeur}', '{genre}', {auteurs[nom_auteur]});\n")

    print("Fichiers SQL avancés générés avec succès.")


