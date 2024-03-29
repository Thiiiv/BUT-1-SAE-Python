#-----Imports-----

from upemtk import *
from random import randint
from time import *
from math import sqrt, atan2, acos, pi, cos, sin

#-----Fonctions-----

def etiquette(joueur, tour) :
    '''Fonction pour nommé les cercles'''
    tag = ''
    if joueur == joueur1 :
        tag = 'jp'
        return tag+str(tour)
    elif joueur == joueur2 :
        tag = 'jd'
        return tag+str(tour)
    else :
        tag = 'div_'
        tag1 = 'div_'
        return tag+str(tour), tag1+str(tour+1)


def calc_distance(x, y, lst_x, lst_y, joueur) :
    '''Cette fonction calcule la distance entre 2 centre de cerlces'''
    distance = []
    temp1 = []
    temp2 = []
    indice = 0
    x_proche = 0
    y_proche = 0
        
    for i in range(0, len(lst_x)) :
        if x >= lst_x[i] :
            temp1.append(x - lst_x[i])
        if x < lst_x[i] :
            temp1.append(lst_x[i] - x)
        if y >= lst_y[i] :
            temp2.append(y - lst_y[i])
        if y < lst_y[i] :
            temp2.append(lst_y[i] - y)
    
    if len(temp1) > 0 :
        indice = temp1.index(min(temp1))
        x_proche = lst_x[indice]
        y_proche = lst_y[indice]
        print("x_proche :", x_proche, "| y_proche :", y_proche)

        
    for j in range(0, len(temp1)) :
        distance.append(sqrt(temp2[j]**2 + temp1[j]**2))
    return distance, x_proche, y_proche, indice

def calculer_aire(lst_x,lst_y,lst_rayon, joueur):
    '''pour chaque cercle dun joueur:
    pour chaque pixel contenu dans carré:
        if pixel in cercle:
            liste.append(coord)
    score=len(set(liste))'''
    pass

def intersection(distance, rayon):
    for i in range(len(distance)):
        if distance[i] < rayon * 2:
            return True
    return False

def menu_textuel(x1, y1, x2, y2, chaine='', tag='None') :
    """
    Affiche le texte centré par rapport au rectangle.

    :param float x1: ax du rectange
    :param float x2: bx du rectange
    :param float y1: ay du rectange
    :param float y2: by du rectange
    :param str chaine: chaîne de caractère

    """
    dx = x2-x1
    dy = y2-y1
    ancrage = (dx-longueur_texte(chaine))/2
    milieu_y = (dy-hauteur_texte())/2
    texte(x1+ancrage, y1+milieu_y, chaine, 'black', 'nw', 'Purisa', 24, tag)
    if tag == 'j2':
        texte(x1+ancrage, y1+milieu_y, chaine, joueur2, 'nw', 'Purisa', 24, tag)
    if tag == 'j1':
        texte(x1+ancrage, y1+milieu_y, chaine, joueur1, 'nw', 'Purisa', 24, tag)
    if tag == 'creer':
        texte(x1+ancrage, y1+milieu_y, chaine, joueur2, 'nw', 'Purisa', 24, tag)
    if tag == "budget_j1" :
        texte(x1+ancrage, y1+milieu_y, chaine, joueur1, 'nw', 'Purisa', 24, tag)
    if tag == "budget_j2" :
        texte(x1+ancrage, y1+milieu_y, chaine, joueur2, 'nw', 'Purisa', 24, tag)


