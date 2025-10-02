# Exemple avec un seul exercice
def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")


def exercice2():
    prenom = input("Entrez votre prénom : ")
    print("Bonjour " + prenom)

# Demande à l'utilisateur quel exercice exécuter
def main():
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":
    main()