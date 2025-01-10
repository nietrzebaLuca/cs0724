#include <stdio.h>
#include <stdlib.h>

void _BOF(){
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
}
