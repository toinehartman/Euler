#include <stdio.h>
#include "Functions.h"

int main(void) {
	long int n = 600851475143, f = largest_factor(n);
	printf("%li\n", f);
	return 0;
}
