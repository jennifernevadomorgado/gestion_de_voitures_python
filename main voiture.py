from classe_voiture import voiture

liste = []

def cherche (plaque):
    for v in liste :
        if v.plaque == plaque :
            return v
    return None

while True :
    print ("1. Ajouter")
    print ("2. Assurer")
    print ("3. Resilier")
    print ("4. Afficher une voiture")
    print ("5. Afficher toutes les voitures")
    print ("6. Quitter")

    choix = input("choix :") 

    match choix :
        case "1":
            plaque = input("plaque:")
            marque = input("marque:")
            v = voiture (plaque, marque)
            liste.append (v)

        case "2":
            plaque = input ("plaque:")
            v = cherche (plaque) 
            if v :
                v.assurer ()
            else :
                print ("voiture introuvable") 
        
        case "3":
            plaque = input ("plaque:")
            v = cherche (plaque)
            if v :
                v.resilier ()
            else:
                print ("voiture introuvable")

        case "4":
            plaque = input ("plaque:")
            v = cherche (plaque)
            if v :
                v.afficher()
            else :
                print ("voiture introuvable")

        case "5":
            for v in liste :
                v.afficher ()

        case "6":
            print ("Fin de programme")
            break

        case _:
            print ("choix invalide")


