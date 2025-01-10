#include <stdio.h>

void _NO_BOF() {

	int vector [10], i, j, k;					//variabili: array 10 interi, intero, intero, intero
	int swap_var;							//variabile intera


	printf ("Inserire 10 interi:\n");

	for ( i = 0 ; i < 10 ; i++)
		{
		int c= i+1;						//vengono acquisiti 10 numeri interi
		printf("[%d]:", c);					//stampa variabile array interi c
		scanf ("%d", &vector[i]);				//input utente variabile intera ed allocazione nel vettore
		}


	printf ("Il vettore inserito e':\n");				// stampa del vettore inserito
	for ( i = 0 ; i < 10 ; i++)					
	        {
	        int t= i+1;						
	        printf("[%d]: %d", t, vector[i]);			// variabili invertite
		printf("\n");
		}


	for (j = 0 ; j < 10 - 1; j++)					// ordinamento array con bubblesort
		{
		for (k = 0 ; k < 10 - j - 1; k++)
			{
				if (vector[k] > vector[k+1])
				{
				swap_var=vector[k];
				vector[k]=vector[k+1];
				vector[k+1]=swap_var;
				}
			}
		}
	printf("Il vettore ordinato e':\n");			// stampa vettore ordinato
	for (j = 0; j < 10; j++)
		{
		int g = j+1;
		printf("[%d]:", g);
		printf("%d\n", vector[j]);
		}
}
