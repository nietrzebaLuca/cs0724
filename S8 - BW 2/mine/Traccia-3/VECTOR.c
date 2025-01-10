#include <stdio.h>

void _BOF();
void _NO_BOF();

int main(){
	int scelta;
	do{
		printf("\nScegli:\n1-BOF\n2-!BOF\n3-exit\n");
		scanf("%d", &scelta);
		
		switch(scelta){
			case 1:		_BOF();		break;
			case 2:		_NO_BOF();	break;
			case 3:		printf("exiting\n");	break;
			default:	printf("invalid\n");
		}
	}
	while (scelta != 3);
	return 0;
}
	
