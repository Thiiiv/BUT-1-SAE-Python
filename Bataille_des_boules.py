#-----Imports-----
import string
import os
from upemtk import *
from random import randint
from time import sleep, time, perf_counter
from math import sqrt, atan2, acos, pi, cos, sin

#-----Fonctions-----

def etiquette(joueur, tour, div: bool = False, indice : int = 100000):
    '''Fonction pour nommé les cercles'''
    tag = ''
    if div == False :
        if joueur == joueur1 :
            tag = 'jp'
            return tag+str(tour)
        elif joueur == joueur2 :
            tag = 'jd'
            return tag+str(tour)
    else :
        if joueur == joueur1 :
            tag = 'jp_div'
            tag1 = 'jp_div'
            return tag+str(indice)+"_1", tag1+str(indice)+"_2"
        elif joueur == joueur2 :
            tag = 'jd_div'
            tag1 = 'jd_div'
            return tag+str(indice)+"_1", tag1+str(indice)+"_2"


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
        #print("x_proche :", x_proche, "| y_proche :", y_proche)

        
    for j in range(0, len(temp1)) :
        distance.append(sqrt(temp2[j]**2 + temp1[j]**2))
    return distance, x_proche, y_proche, indice

def calculer_aire(lst_x, lst_y, lst_rayon, joueur):
    lst_pi = []
    #print("lst_rayon", lst_rayon)
    
    for c in range(len(lst_x)):
        #print("lst_x :", lst_x)
        #print("lst_y", lst_y)
        #print("lst_rayon", lst_rayon)
        for i in range(int(lst_x[c] - lst_rayon[joueur][c]), int(lst_x[c] + lst_rayon[joueur][c])):# lst_rayon[c] au lieu de rayon
            for j in range(int(lst_y[c] - lst_rayon[joueur][c]), int(lst_y[c] + lst_rayon[joueur][c])):
                if sqrt((i - lst_x[c])**2 + (j - lst_y[c])**2) <= lst_rayon[joueur][c]:
                    lst_pi.append((i, j))
    score = len(set(lst_pi))
    return score

def intersection(distance, rayon):
    if type(rayon) != list :
        for i in range(len(distance)):
            if distance[i] < rayon * 2:
                return True
    else :
        for i in range(len(distance)):
            if distance[i] < rayon[i] * 2:
                return True
    return False

