# Ecrivez votre code ici
def salaire_mensuel(salaire_annuel) : 
    data = int(salaire_annuel / 12)
    return data

def salaire_hebdomadaire(salaire_mensuel) :
    data_etapes_deux = int(salaire_mensuel / 4)
    return data_etapes_deux

def salaire_horaire(salaire_hebdomadaire, heures_travaillees) : 
    data_etapes_trois = int(salaire_hebdomadaire / heures_travaillees)
    return data_etapes_trois

data_salaire_annuel=int(input("Saissisez votre salaire annuel :"))
data_salaire_mensuel= salaire_mensuel(data_salaire_annuel)
data_salaire_hebdomadaire = salaire_hebdomadaire(data_salaire_mensuel)
data_heures_travaillees=int(input("Saissiez le nombre d'heures travaillées en semaine : "))
resultat = salaire_horaire(data_salaire_mensuel, data_heures_travaillees)
print(f"Votre salaire horaires est de {resultat}")

