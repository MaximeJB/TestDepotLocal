# Ecrivez votre code ici !
nombre1 = input("Entrez un nombre entier !")
nombre2 = input("Entrez un nombre entier !")

if not nombre1.isnumeric() and not nombre2.isnumeric():
   print("Erreur: les deux nombres doivent être des nombres entiers")
raise SystemExit("Fin du programme")

Nombre1 = int(nombre1)
Nombre2 = int(nombre2)

operation = input("mettez l'opération que vous voulez")

#On vérifie que le +, - etc se trouve bien dans la liste, avec "in" + liste
if operation not in ["+", "-", "*", "/"]:
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    raise SystemExit("Fin du programme")

#Simple opération faite avec python
if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    # Vérifie si la variable `nombre2` n'est pas nulle pour la division
    if nombre2 == 0:
        print("Erreur: impossible de diviser par zéro.")
        raise SystemExit("Fin du programme")

    resultat = round(nombre1 / nombre2, 2)

# Affiche le résultat
print(f"Le résultat de l'opération est: {round(resultat, 2)}")