l = []
liste = []
def lister_todos():
    print("A faire ", l)
    print("Fait ", liste)

def creer_todo():
    print('Nom de la tache')
    l.append(input())

def modifier_statut_todo():
    print('Fonctionnalité "modifier le statut d\'un todo" à venir')

    
def supprimer_todo():
    print('Fonctionnalité "supprimer un todo" à venir')

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