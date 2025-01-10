#include <stdio.h>
#include <stdlib.h>
/*
void _BOF() {

    int vector[10], i, j, k;  // Array di 10 interi
    int swap_var;

    printf("Inserire più di 10 numeri per causare un Buffer Overflow (BOF):\n");

    // Modifichiamo il ciclo per permettere all'utente di inserire più di 10 numeri, ovvero 20
    for (i = 0; i < 15; i++) {  
        printf("[%d]:", i + 1);
        scanf("%d", &vector[i]);  // l'overflow avviene qui quando l'utente inserisce più di 10 numeri
    }

    for (j = 0; j < 10 - 1; j++) {
        for (k = 0; k < 10 - j - 1; k++) {
            if (vector[k] > vector[k+1]) {
                swap_var = vector[k];
                vector[k] = vector[k+1];
                vector[k+1] = swap_var;
            }
        }
    }

    printf("Il vettore ordinato e':\n");
    for (j = 0; j < 10; j++) {
        printf("[%d]: %d\n", j + 1, vector[j]);
    }

}
*/


int main(){
	int *vector;
	int i,j,k;
	int swap_var;
	
	vector = (int*)malloc(10 * sizeof(int)); 	// allocazione vettore 
	
	if (vector == NULL){
		printf("errore allocazione\n");
		exit(1);
	}
	printf("Inserire piu di 10 caratteri per un Buffer Overflow\n");
	
	// Loop inserimento dati più lungo == BOF
	for(i=0; i<20; i++){
		printf("[%d]: ", i+1);
		scanf("%d", &vector[i]);
	}
	
	//b errore segmentazione
	free(vector);					// libera la memoria
	vector = NULL;
	vector[0] = 42;					// accesso a memoria gia liberata
	
	// Bubble Sort
	for(j=0; j<10-1; j++){
		for(k=0; k<10-j-i; k++){
			if(vector[k] > vector[k+1]){
				swap_var = vector[k];
				vector[k] = vector[k+1];
				vector[k+1] = swap_var;
			}
		}
	}
	
	printf("Valore ordinato:\n");
	for(j=0; j<10; j++){
		printf("[%d]: %d\n", j+1, vector[j]);
	}
	
	return 0;
}
