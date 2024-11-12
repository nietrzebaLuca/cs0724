#include <stdio.h>


// ATTENZIONE le funzioni prodotto e media hanno l'approssimazione dei valori float a 2 e a 0 numeri decimali

void prodotto(float a, float b){
	float p = a * b;
	printf("prodotto:\t%.2f + %.2f = %.2f\n", a, b, p);
}

void media(float a, float b){
	float p = (a+b)/2;
	printf("media:\t(%.0f + %.0f)/2 = %.2f\n", a, b, p);
}

int main(){
	float n, m;
	int k;

	printf("inserire due numeri interi: \n");
	scanf("%f", &n);
	scanf("%f", &m);
	printf("\nvalori acquisiti!!\n");
	
	printf("\nscegli tra: \n 1)moltiplicazione;\n 2)media aritmetica;\n 3)moltiplicazione e media aritmetica;\n");
	scanf("%d", &k);
	
	switch(k){
		case 1:
			prodotto(n, m);
			break;
		case 2:
			media(n, m);
			break;
		case 3:
			prodotto(n, m);
			media(n, m);
			break;
		default:
			printf("scegliere tra 1, 2, 3 !!!\n");
	}
	
	return 0;
}



