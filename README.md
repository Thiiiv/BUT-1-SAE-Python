#include "stdlib.h"
#include "stdio.h"
#include "assert.h"
#include "string.h"

//structure de tableau à deux dimensions, dédié à l'algorithme de Levenshtein
typedef struct {
    int lenS;
    int lenT;
    int * tab;
}
LevArray;

//minimum de deux entiers
int min(int a, int b) {
    return a < b ? a : b;
}

//initialiser un tableau pour des chaînes d'une taille donnée
LevArray init(int lenS, int lenT) {
    LevArray a;
    //on stocke les dimensions
    a.lenS = lenS;
    a.lenT = lenT;
    //allocation d'un tableau (1D) de lenS*lenT entiers
    a.tab = malloc(lenS * lenT * sizeof(int));
    //on vérifie que l'allocation s'est bien passée
    assert(a.tab != NULL); 
    return a;

}

//set: insérer une valeur dans le tableau
void set(LevArray a, int indexS, int indexT, int val) {
    //vérification des indices
    assert(indexS >= 0 && indexS < a.lenS && indexT >= 0 && indexT < a.lenT);
    assert(a.tab!=NULL); 
    a.tab[indexT * a.lenS + indexS] = val;
}

//Q1 get: renvoie la valeur correspondant à des indices donnés
//   i+1 pour les requêtes du type get(a, -1, i) ou get (a, i, -1)
int get(LevArray a, int indexS, int indexT) {
    assert(indexS >= -1 && indexS < a.lenS && indexT >= -1 && indexT < a.lenT);
    assert(a.tab != NULL);
    if (indexT < 0) {
        return indexS+1;
    }
    else if (indexS < 0) {
        return indexT+1;
    }
    return a.tab[indexT * a.lenS + indexS];
}

//Q2 levenshtein: calcule la distance de levenshtein de deux chaînes
int levenshtein(char * S, char * T) {
    lenS = strlen(S);
    lenT = strlen(T);
    int val;
    LevArray a = init(lenS, lenT)
    for (int i = 0; i < lenS; i++) {
        for (int j = 0; j < lenT; j++) {
            int subst;
            if (S[i] == T[j]) {
                subst = get(a, i-1, j-1);
            }
            else {
                subst = get(a, i-1, j-1) + 1;
            }
            int suppr = get(a, i-1, j)+1;
            int ins = get(a, i, j-1)+1;
            
            int val = min(min(suppr, ins), subst);
            
            set(a, i, j, val);
        }
    }
    free(a.tab);
    return val;
}

int main(int argc, char * arv[]) {
    printf("Q1 - get: \n");
    LevArray a = init(3, 3);
    set(a, 1, 1, 42);
    set(a, 1, 2, 99); 
    printf("%d\n", a.tab[1 * a.lenS + 1]);
    printf("get(1,1) = %d\n", get(a, 1, 1));
    printf("get(1,2) = %d\n", get(a, 1, 2));
    printf("get(-1,2) = %d\n", get(a, -1, 2));
    printf("get(-1,-1) = %d\n", get(a, -1, -1));
    free(a.tab);


    printf("Q2 - levenshtein: \n");
    char S[] = "BANANE";
    char T[] = "ANANAS";
    printf("%d\n", strlen(S));
    printf("distance %s-%s : %d \n", S, T, levenshtein(S, T));
    return 0;
}
/* sortie attendue: 

Q1 - get: 
get(1,1) = 42
get(1,2) = 99
get(-1,2) = 3
get(-1,-1) = 0
Q2 - levenshtein: 
distance BANANE-ANANAS : 3 


*/
