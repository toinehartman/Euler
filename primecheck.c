#include <stdio.h>
#include <stdbool.h>

#include "Functions.h"


int main(void) {

	int n;
	while (1) {
		printf("Potentieel priemgetal:... ");
		scanf("%i", &n);
		if (isPrime(n) == false){
			printf("%i is geen prime.\n", n);
		}
		else {
			printf("%i is een prime.\n", n);
		}
	}
		
}
