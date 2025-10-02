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
    print(nombre1, " + ",nombre2, " = ", nombre1+nombre2)

def exercice6():
    nombre1 = int(input("Entrez un premier nombre :"))
    nombre2 = int(input("Entrez un deuxième nombre :"))
    print(nombre1, " - ",nombre2, " = ", nombre1-nombre2)

def exercice7():
    nombre1 = int(input("Entrez un premier nombre :"))
    nombre2 = int(input("Entrez un deuxième nombre :"))
    print(nombre1, " x ",nombre2, " = ", nombre1*nombre2)

def exercice8():
    nombre1 = int(input("Entrez un premier nombre :"))
    nombre2 = int(input("Entrez un deuxième nombre :"))
    print(nombre1, " ÷ ",nombre2, " = ", nombre1/nombre2)    

def exercice9():
    nombre1 = int(input("Entrez un premier nombre :"))
    nombre2 = int(input("Entrez un deuxième nombre :"))
    print(nombre1, " puissance ",nombre2, " = ", nombre1**nombre2)

def exercice10():
    nombre = int(input("Entrez un nombre : "))
    print("Le double de", nombre, "est", nombre*2)

def exercice11():
    nombre = int(input("Entrez un nombre : "))
    print("La moitié de", nombre, "est", nombre/2)

def exercice12():
    message = (input("Entrez votre message : "))
    print((message + "\n")*5)

def exercice13():
    i = 0
    for i in range(5):
        i+=1
        print(i)

def exercice14():
    i = 0
    for i in range(5):
        i+=1
        r = 2*i
        print("2 x", i, "=", r)

def exercice15():
    cote = int(input("Entrez la longueur d'un côté :"))
    print("Périmètre =", cote*4)

def exercice16():
    cote = int(input("Entrez la longueur d'un côté :"))
    print("Aire =", cote**2)

def exercice17():
    valeur = int(input("Entrez une somme en € à convertir en $ (sans préciser la devise) :"))
    print(valeur, "€ =", valeur*1.1, "$")

def exercice18():
    min = int(input("Entrez une durrée en minute :"))
    print(min, "minutes =", min*60, "secondes")



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
    elif choix == "12":
        exercice12()
    elif choix == "13":
        exercice13()
    elif choix == "14":
        exercice14()
    elif choix == "15":
        exercice15()
    elif choix == "16":
        exercice16()
    elif choix == "17":
        exercice17()
    elif choix == "18":
        exercice18()
    elif choix == "19":
        exercice19()
    elif choix == "20":
        exercice20()

    
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":
    main()