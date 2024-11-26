l = []
liste = []
def lister_todos():
    print("A faire ", l)
    print("Fait ", liste)

def creer_todo():
    print('Nom de la tache')
    l.append(input())

def modifier_statut_todo():
    print("lequel voulez vous modifiez ?")
    print("1 - A faire ", l)
    print("2 - Fait ", liste)
    choice = input()
    match choice:
        case "1":
            print("Entrez le todo a modifier")
            print(l)
            choice = input()
            match choice:
                case "1" : l
            liste.append(choice)
            l.remove(choice)
            print("A faire ", l)
            print("Fait ", liste)
        case "2" :
            print("Entrez le todo a modifier")
            print(liste)
            choice = input()
            match choice:
                case "1" : liste
            l.append(choice)
            liste.remove(choice)
            print("A faire ", l)
            print("Fait ", liste)
            print("erorr")

def supprimer_todo():
    print("lequel voulez vous supprimez ?")
    print("A faire ", l)
    choice = input()
    print("Etes vous sur ?")
    print("1 - Oui")
    print("2 - Non")
    x = int(input())
    if x == 1:
        match choice:
            case "1": l
        liste.remove(choice)
        l.remove(choice)
        print("A faire ", l)
        print("Fait ", liste)

choix = ''
while choix != 'q':
    print('\n==== Menu principal ====')
    print('1: Lister les todos')
    print('2: Créer un todo')
    print('3: Changer le statut d\'un todo')
    print('4: Supprimer un todo')
    print('q: quitter')
    print('========================')
    choix = input('=> Choix : ')
    match choix:
        case '1': lister_todos()
        case '2': creer_todo()
        case '3': modifier_statut_todo()
        case '4': supprimer_todo()
        case 'q': print('Au revoir')
        case _: print('Choix invalide')