#-----Imports-----

from upemtk import *
from random import randint
from time import *
from math import sqrt, atan2, acos, pi, cos, sin
from decimal import getcontext

#-----Fonctions-----

def etiquette(joueur, tour) :
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

'''Cette fonction calcule la distance entre 2 centre de cerlces'''

def calc_distance(x, y, lst_x, lst_y, joueur) :
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

def intersection(distance, rayon):
    for i in range(len(distance)):
        if distance[i] < rayon * 2:
            return True
    return False
    
    
def divison_boule(x, y, x_proche, y_proche, joueur, tour, tag, indice) :
    dy = y-y_proche
    dx = x-x_proche
    print("dx :", dx, "| dy :", dy, "| indice :", indice, "| tag[indice] :", tag[indice])
    angle = atan2(dy, dx)
    print("x_proche :", x_proche, "| y_proche :", y_proche, "| x :", x, "| y :", y)
    print(angle)
    distance = sqrt(dx**2+dy**2)
    if distance < 50 :
        #if x <= x_proche and y <= y_proche :
        new_x = (x - 50 * cos(angle))
        new_y = (y - 50 * sin(angle))

        tag3, tag4 = etiquette('', tour)
        cercle(x, y, 50-distance, 'black', joueur, 1, tag3)
        cercle(new_x, new_y, 50-(50-distance), 'black', joueur, 1, tag4)
        efface(tag[indice])
        print(new_x, new_y) 
    return


'''Les fonctions j1 et j2 sont des fonctions pour pouvoir attribuer des couleurs froides aléatoirement au joueur1 et des couleurs chaudes aléatoirement au joueur2.'''

def j1():
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

def Victoire(distance):
    SommeAireJ1 = 0
    SommeAireJ2 = 0
    res = rayon**2 * pi
    res *= tour
    R = rayon 
    r = rayon 
    d = distance
    d1 = R**2 - r**2 + d**2
    d2 = d - d1 
    AireIntersection = r**2 * acos(d1/r) - d1 * sqrt(r**2 - d1**2) + R**2 * acos(d2/R) - d2 * sqrt(R**2 - d2**2)

'''La fonction Jeu est le squelette de notre code pour le Jeu des Boules elle réutilise les fonctions précédentes pour pouvoir proposé un jeu fonctionnelle.'''

def Jeu(rayon, tour, joueur1, joueur2):
    cree_fenetre(500, 500)
    lst_x1 = []
    lst_y1 = []
    lst_x2 = []
    lst_y2 = []
    distance1 = []
    distance2 = []
    tag1 = []
    tag2 = []
    x_proche = 0
    y_proche = 0
    indice = 0
    compteur1 = 0
    compteur2 = 0
    
    for i in range(tour) :
        x1, y1, z1 = attente_clic()
        distance1, x_proche, y_proche, indice = calc_distance(x1, y1, lst_x2, lst_y2, joueur1)
        print("distance1 :", distance1)
        print()
        if i == 0 :
            tag1.append(etiquette(joueur1, i))
            cercle(x1, y1, rayon, 'black', joueur1, 1, tag1[compteur1])
            compteur1 += 1
            lst_x1.append(x1)
            lst_y1.append(y1)
        else :
            if intersection(distance1, rayon) == False :
                tag1.append(etiquette(joueur1, i))
                cercle(x1, y1, rayon, 'black', joueur1, 1, tag1[compteur1])
                compteur1 += 1
                lst_x1.append(x1)
                lst_y1.append(y1)
            else :
                divison_boule(x1, y1, x_proche, y_proche, joueur2, tour, tag2, indice)
        x2, y2, z2 = attente_clic()
        distance2, x_proche, y_proche, indice = calc_distance(x2, y2, lst_x1, lst_y1, joueur2)
        print("distance2 :", distance2)
        print()
        if intersection(distance2, rayon) == False :
            tag2.append(etiquette(joueur2, i))
            cercle(x2, y2, rayon, 'black', joueur2, 1, tag2[compteur2])
            compteur2 += 1
            lst_x2.append(x2)
            lst_y2.append(y2)
        else :
            divison_boule(x2, y2, x_proche, y_proche, joueur1, tour, tag1, indice)
        mise_a_jour()
    
    attente_clic()
    ferme_fenetre()

#-----main-----

if __name__ == '__main__':
    joueur1 = j1() # Variables qu'on a besoin de généralisé dans le code
    joueur2 = j2()
    tour = 5
    rayon = 50
    Jeu(rayon, tour, joueur1, joueur2)