def division_boule(x, y, x_proche, y_proche, joueur, tour, tag, indice) :
    dy = y-y_proche
    dx = x-x_proche
    element = 0
    if joueur == joueur1 :
        element = 0
    else :
        element = 1
    #print("dx :", dx, "| dy :", dy, "| indice :", indice, "| tag[indice] :", tag[indice])
    angle = atan2(dy, dx)
    #print("x_proche :", x_proche, "| y_proche :", y_proche, "| x :", x, "| y :", y)
    #print(angle)
    distance = sqrt(dx**2+dy**2)
    if distance < rayon[element] :
        #if x <= x_proche and y <= y_proche :
        new_x = (x - rayon[element] * cos(angle))
        new_y = (y - rayon[element] * sin(angle))

        tag3, tag4 = etiquette('', tour)
        tag.append(tag3)
        tag.append(tag4)
        cercle(x, y, rayon[element]-distance, 'black', joueur, 1, tag3)
        cercle(new_x, new_y, rayon[element]-(rayon[element]-distance), 'black', joueur, 1, tag4)
        lst_x[element].remove(x_proche)
        lst_y[element].remove(y_proche)
        lst_x[element].append(x)
        lst_y[element].append(y)
        lst_x[element].append(new_x)
        lst_y[element].append(new_y)
        lst_rayon[element].append(rayon[element]-distance)
        lst_rayon[element].append(rayon[element]-(rayon[element]-distance))
        print(tag)
        efface(tag[indice])
        print(new_x, new_y) 
    return


