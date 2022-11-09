from upemtk import *
from random import randint
from time import *
from math import sqrt, atan2
from decimal import getcontext

def etiquette(joueur, tour) :
    if joueur == joueur1 :
        tag = 'j1_'
    else :
        tag = 'j2_'
    return tag+str(tour)   

def calc_distance(x, y, lst_x, lst_y, joueur) :
    distance = []
    temp = []
    min = 0
    if joueur == joueur1 :
        min = 1
    else :
        min = 0
        
    for i in range(min, len(lst_x), 2) :
        if x >= lst_x[i] and lst_x[i] != 1000**1000 :
            temp.append(x - lst_x[i])
        if x < lst_x[i] and lst_x[i] != 1000**1000 :
            temp.append(lst_x[i] - x)
        if y >= lst_y[i] and lst_y[i] != 1000**1000 :
            temp.append(y - lst_y[i])
        if y < lst_y[i] and lst_y[i] != 1000**1000 :
            temp.append(lst_y[i] - y)
    for j in range(0, len(temp), 2) :
        if j+1 < len(temp) :
            distance.append(sqrt(temp[j]**2+temp[j+1]**2))
    return distance

def intersection(distance, rayon) :
    temp = 1
    for i in range(len(distance)) :
        if distance[i] < rayon*2 :
            temp = 0
            return True
    return False

"""def divison_boule(x, y, lst_x, lst_y, distance, joueur) :
    for i in range(len(distance)) :
        if distance[i] < rayon :
            cercle(x, y, 50-distance[i], 'black', joueur, 1, 'test')
            cercle()
    return
"""
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
    lst_col = ["red","yellow","orange"]
    hazard = randint(0, 2)
    joueur2 = "black"
    if hazard == 0:
        joueur2 = lst_col[0]
    if hazard == 1:
        joueur2 = lst_col[1]
    if hazard == 2:
        joueur2 = lst_col[2]
    return joueur2
    

if __name__ == '__main__':
    cree_fenetre(500, 500)
    
    joueur1 = j1()
    joueur2 = j2()
    tour = 5
    rayon = 50
    lst_x = []
    lst_y = []
    distance1 = []
    distance2 = []
    tag = []
    
    for i in range(tour) :
        x1, y1, z1 = attente_clic()
        lst_x.append(x1)
        lst_y.append(y1)
        tag.append(etiquette(joueur1, i))
        distance1 = calc_distance(x1, y1, lst_x, lst_y, joueur1)
        print("distance1 :", distance1)
        print()
        if i == 0 :
            cercle(x1, y1, rayon, 'black', joueur1, 1, tag[-1])
        else :
            if intersection(distance1, rayon) == False :
                cercle(x1, y1, rayon, 'black', joueur1, 1, tag)
            else :
                #divison_boule(x1, y1, lst_x, lst_y, distance1, joueur2)
                lst_x[-1] = 1000**1000
                lst_y[-1] = 1000**1000
        x2, y2, z2 = attente_clic()
        lst_x.append(x2)
        lst_y.append(y2)
        tag.append(etiquette(joueur2, i))
        distance2 = calc_distance(x2, y2, lst_x, lst_y, joueur2)
        print("distance2 :", distance2)
        print()
        if intersection(distance2, rayon) == False :
            cercle(x2, y2, rayon, 'black', joueur2, 1, tag[-1])
        else :
            lst_x[-1] = 1000**1000
            lst_y[-1] = 1000**1000
        mise_a_jour()
    
    attente_clic()
    ferme_fenetre()
        