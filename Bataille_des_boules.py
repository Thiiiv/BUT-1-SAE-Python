#-----Imports-----

import string
from upemtk import *
from random import randint
from time import *
from math import pi, sqrt, atan2, acos, cos, sin

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
    '''Cette fonction calcule la distance entre 2 centre de cercles'''
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


def calculer_aire(lst_x, lst_y, lst_rayon, joueur):
    lst_pi = []
    if joueur == joueur1:
        element = 0
    else:
        element = 1
    
    for c in range(len(lst_x[element])):
        for i in range(lst_x[element][c] - rayon[joueur], lst_x[element][c] + rayon[joueur]):# lst_rayon[c] au lieu de rayon
            for j in range(lst_y[element][c] - rayon[joueur], lst_y[element][c] + rayon[joueur]):
                if sqrt((i - lst_x[element][c])**2 + (j - lst_y[element][c])**2) <= rayon[joueur]:
                    lst_pi.append((i, j))
    score = len(set(lst_pi))
    return score

    
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
    if tag == 'j1':
        texte(x1+ancrage, y1+milieu_y, chaine, joueur1, 'nw', 'Purisa', 24, tag)
    if tag == 'j2':
        texte(x1+ancrage, y1+milieu_y, chaine, joueur2, 'nw', 'Purisa', 24, tag)
    if tag == 'creer':
        texte(x1+ancrage, y1+milieu_y, chaine, joueur2, 'nw', 'Purisa', 24, tag)
    if tag == 'term1':
        texte(x1+ancrage, y1+milieu_y, chaine, 'grey', 'nw', 'Purisa', 24, tag)
    if tag == 'scor':
        texte(x1+ancrage, y1+milieu_y, chaine, 'grey', 'nw', 'Purisa', 24, tag)
    if tag == 'scor1':
        texte(x1+ancrage, y1+milieu_y, chaine, joueur1, 'nw', 'Purisa', 24, tag)
    if tag == 'scor2':
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
    if distance < rayon[joueur] :
        #if x <= x_proche and y <= y_proche :
        new_x = (x - rayon[joueur] * cos(angle))
        new_y = (y - rayon[joueur] * sin(angle))

        tag3, tag4 = etiquette('', tour)
        cercle(x, y, rayon[joueur]-distance, 'black', joueur, 1, tag3)
        cercle(new_x, new_y, rayon[joueur]-(rayon[joueur]-distance), 'black', joueur, 1, tag4)
        efface(tag[indice])
        #print(new_x, new_y) 
        tag.pop(indice)
        tag.append(tag3)
        tag.append(tag4)
        '''lst_x[element].pop(x_proche)
        lst_y[element].pop(y_proche)
        lst_x[element].append(x)
        lst_x[element].append(new_x)
        lst_y[element].append(y)
        lst_x[element].append(new_y)'''
    return


def start(tour) :
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
        #menu_variante(etat_taille, etat_obt)
        #ferme_fenetre()
        Jeu(rayon, tour)
    if x >= (x_droite+x_gauche) and x <= x_droite*2 and y >= y_superieur and y <= y_inferieur :
        efface('quitter')
        mise_a_jour()
        rectangle(x_droite+x_gauche, y_superieur, (x_droite*2), y_inferieur, 'red', 'red', 1, 'quitter')
        menu_textuel(x_droite+x_gauche, y_superieur, x_droite*2, y_inferieur, 'Quitter')
        mise_a_jour()
        sleep(0.25)
        ferme_fenetre()
    return


def fin():
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
    player1 = calculer_aire(lst_x, lst_y, [], joueur1)
    player2 = calculer_aire(lst_x, lst_y, [], joueur2)

    if player1 == player2:
        menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Egalité')
    if player1 > player2:
        menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Joueur1 a gagné')
    if player1 < player2:
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