def start() :
    """
    Affiche le menu de départ pour lancer le jeu ou le quitter lorsque celui-ci est terminé
    """
    cree_fenetre(largeurFenetre, hauteurFenetre)
    rectangle(0, hauteurFenetre, largeurFenetre, 0, 'orange', 'orange')
    rectangle(5, hauteurFenetre-5, largeurFenetre-5, 5, 'black', 'black')
    x_gauche = 10
    x_droite = largeurFenetre//2 - x_gauche
    y_superieur = 200
    y_inferieur = hauteurFenetre - y_superieur
    rectangle(largeurFenetre*0.75, y_superieur//2, x_droite//2, hauteurFenetre//20, 'orange', 'red', 1, 'Jeux')
    rectangle(x_gauche, y_superieur, x_droite, y_inferieur, 'grey', 'grey', 1, 'jouer')
    rectangle(x_droite+x_gauche, y_superieur, x_droite*2, y_inferieur, 'grey', 'grey', 1, 'quitter')
    rectangle(largeurFenetre*0.75, y_superieur*4.4, x_droite//2, y_superieur*4.6, 'orange', 'red', 1, 'leg')
    cercle(largeurFenetre*0.75, y_superieur//2, 50, 'orange', 'red', 1, 'Jeux1')
    cercle(25*x_gauche, y_superieur//2, 50, 'orange', 'red', 1, 'Jeux2')
    menu_textuel(largeurFenetre*0.75, y_superieur//2, x_droite//2, hauteurFenetre//20, 'Jeux de boules')
    menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Jouer')
    menu_textuel(x_droite+x_gauche, y_superieur, x_droite*2, y_inferieur, 'Quitter')
    menu_textuel(largeurFenetre*0.75, y_superieur//2, x_droite//2, hauteurFenetre//5, 'Créer par Thivakar et Tony', 'creer')
    menu_textuel(largeurFenetre*0.75, y_superieur*4.5, x_droite//2, y_superieur*4.5, 'SAE1-01 & SAE1-02', 'leg1')
    x, y, z = attente_clic()
    print(x, y)
    if x >= x_gauche and x <= x_droite and y >= y_superieur and y <= y_inferieur :
        efface('jouer')
        mise_a_jour()
        rectangle(x_gauche, y_superieur, x_droite, y_inferieur, 'green', 'green', 1, 'jouer')
        menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Jouer')
        mise_a_jour()
        sleep(0.25)
        ferme_fenetre()
        menu_variante(etat_taille, etat_obt)
        ferme_fenetre()
        Jeu(rayon)
    if x >= (x_droite+x_gauche) and x <= x_droite*2 and y >= y_superieur and y <= y_inferieur :
        efface('quitter')
        mise_a_jour()
        rectangle(x_droite+x_gauche, y_superieur, (x_droite*2), y_inferieur, 'red', 'red', 1, 'quitter')
        menu_textuel(x_droite+x_gauche, y_superieur, x_droite*2, y_inferieur, 'Quitter')
        mise_a_jour()
        sleep(0.25)
        ferme_fenetre()
    return

def fin(n):
    """
    Affiche le menu de fin pour dire le gagnant du jeu et quitte.
    """
    cree_fenetre(largeurFenetre, hauteurFenetre)
    rectangle(0, hauteurFenetre, largeurFenetre, 0, 'orange', 'orange')
    rectangle(5, hauteurFenetre-5, largeurFenetre-5, 5, 'black', 'black')
    x_gauche = 10
    x_droite = largeurFenetre//2-x_gauche
    y_superieur = 200
    y_inferieur = hauteurFenetre - y_superieur
    rectangle(largeurFenetre*0.75, y_superieur//2, x_droite//2, hauteurFenetre//20, 'red', 'red', 1, 'Joué')
    rectangle(x_gauche, y_superieur, x_droite, y_inferieur, 'grey', 'grey')
    rectangle(x_droite+x_gauche, y_superieur, (x_droite*2), y_inferieur, 'grey', 'grey')
    cercle(largeurFenetre*0.75, y_superieur//2.5, 50, 'orange', 'red', 1, 'Jeux3')
    cercle(25*x_gauche, y_superieur//2.5, 50, 'orange', 'red', 1, 'Jeux4')
    menu_textuel(largeurFenetre*0.75, y_superieur//2, x_droite//2, hauteurFenetre//20, 'Merci d\'avoir joué !')
    
    if n == 0:
        menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Egalité')
    if n == 1:
        menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Joueur1 a gagné')
    if n == 2:
        menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Joueur2 a gagné')

    menu_textuel(x_droite+x_gauche, y_superieur, x_droite*2, y_inferieur, 'Quitter')
    attente_clic()
    sleep(1)
    ferme_fenetre()



def j1():
    '''Les fonctions j1 et j2 sont des fonctions pour pouvoir attribuer des couleurs froides 
    aléatoirement au joueur1 et des couleurs chaudes aléatoirement au joueur2.'''
    lst_col = ["blue","green","purple"]
    hazard = randint(0, 2) # Randomizer pour les couleurs
    joueur1 = "black"
    if hazard == 0:
        joueur1 = lst_col[0]
    if hazard == 1:
        joueur1 = lst_col[1]
    if hazard == 2:
        joueur1 = lst_col[2]
    return joueur1

def j2():
    lst_col = ["red", "yellow", "orange"]
    hazard = randint(0, 2)
    joueur2 = "black"
    if hazard == 0:
        joueur2 = lst_col[0]
    if hazard == 1:
        joueur2 = lst_col[1]
    if hazard == 2:
        joueur2 = lst_col[2]
    return joueur2



def Jeu(rayon):
    '''La fonction Jeu est le squelette de notre code pour le Jeu des 
    Boules elle réutilise les fonctions précédentes pour pouvoir proposé un jeu fonctionnelle.'''
    cree_fenetre(hauteurFenetre, largeurFenetre)
    rectangle(0, hauteurFenetre, largeurFenetre, 0, 'orange', 'orange')
    rectangle(5, hauteurFenetre-5, largeurFenetre-5, 5, 'black', 'black')
    distance1 = []
    distance2 = []
    distanceO = []
    tag1 = []
    tag2 = []
    x_proche = 0
    xO = 0
    yO = 0
    y_proche = 0
    indice = 0
    indO = 0
    compteur1 = 0
    compteur2 = 0
    obstacles(randint(1, 5)) #variante obstacles
    for i in range(tour) :
        x1, y1, z1 = attente_clic()
        efface('j2')
        efface('budget_j2')
        menu_textuel(75, 20, 75, 20, 'Tour: J1', 'j1')
        menu_textuel(largeurFenetre-150, 20, largeurFenetre-150, 20, "Il vous reste :"+str(budget[1]), 'budget_j1')
        mise_a_jour()
        distance1, x_proche, y_proche, indice = calc_distance(x1, y1, lst_x[1], lst_y[1], joueur1)
        distanceO, xO, yO, indO = calc_distance(x1, y1, obtx, obty, joueur1) #variante obstacles
        print("DistanceO :", distanceO)
        print("distance1 :", distance1)
        print()
        if etat_taille[0] == True :
            rayon[0] = taille_des_boules(1)
        if rayon[0] != 0 :
            if i == 0 and intersection(distanceO, rayon[0]) == False :
                tag1.append(etiquette(joueur1, i))
                cercle(x1, y1, rayon[0], 'black', joueur1, 1, tag1[compteur1])
                compteur1 += 1
                lst_x[0].append(x1)
                lst_y[0].append(y1)
                lst_rayon[0].append(rayon[0])
            else :
                if intersection(distance1, lst_rayon[1][-1]) == False and intersection(distanceO, lst_rayon[0][-1]) == False : 
                    tag1.append(etiquette(joueur1, i))
                    cercle(x1, y1, lst_rayon[0][-1], 'black', joueur1, 1, tag1[compteur1])
                    lst_rayon[0].append(rayon[0])
                    compteur1 += 1
                    lst_x[0].append(x1)
                    lst_y[0].append(y1)
                else :
                    division_boule(x1, y1, x_proche, y_proche, joueur2, tour, tag2, indice)
            efface('budget_j1')
            menu_textuel(largeurFenetre-150, 20, largeurFenetre-150, 20, "Il vous reste :"+str(budget[1]), 'budget_j1')
            mise_a_jour()
        x2, y2, z2 = attente_clic()
        efface('j1')
        efface('budget_j1')
        menu_textuel(75, 20, 75, 20, 'Tour: J2', 'j2')
        menu_textuel(largeurFenetre-150, 20, largeurFenetre-150, 20, "Il vous reste :"+str(budget[2]), 'budget_j2')
        mise_a_jour()
        distance2, x_proche, y_proche, indice = calc_distance(x2, y2, lst_x[0], lst_y[0], joueur2)
        distanceO, xO, yO, indO = calc_distance(x2, y2, obtx, obty, joueur2) #variante obstacles
        print("distance2 :", distance2)
        print()
        if etat_taille[0] == True :
            rayon[1] = taille_des_boules(2)
        if rayon[1] != 0 :
            lst_rayon[1].append(rayon[1])
            if intersection(distance2, rayon[0]) == False and intersection(distanceO, rayon[1]) == False :
                tag2.append(etiquette(joueur2, i))
                cercle(x2, y2, rayon[1], 'black', joueur2, 1, tag2[compteur2])
                lst_rayon[1].append(rayon[1])
                compteur2 += 1
                lst_x[1].append(x2)
                lst_y[1].append(y2)
            else :
                division_boule(x2, y2, x_proche, y_proche, joueur1, tour, tag1, indice)
            efface('budget_j2')
            menu_textuel(largeurFenetre-150, 20, largeurFenetre-150, 20, "Il vous reste :"+str(budget[2]), 'budget_j2')
        mise_a_jour()
    
    attente_clic()
    ferme_fenetre()
    if len(tag1) > len(tag2) :
        fin(1)
    elif len(tag2) > len(tag1) :
        fin(2)
    else :
        fin(0)

#-----Variantes-----

def menu_variante(etat_taille, etat_obt):
    cree_fenetre(largeurFenetre, hauteurFenetre)
    rectangle(0, hauteurFenetre, largeurFenetre, 0, 'orange', 'orange')
    rectangle(5, hauteurFenetre-5, largeurFenetre-5, 5, 'black', 'black')
    x_gauche = 10
    x_droite = largeurFenetre//2 - x_gauche
    y_superieur = 200
    y_inferieur = y_superieur*2
    
    # Boutons options
    rectangle(x_gauche, y_superieur, x_droite, y_inferieur, 'red', 'red', 1, 'taille des boules')
    rectangle(x_gauche, y_inferieur+10, x_droite, y_superieur*3, 'red', 'red', 1, 'obstacles')
    rectangle(x_gauche, (y_superieur*3)+10, x_droite, y_superieur*4, 'grey', 'grey', 1, 'jouer')
    
    
    # Element de design
    rectangle(largeurFenetre*0.75, y_superieur*4.4, x_droite//2, y_superieur*4.6, 'orange', 'red', 1, 'leg')
    rectangle(largeurFenetre*0.75, y_superieur//2, x_droite//2, hauteurFenetre//20, 'orange', 'red', 1, 'Jeux')
    rectangle(largeurFenetre*0.75, y_superieur*4.4, x_droite//2, y_superieur*4.6, 'orange', 'red', 1, 'leg2')
    cercle(largeurFenetre*0.75, y_superieur//2, 50, 'orange', 'red', 1, 'Jeux3')
    cercle(25*x_gauche, y_superieur//2, 50, 'orange', 'red', 1, 'Jeux4')
    
    # Textes options
    menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Taille Boules')
    menu_textuel(x_gauche, y_inferieur+10, x_droite, y_superieur*3, 'Obstacles')
    menu_textuel(x_gauche, (y_superieur*3)+10, x_droite, y_superieur*4, 'Jouer')
    
    # Texte générique
    menu_textuel(largeurFenetre*0.75, y_superieur//2, x_droite//2, hauteurFenetre//20, 'Jeux de boules')
    menu_textuel(largeurFenetre*0.75, y_superieur//2, x_droite//2, hauteurFenetre//5, 'Créer par Thivakar et Tony', 'creer')
    menu_textuel(largeurFenetre*0.75, y_superieur*4.5, x_droite//2, y_superieur*4.5, 'SAE1-01 & SAE1-02', 'leg1')
    
    while True :
        x, y, z = attente_clic()
        if x >= x_gauche and x <= x_droite and y >= y_superieur and y<= y_inferieur :
            efface('taille des boucles')
            mise_a_jour()
            etat_taille[0] = not etat_taille[0]
            if etat_taille[0] == True :
                rectangle(x_gauche, y_superieur, x_droite, y_inferieur, 'green', 'green', 1, 'taille des boules')
            else :
                rectangle(x_gauche, y_superieur, x_droite, y_inferieur, 'red', 'red', 1, 'taille des boules')
            menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Taille Boules')
            mise_a_jour()
        
        if x >= x_gauche and x <= x_droite and y >= y_inferieur+10 and y <= y_superieur*3 :
            efface('obstacles')
            mise_a_jour()
            etat_obt[0] = not etat_obt[0]
            if etat_obt[0] == True :
                rectangle(x_gauche, y_inferieur+10, x_droite, y_superieur*3, 'green', 'green', 1, 'obstacles')
            else :
                rectangle(x_gauche, y_inferieur+10, x_droite, y_superieur*3, 'red', 'red', 1, 'obstacles')
            menu_textuel(x_gauche, y_inferieur+10, x_droite, y_superieur*3, 'Obstacles')
            mise_a_jour()
        
        if x >= x_gauche and x <= x_droite and y >= (y_superieur*3)+10 and y <= y_superieur*4 :
            return

def sablier():
    '''Fonctions pour la variante sablier'''
    t1 = time() + 20 if sablier else None
    while t1 is None or time() < t1:
        ev = donne_evenement() 
        typeEv = type_evenement(ev)

def affichage(temps, couleur):
    efface('timer')
    texte(19*1//20,h//32,f'')

def obstacles(nombre) :
    '''Fonctions pour la variante obstacles'''
    for i in range(nombre) :
        x = randint(50, 1000-50)
        y = randint(50, 1000-50)
        cercle(x, y, 50, 'black', 'grey', 1, "obstacle")
        obtx.append(x)
        obty.append(y)

def taille_des_boules(joueur) :
    """Pour le paramètre joueur, c'est 1 pour le joueur 1 et 2 pour le joueur 2"""
    temp = []
    temp2 = ''   
    fin = 0
    while True :
        temp.append(attente_touche())
        print(temp)
        for i in range(len(temp)) :
            if temp[i] == 'Return' :
                temp.pop(i)
                fin = 1
                break
        if fin == 1 :
            for i in range(len(temp)) :
                if temp[i] != 'Return' :
                    temp2 += str(temp[i])
            rayon = int(temp2)
            break
        
        
    if rayon <= budget[joueur] :   
        budget[joueur] = budget[joueur] - rayon
        return rayon
    else :
        return 0
    

#-----main-----

if __name__ == '__main__':
    joueur1 = j1() # Variables qu'on a besoin de généralisé dans le code
    joueur2 = j2()
    lst_x = [[], []]
    lst_y = [[], []]
    lst_rayon = [[], []]
    obtx = []
    obty = []
    tour = 5
    rayon = [50, 50, 50]
    largeurFenetre = 1000
    hauteurFenetre = 1000
    budget = [0, 200, 200]
    etat_taille = [False]
    etat_obt = [False]
    start()
