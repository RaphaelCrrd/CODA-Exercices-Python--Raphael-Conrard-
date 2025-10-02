# Exemple avec un seul exercice
def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")


def exercice2():
    prenom = input("Entrez votre prénom : ")
    print("Bonjour " + prenom)

def exercice3():
    print(" Première ligne \nDeuxieme ligne \nTroisieme ligne")

def exercice4(): 
    annee_naissance = int(input("Entrez votre année de naissance : "))
    age = 2025 - annee_naissance
    print("Vous avez environ", age, "ans")

def exercice5():
    nombre1 = int(input("Entrez un premier nombre :"))
    nombre2 = int(input("Entrez un deuxième nombre :"))
    print(nombre1, " + ",nombre2, " = ", nombre1+nombre2 )

def exercice6():
    nombre1 = int(input("Entrez un premier nombre :"))
    nombre2 = int(input("Entrez un deuxième nombre :"))
    print(nombre1, " - ",nombre2, " = ", nombre1-nombre2 )

def exercice7():
    nombre1 = int(input("Entrez un premier nombre :"))
    nombre2 = int(input("Entrez un deuxième nombre :"))
    print(nombre1, " x ",nombre2, " = ", nombre1*nombre2 )


# Demande à l'utilisateur quel exercice exécuter
def main():
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        exercice4()
    elif choix == "5":
        exercice5()
    elif choix == "6":
        exercice6()
    elif choix == "7":
        exercice7()
    elif choix == "8":
        exercice8()
    elif choix == "9":
        exercice9()
    elif choix == "10":
        exercice10()
    elif choix == "11":
        exercice11()
    
    
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":
    main()