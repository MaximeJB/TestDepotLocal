#pseudocode pour l'exo sur le coca 
# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the user to 
# insert a coin, one at a time, each time informing the user of the amount due. 
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

#pseudo code : le coca est = 50 cents
#exclure les autres integer sauf 25, 10, 5
def distributeur():
    coca = 50
    vingt_cinq = 25
    dix = 10
    cinq = 5

    while coca > 0:
        coins = input("Pour la bouteille de coca, insérez un montant : ")
        int_coins = int(coins)

        # Vérifie si l'entrée est valide
        if int_coins not in [25, 10, 5]:
            print("Nous ne prenons que les pièces de 25, 10, ou 5 centimes.")
            continue

        # Soustrait la pièce insérée
        coca -= int_coins

        # Vérifie si le montant est suffisant ou dépasse
        if coca == 0:
            print("Merci, voici votre bouteille !")
            break
        elif coca < 0:
            print(f"Merci ! Voici votre bouteille et votre monnaie : {-coca} centimes.")
            break
        else:
            print(f"Il vous manque encore {coca} centimes.")


distributeur()


#demander un input, le convertir en integer
#dire a l'user combien de change il recevoir