def Jeu(rayon, tour):
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
    i = 0
    obstacles(randint(1, 5)) #variante obstacles
    menu_textuel(75, 15, 75, 15, 'Tour: J1', 'j1')
    mise_a_jour()
    while i < tour:
        
        evenement = attente_clic_ou_touche()
        if evenement[2] == 'Touche':
            if evenement[1] == 't':
                i = terminaison(tour,i)
            if evenement[1] == 's':
                score()

        elif 'Clic' in evenement[2]:
            x1, y1, z1 = evenement
            efface('j1')
            menu_textuel(75, 15, 75, 15, 'Tour: J2', 'j2')
            mise_a_jour()
            distance1, x_proche, y_proche, indice = calc_distance(x1, y1, lst_x[1], lst_y[1], joueur1)
            distanceO, xO, yO, indO = calc_distance(x1, y1, obtx, obty, joueur1) #variante obstacles
            print("DistanceO :", distanceO)
            print("distance1 :", distance1)
            print()
            '''
            if etat_taille[0] == True :
                rayon[0] = taille_des_boules(1)
                efface('budget_j2')
                menu_textuel(largeurFenetre-55, 15, largeurFenetre-55, 15, tIl vous reste :"+str(budget[1]), 'budget_j1')
                mise_a_jour()'''
            if i == 0 and intersection(distanceO, rayon[joueur2]) == False :
                tag1.append(etiquette(joueur1, i))
                cercle(x1, y1, rayon[joueur1], 'black', joueur1, 1, tag1[compteur1])
                compteur1 += 1
                lst_x[0].append(x1)
                lst_y[0].append(y1)
            else :
                if intersection(distance1, rayon[joueur2]) == False and intersection(distanceO, rayon[joueur1]) == False : 
                    tag1.append(etiquette(joueur1, i))
                    cercle(x1, y1, rayon[joueur1], 'black', joueur1, 1, tag1[compteur1])
                    compteur1 += 1
                    lst_x[0].append(x1)
                    lst_y[0].append(y1)
                else :
                    division_boule(x1, y1, x_proche, y_proche, joueur2, tour, tag2, indice)
        
        evenement = attente_clic_ou_touche()
        if evenement[2]=='Touche':
            if evenement[1] == 't':
                i = terminaison(tour,i)
            if evenement[1] == 's':
                score()

        if 'Clic' in evenement[2]:
            x2, y2, z2 = evenement
            efface('j2')
            menu_textuel(75, 15, 75, 15, 'Tour: J1', 'j1')
            mise_a_jour()
            distance2, x_proche, y_proche, indice = calc_distance(x2, y2, lst_x[0], lst_y[0], joueur2)
            distanceO, xO, yO, indO = calc_distance(x2, y2, obtx, obty, joueur2) #variante obstacles
            print("distance2 :", distance2)
            print()
            '''
            if etat_taille[0] == True :
                rayon[1] = taille_des_boules(2)
                efface('budget_j1')
                menu_textuel(largeurFenetre-55, 15, largeurFenetre-55, 15, "Il vous reste :"+str(budget[2]), 'budget_j2')
                mise_a_jour()'''
            if intersection(distance2, rayon[joueur1]) == False and intersection(distanceO, rayon[joueur1]) == False :
                tag2.append(etiquette(joueur2, i))
                cercle(x2, y2, rayon[joueur1], 'black', joueur2, 1, tag2[compteur2])
                compteur2 += 1
                lst_x[1].append(x2)
                lst_y[1].append(y2)
            else :
                division_boule(x2, y2, x_proche, y_proche, joueur1, tour, tag1, indice)
            mise_a_jour()
        i += 1
    
    attente_clic()
    ferme_fenetre()
    fin()

#-----Variantes-----
'''
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
'''
def sablier():
    '''Fonctions pour la variante sablier'''
    t1 = time() + 20 if sablier else None
    while t1 is None or time() < t1:
        ev = donne_evenement() 
        typeEv = type_evenement(ev)
    pass

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

def terminaison(tour,i):
    rectangle(0, hauteurFenetre//4, largeurFenetre//2, 0, 'orange', 'orange', tag='term1')
    rectangle(5, hauteurFenetre//4-5, largeurFenetre//2-5, 5, 'black', 'black', tag='term1')
    menu_textuel(0, hauteurFenetre//4-5, largeurFenetre//2-5, 0, 'Fin du jeu dans 5 tours', tag='term1')
    mise_a_jour()
    sleep(2)
    efface('term1')
    i = tour-5
    return i 

def taille_des_boules(joueur) :
    rayon = ''
    while True :
        touche = attente_touche()
        if int(touche) in string.digits :
            rayon += touche
        else :
            rayon = int(rayon)
            break
    if budget[joueur]-rayon >= 0 :
        budget[joueur] = budget[joueur]-rayon
        return rayon
    else :
        return 0 

def score():
    rectangle(0, hauteurFenetre//4, largeurFenetre//2, 0, 'orange', 'orange', tag='scor')
    rectangle(5, hauteurFenetre//4-5, largeurFenetre//2-5, 5, 'black', 'black', tag='scor')
    menu_textuel(0, hauteurFenetre//6-5, largeurFenetre//2-5, 0, 'Score des joueurs:', tag='scor')
    menu_textuel(0, hauteurFenetre//4-5, largeurFenetre//2-5, 0, calculer_aire(lst_x, lst_y, rayon, joueur1), tag='scor1')
    menu_textuel(0, hauteurFenetre//3-5, largeurFenetre//2-5, 0, calculer_aire(lst_x, lst_y, rayon, joueur2), tag='scor2')
    mise_a_jour()
    sleep(2)
    efface('scor')
    efface('scor1')
    efface('scor2')
    pass

#-----Main-----

if __name__ == '__main__':
    joueur1 = j1() # Variables qu'on a besoin de généralisé dans le code
    joueur2 = j2()
    lst_x = [[], []]
    lst_y = [[], []]
    obtx = []
    obty = []
    tour = 20
    rayon = {'obstacle' : 50, joueur1 : 50, joueur2 : 50}
    lst_rayon = {joueur1 : [], joueur2 : []}
    largeurFenetre = 1000
    hauteurFenetre = 1000
    etat_taille = [False]
    etat_obt = [False]
    budget = {joueur1 : 200, joueur2 : 200}
    start(tour)