def menu_textuel(x1, y1, x2, y2, chaine='', tag='None', couleur : str = 'black') :
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
    texte(x1+ancrage, y1+milieu_y, chaine, couleur, 'nw', 'Purisa', 24, tag)
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
    if distance < lst_rayon[joueur][indice] :
        #if x <= x_proche and y <= y_proche :
        new_x = (x - lst_rayon[joueur][indice] * cos(angle))
        new_y = (y - lst_rayon[joueur][indice] * sin(angle))

        tag3, tag4 = etiquette(joueur, tour, True, indice)
        cercle(x, y, lst_rayon[joueur][indice]-distance, 'black', joueur, 1, tag3)
        cercle(new_x, new_y, lst_rayon[joueur][indice]-(lst_rayon[joueur][indice]-distance), 'black', joueur, 1, tag4)
        lst_rayon[joueur].append(lst_rayon[joueur][indice]-distance)
        lst_rayon[joueur].append(lst_rayon[joueur][indice]-(lst_rayon[joueur][indice]-distance))
        lst_rayon[joueur].pop(indice)
        lst_x[element].remove(x_proche)
        lst_y[element].remove(y_proche)
        lst_x[element].append(x)
        lst_y[element].append(y)
        lst_x[element].append(new_x)
        lst_y[element].append(new_y)
        efface(tag[indice])
        #print(tag[indice])
        tag.pop(indice)
        tag.append(tag3)
        tag.append(tag4)
        #print(new_x, new_y) 
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
    #print(x, y)
    if x >= x_gauche and x <= x_droite and y >= y_superieur and y <= y_inferieur :
        efface('jouer')
        mise_a_jour()
        rectangle(x_gauche, y_superieur, x_droite, y_inferieur, 'green', 'green', 1, 'jouer')
        menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Jouer')
        mise_a_jour()
        sleep(0.25)
        ferme_fenetre()
        menu_variante(variante, rayon, tour)
        #ferme_fenetre()
        #Jeu(rayon, tour)
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
    #print("lst_rayon[joueur1] :", lst_rayon[joueur1])
    #print("lst_rayon[joueur2] :", lst_rayon[joueur2])
    player1 = calculer_aire(lst_x[0], lst_y[0], lst_rayon, joueur1)
    player2 = calculer_aire(lst_x[1], lst_y[1], lst_rayon, joueur2)

    if player1 == player2:
        menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Egalité')
    if player1 > player2:
        menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Joueur1 a gagné')
    if player1 < player2:
        menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Joueur2 a gagné')

    menu_textuel(x_droite+x_gauche, y_superieur, x_droite*2, y_inferieur, 'Quitter')
    attente_clic()
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
    y_proche = 0
    indice = 0
    #compteur1 = 0
    #compteur2 = 0
    i = 0
    if variante['obstacles'] == True :
        for obs in range(randint(2,8)) :
            obstacles() #variante obstacles
        mise_a_jour()
    if bonus['arene1'] == True :
        tempo = bonus_obstacles('arene1.txt')
        obstacles(hauteurFenetre/int(tempo[0]), largeurFenetre/int(tempo[1]), int(tempo[2]), tempo[3], tempo[4], int(tempo[5]), tempo[6])
        obstacles(hauteurFenetre/int(tempo[7]), largeurFenetre/int(tempo[8]), int(tempo[9]), tempo[10], tempo[11], int(tempo[12]), tempo[13])
        obstacles(hauteurFenetre/int(tempo[14]), largeurFenetre/int(tempo[15]), int(tempo[16]), tempo[17], tempo[18], int(tempo[19]), tempo[20])
        obstacles(hauteurFenetre/int(tempo[21])+320, largeurFenetre/int(tempo[22]), int(tempo[23]), tempo[24], tempo[25], int(tempo[26]), tempo[27])
        obstacles(hauteurFenetre/int(tempo[28])+400, largeurFenetre/int(tempo[29]), int(tempo[30]), tempo[31], tempo[32], int(tempo[33]), tempo[34])
    if bonus['arene2'] == True :
        tempo = bonus_obstacles('arene2.txt')
        obstacles(hauteurFenetre/int(tempo[0]), largeurFenetre/int(tempo[1]), int(tempo[2]), tempo[3], tempo[4], int(tempo[5]), tempo[6])
        obstacles(hauteurFenetre/int(tempo[7]), largeurFenetre/int(tempo[8]), int(tempo[9]), tempo[10], tempo[11], int(tempo[12]), tempo[13])
        obstacles(hauteurFenetre/int(tempo[14])+320, largeurFenetre/int(tempo[15]), int(tempo[16]), tempo[17], tempo[18], int(tempo[19]), tempo[20])
        obstacles(hauteurFenetre/int(tempo[21])-200, largeurFenetre/float(tempo[22]), int(tempo[23]), tempo[24], tempo[25], int(tempo[26]), tempo[27])
        obstacles(hauteurFenetre/int(tempo[28])-130, largeurFenetre/float(tempo[29]), int(tempo[30]), tempo[31], tempo[32], int(tempo[33]), tempo[34])
        obstacles(hauteurFenetre/int(tempo[35])-50, largeurFenetre/float(tempo[36]), int(tempo[37]), tempo[38], tempo[39], int(tempo[40]), tempo[41])
        obstacles(hauteurFenetre/int(tempo[42])+50, largeurFenetre/float(tempo[43]), int(tempo[44]), tempo[45], tempo[46], int(tempo[47]), tempo[48])
        obstacles(hauteurFenetre/int(tempo[49])+130, largeurFenetre/float(tempo[50]), int(tempo[51]), tempo[52], tempo[53], int(tempo[54]), tempo[55])
        obstacles(hauteurFenetre/int(tempo[56])+200, largeurFenetre/float(tempo[57]), int(tempo[58]), tempo[59], tempo[60], int(tempo[61]), tempo[62])
    if bonus['arene3'] == True :
        tempo = bonus_obstacles('arene3.txt')
        obstacles(hauteurFenetre/int(tempo[0]), largeurFenetre/int(tempo[1]), int(tempo[2]), tempo[3], tempo[4], int(tempo[5]), tempo[6])
        obstacles(hauteurFenetre/int(tempo[7]), largeurFenetre/int(tempo[8]), int(tempo[9]), tempo[10], tempo[11], int(tempo[12]), tempo[13])
        obstacles(hauteurFenetre/int(tempo[14])+320, largeurFenetre/int(tempo[15]), int(tempo[16]), tempo[17], tempo[18], int(tempo[19]), tempo[20])
        obstacles(hauteurFenetre/int(tempo[21])-200, largeurFenetre/float(tempo[22]), int(tempo[23]), tempo[24], tempo[25], int(tempo[26]), tempo[27])
        obstacles(hauteurFenetre/int(tempo[28])-130, largeurFenetre/float(tempo[29]), int(tempo[30]), tempo[31], tempo[32], int(tempo[33]), tempo[34])
        obstacles(hauteurFenetre/int(tempo[35])-50, largeurFenetre/float(tempo[36]), int(tempo[37]), tempo[38], tempo[39], int(tempo[40]), tempo[41])
        obstacles(hauteurFenetre/int(tempo[42])+50, largeurFenetre/float(tempo[43]), int(tempo[44]), tempo[45], tempo[46], int(tempo[47]), tempo[48])
        obstacles(hauteurFenetre/int(tempo[49])+130, largeurFenetre/float(tempo[50]), int(tempo[51]), tempo[52], tempo[53], int(tempo[54]), tempo[55])
        obstacles(hauteurFenetre/int(tempo[56])+200, largeurFenetre/float(tempo[57]), int(tempo[58]), tempo[59], tempo[60], int(tempo[61]), tempo[62])
    etat_terminaison = False
    while i < tour:
        menu_textuel(75, 15, 75, 15, 'Tour: J1', 'j1', joueur1)  
        efface('j2')
        efface('tour')
        menu_textuel(largeurFenetre//2, 15, largeurFenetre//2, 15, 'Nombre de tours restants : '+str(tour-i-1), 'tour', joueur1)
        if variante['terminaison'] == True or variante['score'] == True or variante['sablier'] == True :
            if variante['sablier'] == True :
                evenement = sablier(5, joueur1)
                if evenement == None :
                    evenement = ('', '', 'Touche')
            else :
                evenement = attente_clic_ou_touche()
            #print(evenement)
            if evenement[2] == 'Touche':
                if evenement[1] == 't':
                    if etat_terminaison == False :
                        i = terminaison(tour,i)
                        etat_terminaison = True
                        i = i-1
                    evenement = attente_clic_ou_touche()
                if evenement[1] == 's':
                    score()
                    i = i-1
                    evenement = attente_clic_ou_touche()
        else :
            evenement = attente_clic_ou_touche()
            print(evenement)
        
        
        if 'Clic' in evenement[2] :
            x1, y1, z1 = evenement
            if variante['taille_des_boules'] == True :
                efface('budget_j2')
                menu_textuel(largeurFenetre-100, 15, largeurFenetre-100, 15, 'Budget : '+str(budget[joueur1]), 'budget_j1', joueur1)
            mise_a_jour()
            #variante obstacles
            #print("DistanceO :", distanceO)
            #print("distance1 :", distance1)
            #print()
            
            """if etat_taille[0] == True :
                rayon[0] = taille_des_boules(1)
                efface('budget_j2')
                menu_textuel(largeurFenetre-55, 15, largeurFenetre-55, 15, 'Il vous reste :'+str(budget[1]), 'budget_j1')
                mise_a_jour()"""
            if variante['taille_des_boules'] == True :
                rayon[joueur1] = taille_des_boules(joueur1)
            if rayon[joueur1] != 0 :
                distance1, x_proche, y_proche, indice = calc_distance(x1, y1, lst_x[1], lst_y[1], joueur1)

                if bonus['arene1'] == True :
                    distanceO = calc_distance(x1, y1, lst_x[2], lst_y[2], joueur1)[0]
                
                if variante['obstacles'] == True or bonus['arene1'] == True or bonus['arene2'] == True or bonus['arene3'] == True :
                    distanceO = calc_distance(x1, y1, lst_x[2], lst_y[2], joueur1)[0] 
                lst_rayon[joueur1].append(rayon[joueur1])
                if variante['obstacles'] == True or bonus['arene1'] == True or bonus['arene2'] == True or bonus['arene3'] == True :
                    if i == 0 and intersection(distanceO, lst_rayon[joueur1][-1]) == False :
                        print('ligne 374 : Passed')
                        tag = etiquette(joueur1, i)
                        tag1.append(tag)
                        cercle(x1, y1, rayon[joueur1], 'black', joueur1, 1, tag)
                        #print(tag)
                        #coordonnees[tag] = set()
                        #coordonnees[tag].add((x1, y1))
                        #compteur1 += 1
                        lst_x[0].append(x1)
                        lst_y[0].append(y1)
                    else :
                        print('ligne 374 : Not Passed')
                        if intersection(distance1, lst_rayon[joueur1][-1]) == False and intersection(distanceO, lst_rayon[joueur1][-1]) == False : 
                            print('ligne 387 : Passed')
                            tag = etiquette(joueur1, i)
                            tag1.append(tag)
                            cercle(x1, y1, lst_rayon[joueur1][-1], 'black', joueur1, 1, tag)
                            #print(tag)
                            #coordonnees[tag] = (x1, y1)
                            #compteur1 += 1
                            lst_x[0].append(x1)
                            lst_y[0].append(y1)
                        else :
                            print('ligne 387 : Not Passed')
                            if len(lst_rayon[joueur1]) > 0 and intersection(distanceO, lst_rayon[joueur1][-1]) != True :
                                print('ligne 399 : Passed')
                                division_boule(x1, y1, x_proche, y_proche, joueur2, tour, tag2, indice)
                                #print("tag2 :", tag2)
                else :
                    if i == 0 and intersection(distanceO, lst_rayon[joueur1][-1]) == False :
                        tag = etiquette(joueur1, i)
                        tag1.append(tag)
                        cercle(x1, y1, rayon[joueur1], 'black', joueur1, 1, tag)
                        #print(tag)
                        #coordonnees[tag] = set()
                        #coordonnees[tag].add((x1, y1))
                        #compteur1 += 1
                        lst_x[0].append(x1)
                        lst_y[0].append(y1)
                    else :
                        if intersection(distance1, lst_rayon[joueur1][-1]) == False : 
                            tag = etiquette(joueur1, i)
                            tag1.append(tag)
                            cercle(x1, y1, lst_rayon[joueur1][-1], 'black', joueur1, 1, tag)
                            #print(tag)
                            #coordonnees[tag] = (x1, y1)
                            #compteur1 += 1
                            lst_x[0].append(x1)
                            lst_y[0].append(y1)
                        else :
                            division_boule(x1, y1, x_proche, y_proche, joueur2, tour, tag2, indice)
                            #print("tag2 :", tag2)
        menu_textuel(75, 15, 75, 15, 'Tour: J2', 'j2', joueur2)
        efface('j1')
        efface('tour')
        menu_textuel(largeurFenetre//2, 15, largeurFenetre//2, 15, 'Nombre de tours restants : '+str(tour-i-1), 'tour', joueur2)
        if variante['terminaison'] == True or variante['score'] == True or variante['sablier'] == True :
            if variante['sablier'] == True :
                efface('temps')
                evenement = sablier(5, joueur2)
                if evenement == None :
                    evenement = ('', '', 'Touche')
            else :
                evenement = attente_clic_ou_touche()
            #print(evenement)
            if evenement[2] == 'Touche':
                if evenement[1] == 't':
                    if etat_terminaison == False :
                        i = terminaison(tour,i)
                        etat_terminaison = True
                        i = i-1
                    evenement = attente_clic_ou_touche()
                if evenement[1] == 's':
                    score()
                    i = i-1
                    evenement = attente_clic_ou_touche()
        else :
            evenement = attente_clic_ou_touche()
        
        if 'Clic' in evenement[2] :
            #print("je suis dans la boucle du j2")
            x2, y2, z2 = evenement
            if variante['taille_des_boules'] == True :
                efface('budget_j1')
                menu_textuel(largeurFenetre-100, 15, largeurFenetre-100, 15, "Budget : "+str(budget[joueur2]), 'budget_j2', joueur2)
            mise_a_jour()
             #variante obstacles
            #print("distance2 :", distance2)
            #print()
            
            """if etat_taille[0] == True :
                rayon[1] = taille_des_boules(2)
                efface('budget_j1')
                menu_textuel(largeurFenetre-55, 15, largeurFenetre-55, 15, "Il vous reste :"+str(budget[2]), 'budget_j2')
                mise_a_jour()"""
            if variante['taille_des_boules'] == True :
                rayon[joueur2] = taille_des_boules(joueur2)
            if rayon[joueur2] != 0 :
                distance2, x_proche, y_proche, indice = calc_distance(x2, y2, lst_x[0], lst_y[0], joueur2)
                if variante['obstacles'] == True or bonus['arene1'] == True or bonus['arene2'] == True or bonus['arene3'] == True :
                    distanceO = calc_distance(x2, y2, lst_x[2], lst_y[2], joueur2)[0]
                lst_rayon[joueur2].append(rayon[joueur2])
                if variante['obstacles'] == True or bonus['arene1'] == True or bonus['arene2'] == True or bonus['arene3'] == True :
                    if intersection(distance2, lst_rayon[joueur2][-1]) == False and intersection(distanceO, lst_rayon[joueur2][-1]) == False :
                        tag = etiquette(joueur2, i)
                        tag2.append(tag)
                        cercle(x2, y2, lst_rayon[joueur2][-1], 'black', joueur2, 1, tag)
                        #print(tag)
                        #coordonnees[tag] = (x2, y2)
                        #compteur2 += 1
                        lst_x[1].append(x2)
                        lst_y[1].append(y2)
                    else :
                        if intersection(distanceO, lst_rayon[joueur2][-1]) != True :
                            division_boule(x2, y2, x_proche, y_proche, joueur1, tour, tag1, indice)
                        #print("tag1 :", tag1)
                else :
                    if intersection(distance2, lst_rayon[joueur2][-1]) == False :
                        tag = etiquette(joueur2, i)
                        tag2.append(tag)
                        cercle(x2, y2, lst_rayon[joueur2][-1], 'black', joueur2, 1, tag)
                        #print(tag)
                        #coordonnees[tag] = (x2, y2)
                        #compteur2 += 1
                        lst_x[1].append(x2)
                        lst_y[1].append(y2)
                    else :
                        if len(lst_rayon[joueur1]) > 0 :
                            division_boule(x2, y2, x_proche, y_proche, joueur1, tour, tag1, indice)
                            #print("tag1 :", tag1)
            mise_a_jour()
        #print("tag1 :", tag1)
        #print("tag2 :", tag2)
        if variante['dynamique'] == True :
            dynamique(lst_x, lst_y, lst_rayon, tag1, tag2)
            mise_a_jour()
        i += 1
    #print(coordonnees)
    attente_clic()
    ferme_fenetre()
    fin()

#-----Variantes-----

def menu_variante(variante, rayon, tour):
    cree_fenetre(largeurFenetre, hauteurFenetre)
    rectangle(0, hauteurFenetre, largeurFenetre, 0, 'orange', 'orange')
    rectangle(5, hauteurFenetre-5, largeurFenetre-5, 5, 'black', 'black')
    x_gauche = 10
    x_droite = largeurFenetre//2 - x_gauche
    y_superieur = 200
    y_inferieur = y_superieur*2
    x_temp = x_droite+x_gauche
    
# Boutons options
    rectangle(x_gauche, y_superieur, x_droite, y_inferieur, str('red' if variante['taille_des_boules'] == False else 'green'), str('red' if variante['taille_des_boules'] == False else 'green'), 1, 'taille des boules')
    rectangle(x_temp, y_inferieur, x_droite*2, y_superieur, str('red' if variante['obstacles'] == False else 'green'), str('red' if variante['obstacles'] == False else 'green'), 1, 'obstacles')
    rectangle(x_gauche, y_inferieur+10, x_droite, y_superieur*3, str('red' if variante['terminaison'] == False else 'green'), str('red' if variante['terminaison'] == False else 'green'), 1, 'terminaison')
    rectangle(x_temp, y_inferieur+10, x_droite*2, y_superieur*3, str('red' if variante['score'] == False else 'green'), str('red' if variante['score'] == False else 'green'), 1, 'score')
    rectangle(x_gauche, y_superieur*3+10, x_droite, y_superieur*4, str('red' if variante['dynamique'] == False else 'green'), str('red' if variante['dynamique'] == False else 'green'), 1, 'dynamique')
    rectangle(x_temp, y_superieur*3+10, x_droite*2, y_superieur*4, str('red' if variante['sablier'] == False else 'green'), str('red' if variante['sablier'] == False else 'green'), 1, 'sablier')
    #rectangle(x_gauche, y_superieur*6+10, x_droite, y_superieur*7, 'grey', 'grey', 1, 'jouer')
    
    
    # Element de design
    rectangle(largeurFenetre*0.75, y_superieur//2, x_droite//2, hauteurFenetre//20, 'orange', 'red', 1, 'Jeux')
    cercle(largeurFenetre*0.75, y_superieur//2, 50, 'orange', 'red', 1, 'Jeux3')
    cercle(25*x_gauche, y_superieur//2, 50, 'orange', 'red', 1, 'Jeux4')
    
    # Textes options
    menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Taille Boules')
    menu_textuel(x_temp, y_inferieur, x_droite*2, y_superieur, 'Obstacles')
    menu_textuel(x_gauche, y_inferieur+10, x_droite, y_superieur*3, 'Terminaison')
    menu_textuel(x_temp, y_inferieur+10, x_droite*2, y_superieur*3, 'Score')
    menu_textuel(x_gauche, y_superieur*3+10, x_droite, y_superieur*4, 'Dynamique')
    menu_textuel(x_temp, y_superieur*3+10, x_droite*2, y_superieur*4, 'Sablier')
    #menu_textuel(x_gauche, y_superieur*6+10, x_droite, y_superieur*7, 'Jouer')

    
    # Texte générique
    menu_textuel(largeurFenetre*0.75, y_superieur//2, x_droite//2, hauteurFenetre//20, 'Variantes')
    menu_textuel(largeurFenetre*0.75, y_superieur//2, x_droite//2, hauteurFenetre//5, 'Créer par Thivakar et Tony', 'creer')
    
    while True :
        x, y, touche = attente_clic_ou_touche()
        if 'Clic' in touche :
            if x >= x_gauche and x <= x_droite and y >= y_superieur and y<= y_inferieur :
                efface('taille des boucles')
                mise_a_jour()
                variante['taille_des_boules'] = not variante['taille_des_boules']
                if variante['taille_des_boules'] == True :
                    rectangle(x_gauche, y_superieur, x_droite, y_inferieur, 'green', 'green', 1, 'taille des boules')
                else :
                    rectangle(x_gauche, y_superieur, x_droite, y_inferieur, 'red', 'red', 1, 'taille des boules')
                menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Taille Boules')
                mise_a_jour()
            
            if x >= x_temp and x <= x_droite*2 and y >= y_superieur and y <= y_inferieur :
                efface('obstacles')
                mise_a_jour()
                variante['obstacles'] = not variante['obstacles']
                if variante['obstacles'] == True :
                    rectangle(x_temp, y_inferieur, x_droite*2, y_superieur, 'green', 'green', 1, 'obstacles')
                else :
                    rectangle(x_temp, y_inferieur, x_droite*2, y_superieur, 'red', 'red', 1, 'obstacles')
                menu_textuel(x_temp, y_inferieur, x_droite*2, y_superieur, 'Obstacles')
                mise_a_jour()
            
            if x >= x_gauche and x <= x_droite and y >= y_inferieur+10 and y <= y_superieur*3 :
                efface('terminaison')
                mise_a_jour()
                variante['terminaison'] = not variante['terminaison']
                if variante['terminaison'] == True :
                    rectangle(x_gauche, y_inferieur+10, x_droite, y_superieur*3, 'green', 'green', 1, 'terminaison')
                else :
                    rectangle(x_gauche, y_inferieur+10, x_droite, y_superieur*3, 'red', 'red', 1, 'terminaison')
                menu_textuel(x_gauche, y_inferieur+10, x_droite, y_superieur*3, 'Terminaison')
                mise_a_jour()

            if x >= x_temp and x <= x_droite*2 and y >= y_inferieur+10 and y <= y_superieur*3 :
                efface('score')
                mise_a_jour()
                variante['score'] = not variante['score']
                if variante['score'] == True :
                    rectangle(x_temp, y_inferieur+10, x_droite*2, y_superieur*3, 'green', 'green', 1, 'score')
                else :
                    rectangle(x_temp, y_inferieur+10, x_droite*2, y_superieur*3, 'red', 'red', 1, 'score')
                menu_textuel(x_temp, y_inferieur+10, x_droite*2, y_superieur*3, 'Score')
                mise_a_jour()

            if x >= x_gauche and x <= x_droite and y >= y_superieur*3+10 and y<= y_superieur*4 :
                efface('dynamique')
                mise_a_jour()
                variante['dynamique'] = not variante['dynamique']
                if variante['dynamique'] == True :
                    rectangle(x_gauche, y_superieur*3+10, x_droite, y_superieur*4, 'green', 'green', 1, 'dynamique')
                else :
                    rectangle(x_gauche, y_superieur*3+10, x_droite, y_superieur*4, 'red', 'red', 1, 'dynamique')
                menu_textuel(x_gauche, y_superieur*3+10, x_droite, y_superieur*4, 'Dynamique')
                mise_a_jour()
            
            if x >= x_temp and x <= x_droite*2 and y >= y_superieur*3+10 and y <= y_superieur*4 :
                efface('sablier')
                mise_a_jour()
                variante['sablier'] = not variante['sablier']
                if variante['sablier'] == True :
                    rectangle(x_temp, y_superieur*3+10, x_droite*2, y_superieur*4, 'green', 'green', 1, 'sablier')
                else :
                    rectangle(x_temp, y_superieur*3+10, x_droite*2, y_superieur*4, 'red', 'red', 1, 'sablier')
                menu_textuel(x_temp, y_superieur*3+10, x_droite*2, y_superieur*4, 'Sablier')
                mise_a_jour()
        else :
            ferme_fenetre()
            menu_bonus(bonus, rayon, tour)

def sablier(secondes, joueur):
    """
    Attend que l'utilisateur clique sur la fenêtre pendant le temps indiqué
    """
    t1=time()+secondes
    typeEv = "RAS"
    while time()<t1 or typeEv != "Touche" or "Clic" not in typeEv :
        ev=donne_evenement()
        typeEv=type_evenement(ev)
        menu_textuel(largeurFenetre/2, 90, largeurFenetre/2, 15, str(t1-time()), 'temps', joueur)
        if time()>= t1 :
            return ('', '', 'Touche')
        if "Clic" in typeEv:
            return clic_x(ev), clic_y(ev), typeEv
        elif typeEv == "Touche":
            return -1, touche(ev), typeEv
        mise_a_jour()
        efface('temps')
    return None

def obstacles(x=None, y=None, r: int=50, couleur: str='grey', remplissage: str='grey', epaisseur: int=1, tag: str='obstacle') :
    '''Fonctions pour la variante obstacles'''
    if x != None and y != None :
        cercle(x, y, r, couleur, remplissage, epaisseur, tag)
    else :
        x = randint(r, largeurFenetre-r)
        y = randint(r, hauteurFenetre-r)
        cercle(x, y, r, couleur, remplissage, epaisseur, tag)
    lst_x[2].append(x)
    lst_y[2].append(y)
    return

def terminaison(tour,i):
    rectangle(0, hauteurFenetre//4, largeurFenetre//2, 0, 'orange', 'orange', tag='term1')
    rectangle(5, hauteurFenetre//4-5, largeurFenetre//2-5, 5, 'black', 'black', tag='term1')
    menu_textuel(0, hauteurFenetre//4-5, largeurFenetre//2-5, 0, 'Fin du jeu dans 5 tours', tag='term1')
    mise_a_jour()
    sleep(2)
    efface('term1')
    i = tour-5
    return i 

def score():
    rectangle(0, hauteurFenetre//4, largeurFenetre//2, 0, 'orange', 'orange', tag='scor')
    rectangle(5, hauteurFenetre//4-5, largeurFenetre//2-5, 5, 'black', 'black', tag='scor')
    menu_textuel(0, hauteurFenetre//6-5, largeurFenetre//2-5, 0, 'Score des joueurs:', tag='scor')
    menu_textuel(0, hauteurFenetre//4-5, largeurFenetre//2-5, 0, calculer_aire(lst_x[0], lst_y[0], lst_rayon, joueur1), tag='scor1')
    menu_textuel(0, hauteurFenetre//3-5, largeurFenetre//2-5, 0, calculer_aire(lst_x[1], lst_y[1], lst_rayon, joueur2), tag='scor2')
    mise_a_jour()
    sleep(2)
    efface('scor')
    efface('scor1')
    efface('scor2')
    return

def taille_des_boules(joueur) :
    rayon = ''
    while True :
        touche = attente_touche()
        if touche in string.digits :
            rayon += touche
        else :
            if len(rayon) > 0 :
                rayon = int(rayon)
            else :
                rayon = budget[joueur]+10
            break
    if budget[joueur]-rayon >= 0 :
        budget[joueur] = budget[joueur]-rayon
        return rayon
    else :
        return 0 
        

def dynamique(lst_x, lst_y, lst_rayon, tag_j1, tag_j2) :
    distance1 = []
    distance2 = []
    distance_obt = []
        
    for i in range(len(tag_j1)) :
        efface(tag_j1[i])
        lst_rayon[joueur1][i] *= 1.04
        distance1 = calc_distance(lst_x[0][i], lst_y[0][i], lst_x[1], lst_y[1], joueur1)[0]
        print(lst_x[2])
        if len(lst_x[2]) > 0 :
            distance_obt = calc_distance(lst_x[0][i], lst_y[0][i], lst_x[2], lst_y[2], joueur1)[0]
            if intersection(distance1, lst_rayon[joueur1][i]) == False and intersection(distance_obt, lst_rayon[joueur1][i]) == False :
                cercle(lst_x[0][i], lst_y[0][i], lst_rayon[joueur1][i], 'black', joueur1, 1, tag_j1[i])
            else :
                cercle(lst_x[0][i], lst_y[0][i], lst_rayon[joueur1][i], 'black', joueur1, 1, tag_j1[i])
        else :
            if intersection(distance1, lst_rayon[joueur1][i]) == False :
                cercle(lst_x[0][i], lst_y[0][i], lst_rayon[joueur1][i], 'black', joueur1, 1, tag_j1[i])
            else :
                cercle(lst_x[0][i], lst_y[0][i], lst_rayon[joueur1][i], 'black', joueur1, 1, tag_j1[i])
        
    for k in range(len(tag_j2)) :
        efface(tag_j2[k])
        lst_rayon[joueur2][k] *= 1.04
        distance2 = calc_distance(lst_x[1][k], lst_y[1][k], lst_x[0], lst_y[0], joueur2)[0]
        print(lst_x[2])
        if len(lst_x[2]) > 0 :
            distance_obt = calc_distance(lst_x[0][k], lst_y[0][k], lst_x[2], lst_y[2], joueur2)[0]
            if intersection(distance2, lst_rayon[joueur2][k]) == False and intersection(distance_obt, lst_rayon[joueur2][k]) == False :
                cercle(lst_x[1][k], lst_y[1][k], lst_rayon[joueur2][k], 'black', joueur2, 1, tag_j2[k])
            else :
                cercle(lst_x[1][k], lst_y[1][k], lst_rayon[joueur2][k], 'black', joueur2, 1, tag_j2[k])
        else :
            if intersection(distance2, lst_rayon[joueur2][k]) == False :
                cercle(lst_x[1][k], lst_y[1][k], lst_rayon[joueur2][k], 'black', joueur2, 1, tag_j2[k])
            else :
                cercle(lst_x[1][k], lst_y[1][k], lst_rayon[joueur2][k], 'black', joueur2, 1, tag_j2[k])
    return

#-----Bonus-----

def bonus_obstacles(fichier):
    with open(fichier) as f:
        return f.read().split()
    
def menu_bonus(bonus, rayon, tour):
    cree_fenetre(largeurFenetre, hauteurFenetre)
    rectangle(0, hauteurFenetre, largeurFenetre, 0, 'orange', 'orange')
    rectangle(5, hauteurFenetre-5, largeurFenetre-5, 5, 'black', 'black')
    x_gauche = 10
    x_droite = largeurFenetre//2 - x_gauche
    y_superieur = 200
    y_inferieur = y_superieur*2
    x_temp = x_droite+x_gauche

# Boutons options
    rectangle(x_gauche, y_superieur, x_droite, y_inferieur, str('red' if bonus['arene1'] == False else 'green'), str('red' if bonus['arene1'] == False else 'green'), 1, 'arene1')
    rectangle(x_temp, y_inferieur, x_droite*2, y_superieur, str('red' if bonus['parametres'] == False else 'green'), str('red' if bonus['parametres'] == False else 'green'), 1, 'parametres')
    rectangle(x_gauche, y_inferieur+10, x_droite, y_superieur*3, str('red' if bonus['arene2'] == False else 'green'), str('red' if bonus['arene2'] == False else 'green'), 1, 'arene2')
    rectangle(x_temp, y_inferieur+10, x_droite*2, y_superieur*3, str('red' if bonus['bonus2'] == False else 'green'), str('red' if bonus['bonus2'] == False else 'green'), 1, 'bonus2')
    rectangle(x_gauche, y_superieur*3+10, x_droite, y_superieur*4, str('red' if bonus['arene3'] == False else 'green'), str('red' if bonus['arene3'] == False else 'green'), 1, 'arene3')
    rectangle(x_temp, y_superieur*3+10, x_droite*2, y_superieur*4, str('red' if bonus['bonus2'] == False else 'green'), str('red' if bonus['bonus2'] == False else 'green'), 1, 'bonus2')
    
    
    # Element de design
    rectangle(largeurFenetre*0.75, y_superieur//2, x_droite//2, hauteurFenetre//20, 'orange', 'red', 1, 'Jeux')
    cercle(largeurFenetre*0.75, y_superieur//2, 50, 'orange', 'red', 1, 'Jeux3')
    cercle(25*x_gauche, y_superieur//2, 50, 'orange', 'red', 1, 'Jeux4')
    
    # Textes options
    menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Arene 1')
    menu_textuel(x_temp, y_inferieur, x_droite*2, y_superieur, 'Paramètres')
    menu_textuel(x_gauche, y_inferieur+10, x_droite, y_superieur*3, 'Arene 2')
    menu_textuel(x_temp, y_inferieur+10, x_droite*2, y_superieur*3, 'Bonus2')
    menu_textuel(x_gauche, y_superieur*3+10, x_droite, y_superieur*4, 'Arene 3')
    menu_textuel(x_temp, y_superieur*3+10, x_droite*2, y_superieur*4, 'Bonus2')

    
    # Texte générique
    menu_textuel(largeurFenetre*0.75, y_superieur//2, x_droite//2, hauteurFenetre//20, 'Bonus')
    menu_textuel(largeurFenetre*0.75, y_superieur//2, x_droite//2, hauteurFenetre//5, 'Créer par Thivakar et Tony', 'creer')
    
    while True :
        x, y, touche = attente_clic_ou_touche()
        if 'Clic' in touche :
            if x >= x_gauche and x <= x_droite and y >= y_superieur and y<= y_inferieur :
                efface('arene1')
                mise_a_jour()
                bonus['arene1'] = not bonus['arene1']
                if bonus['arene1'] == True :
                    rectangle(x_gauche, y_superieur, x_droite, y_inferieur, 'green', 'green', 1, 'arene1')
                else :
                    rectangle(x_gauche, y_superieur, x_droite, y_inferieur, 'red', 'red', 1, 'arene1')
                menu_textuel(x_gauche, y_superieur, x_droite, y_inferieur, 'Arene 1')
                mise_a_jour()
            
            if x >= x_temp and x <= x_droite*2 and y >= y_superieur and y <= y_inferieur :
                efface('parametres')
                mise_a_jour()
                bonus['parametres'] = not bonus['parametres']
                if bonus['parametres'] == True :
                    rectangle(x_temp, y_inferieur, x_droite*2, y_superieur, 'green', 'green', 1, 'parametres')
                else :
                    rectangle(x_temp, y_inferieur, x_droite*2, y_superieur, 'red', 'red', 1, 'parametres')
                menu_textuel(x_temp, y_inferieur, x_droite*2, y_superieur, 'Paramètres')
                mise_a_jour()

            if x >= x_gauche and x <= x_droite and y >= y_inferieur+10 and y <= y_superieur*3 :
                efface('arene2')
                mise_a_jour()
                bonus['arene2'] = not bonus['arene2']
                if bonus['arene2'] == True :
                    rectangle(x_gauche, y_inferieur+10, x_droite, y_superieur*3, 'green', 'green', 1, 'arene2')
                else :
                    rectangle(x_gauche, y_inferieur+10, x_droite, y_superieur*3, 'red', 'red', 1, 'arene2')
                menu_textuel(x_gauche, y_inferieur+10, x_droite, y_superieur*3, 'Arene 2')
                mise_a_jour()

            if x >= x_temp and x <= x_droite*2 and y >= y_inferieur+10 and y <= y_superieur*3 :
                efface('bonus2')
                mise_a_jour()
                bonus['bonus2'] = not bonus['bonus2']
                if bonus['bonus2'] == True :
                    rectangle(x_temp, y_inferieur+10, x_droite*2, y_superieur*3, 'green', 'green', 1, 'bonus2')
                else :
                    rectangle(x_temp, y_inferieur+10, x_droite*2, y_superieur*3, 'red', 'red', 1, 'bonus2')
                menu_textuel(x_temp, y_inferieur+10, x_droite*2, y_superieur*3, 'Bonus2')
                mise_a_jour()

            if x >= x_gauche and x <= x_droite and y >= y_superieur*3+10 and y<= y_superieur*4 :
                efface('arene3')
                mise_a_jour()
                bonus['arene3'] = not bonus['arene3']
                if bonus['arene3'] == True :
                    rectangle(x_gauche, y_superieur*3+10, x_droite, y_superieur*4, 'green', 'green', 1, 'arene3')
                else :
                    rectangle(x_gauche, y_superieur*3+10, x_droite, y_superieur*4, 'red', 'red', 1, 'arene3')
                menu_textuel(x_gauche, y_superieur*3+10, x_droite, y_superieur*4, 'Arene 3')
                mise_a_jour()
            
            if x >= x_temp and x <= x_droite*2 and y >= y_superieur*3+10 and y <= y_superieur*4 :
                efface('bonus2')
                mise_a_jour()
                bonus['bonus2'] = not bonus['bonus2']
                if bonus['bonus2'] == True :
                    rectangle(x_temp, y_superieur*3+10, x_droite*2, y_superieur*4, 'green', 'green', 1, 'bonus2')
                else :
                    rectangle(x_temp, y_superieur*3+10, x_droite*2, y_superieur*4, 'red', 'red', 1, 'bonus2')
                menu_textuel(x_temp, y_superieur*3+10, x_droite*2, y_superieur*4, 'Bonus2')
                mise_a_jour()
        else :
            ferme_fenetre()
            if bonus['parametres'] == True :
                parametres()
            Jeu(rayon, tour)

def parametres(mode: str='lecture') :
    if mode == 'lecture' :
        with open(os.path.join('data', 'config.txt')) as file :
            line = file.read().split()
            print(line)
            global joueur1, joueur2, tour, rayon, largeurFenetre, hauteurFenetre, budget, variante, bonus, lst_rayon 
            joueur1, joueur2 = line[1], line[2]
            lst_rayon = []
            lst_rayon = {joueur1 : [], joueur2 : []}
            if line[3] == 'tour' :
                tour = line[4]
            if line[5] == 'rayon' :
                rayon[joueur1] = int(line[6])
                rayon[joueur2] = int(line[7])
                rayon['obstacle'] = int(line[8])
            if line[9] == 'fenetre' :
                largeurFenetre = int(line[10])
                hauteurFenetre = int(line[11])
            if line[12] == 'budget' :
                budget[joueur1] = int(line[13])
                budget[joueur2] = int(line[14])
            """
            if line[15] == 'variante' :
                variante['taille_des_boules'] = line[16]
                variante['obstacles'] = line[17]
                variante['terminaison'] = line[18]
                variante['score'] = line[19]
                variante['dynamique'] = line[20]
                variante['sablier'] = line[21]
            if line[22] == 'bonus' :
                bonus['arene1'] = line[23]
                bonus['arene2'] = line[24]
                bonus['arene3'] = line[25]
                bonus['bonus2'] = line[26]
                bonus['parametres'] = line[27]"""
    elif mode == 'sauvegarde' :
        with open(os.path.join('data', 'config.txt'), 'w') as file :
            file.write('joueur '+joueur1+' '+joueur2)
            file.write('\n')
            file.write('tour '+str(tour))
            file.write('\n')
            file.write('rayon '+' '.join(rayon.values()))
            file.write('\n')
            file.write('fenetre '+str(largeurFenetre)+' '+str(hauteurFenetre))
            file.write('\n')
            file.write('variante '+' '.join(variante.values()))
            file.write('\n')
            file.write('bonus '+' '.join(bonus.values()))
    return
#-----Main-----

if __name__ == '__main__':
    global joueur1, joueur2, lst_x, lst_y, tour, rayon, largeurFenetre, hauteurFenetre, budget, lst_rayon, variante, bonus
    joueur1 = j1() # Variables qu'on a besoin de généralisé dans le code
    joueur2 = j2()
    lst_x = [[], [], []]
    lst_y = [[], [], []]
    tour = 15
    rayon = {'obstacle' : 50, joueur1 : 50, joueur2 : 50}
    largeurFenetre = 1000
    hauteurFenetre = 1000
    budget = {joueur1 : 500, joueur2 : 500}
    #coordonnees = dict()
    lst_rayon = {joueur1 : [], joueur2 : []}
    variante = {'taille_des_boules' : False, 'obstacles' : False, 'terminaison' : False, 'score' : False, 'dynamique' : False, 'sablier' : False}
    bonus = {'arene1' : False, 'arene2' : False, 'arene3' : False, 'bonus2' : False, 'parametres' : False}
    start(tour)
