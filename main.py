m = open("requête.sql", "w") 

requete = "CREATE TABLE auteur (nom VARCHAR(40));" 

m.write(requete)
m.close() 

def algorithme(fichier):
    donne = open(fichier, "w")