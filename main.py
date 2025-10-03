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

def exercice19():
    ht = int(input("Entrez le prix hors taxe :"))
    print("Prix TTC = ", ht*1.20, "€")

def exercice20():
    prenom = input("Entrez votre prénom :")
    age = int(input("Entrez votre age :"))
    print(prenom, "a", age, "ans")

def exercice21():
    nombre = int(input("Entrez un nombre "))
    if nombre < 0:
        print("Négatif")
    elif nombre == 0:
        print("Nul")
    else:
        print("Positif")

def exercice22():
    age = int(input("Entrez un age :"))
    if age < 18:
        print("Mineur")
    else:
        print("Majeur")

def exercice23():
    note = int(input("Entrez une note :"))
    if note < 10:
        print("Non validé")
    else:
        print("Validé")

def exercice24():
    n1 = int(input("Entrez un premier nombre :"))
    n2 = int(input("Entrez un deuxième nombre :"))
    if n1 > n2:
        print(n1, "est plus grand")
    else:
        print(n2, "est plus grand")

def exercice25():
    n1 = int(input("Entrez un premier nombre :"))
    n2 = int(input("Entrez un deuxième nombre :"))
    if n1 > n2:
        print("Ordre croissant : NON")
    else:
        print("Ordre croissant : OUI")

def exercice26():
    nombre = int(input("Entrez un nombre :"))
    if nombre%5 == 0:
        print("Divisible par 5")
    else:
        print("Non divisible par 5")

def exercice27():
    age = int(input("Entrez un age :"))
    if age < 12:
        print("Enfant")
    elif age >= 18:
        print("Adulte")
    else:
        print("Adolescent")

def exercice28():
    Température = int(input("Entrez une température :"))
    if Température < 0:
        print("Glace")
    elif Température >= 100:
        print("Vapeur")
    else:
        print("Liquide")

def exercice29():
    Note = int(input("Entrez une note :"))
    if Note < 10:
        print("Recalé")
    elif Note >= 10 and Note < 12:
        print("Passable")
    elif Note >= 12 and Note < 16:
        print("Bien")
    else:
        print("Très bien")

def exercice30():
    Limite = int(input("Entrez une valeur :"))
    i = 0
    for i in range(Limite):
        i += 1
        print(i)

def exercice31():
    Depart = int(input("Entrez la valeur de départ :"))
    Depart += 1
    for i in reversed(range(Depart)):
        Depart -= 1
        print(Depart)

def exercice32():
    N = int(input("Entrez une valeur :"))
    S = 0
    for i in range(N):
        S += N
    print(S)

def exercice33():
    N = int(input("Entrez un nombre :"))
    print(N, "x 1 =", N*1, " , ", N, "x 2 =", N*2, " , ", N, "x 3 =", N*3, " , ", N, "x 4 =", N*4, " , ", N, "x 5 =", N*5, " , ", N, "x 6 =", N*6, " , ", N, "x 7 =", N*7, " , ", N, "x 8 =", N*8, " , ", N, "x 9 =", N*9, " , ", N, "x 10 =", N*10,)

def exercice34():
    N = int(input("Entrez une valeur :"))
    for i in range(N):
        if i%2 == 0:
            print(i)

def exercice35():
    N = int(input("Entrez une valeur :"))
    Liste = []
    for i in range(1, N):
        Liste.append(i)
    for i in range(1, N):
        if i**2 in Liste:
            print(i**2)

def exercice36():
    mot = input("Entrez un mot :")
    nombre = int(input("Choisissez combien de fois l'afficher :"))
    for i in range (nombre):
        print(mot)

def exercice37():
    n = int(input("Quelle hauteur souhaitez vous ? :"))
    for i in range(1, n+1):
        print(" " * (n - i) + "*" * (2*i - 1))




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
    if choix == "21":
        exercice21()
    elif choix == "22":
        exercice22()
    elif choix == "23":
        exercice23()
    elif choix == "24":
        exercice24()
    elif choix == "25":
        exercice25()
    elif choix == "26":
        exercice26()
    elif choix == "27":
        exercice27()
    elif choix == "28":
        exercice28()
    elif choix == "29":
        exercice29()
    elif choix == "30":
        exercice30()
    elif choix == "31":
        exercice31()
    elif choix == "32":
        exercice32()
    elif choix == "33":
        exercice33()
    elif choix == "34":
        exercice34()
    elif choix == "35":
        exercice35()
    elif choix == "36":
        exercice36()
    elif choix == "37":
        exercice37()
    elif choix == "38":
        exercice38()
    elif choix == "39":
        exercice39()
    elif choix == "40":
        exercice40()
    elif choix == "41":
        exercice41()
    elif choix == "42":
        exercice42()
    elif choix == "43":
        exercice43()
    elif choix == "44":
        exercice44()
    elif choix == "45":
        exercice45()
    elif choix == "46":
        exercice46()
    elif choix == "47":
        exercice47()
    elif choix == "48":
        exercice48()
    elif choix == "49":
        exercice49()
    elif choix == "50":
        exercice50()
    elif choix == "51":
        exercice51()
    elif choix == "52":
        exercice52()
    elif choix == "53":
        exercice53()
    elif choix == "54":
        exercice54()
    elif choix == "55":
        exercice55()
    elif choix == "56":
        exercice56()
    elif choix == "57":
        exercice57()
    elif choix == "58":
        exercice58()
    elif choix == "59":
        exercice59()
    elif choix == "60":
        exercice60()
    elif choix == "61":
        exercice61()
    elif choix == "62":
        exercice62()
    elif choix == "63":
        exercice63()
    elif choix == "64":
        exercice64()
    elif choix == "65":
        exercice65()
    elif choix == "66":
        exercice66()
    elif choix == "67":
        exercice67()
    elif choix == "68":
        exercice68()
    elif choix == "69":
        exercice69()
    elif choix == "70":
        exercice70()
    elif choix == "71":
        exercice71()
    elif choix == "72":
        exercice72()
    elif choix == "73":
        exercice73()
    elif choix == "74":
        exercice74()
    elif choix == "75":
        exercice75()
    elif choix == "76":
        exercice76()
    elif choix == "77":
        exercice77()
    elif choix == "78":
        exercice78()
    elif choix == "79":
        exercice79()
    elif choix == "80":
        exercice80()
    elif choix == "81":
        exercice81()
    elif choix == "82":
        exercice82()
    elif choix == "83":
        exercice83()
    elif choix == "84":
        exercice84()
    elif choix == "85":
        exercice85()
    elif choix == "86":
        exercice86()
    elif choix == "87":
        exercice87()
    elif choix == "88":
        exercice88()
    elif choix == "89":
        exercice89()
    elif choix == "90":
        exercice90()
    elif choix == "91":
        exercice91()
    elif choix == "92":
        exercice92()
    elif choix == "93":
        exercice93()
    elif choix == "94":
        exercice94()
    elif choix == "95":
        exercice95()
    elif choix == "96":
        exercice96()
    elif choix == "97":
        exercice97()
    elif choix == "98":
        exercice98()
    elif choix == "99":
        exercice99()
    elif choix == "100":
        exercice100()    
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":
    main()