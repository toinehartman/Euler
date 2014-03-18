#include <stdio.h>
#include <stdlib.h>
#include "Functions.h"

int main(int argc, char** argv) {
	printf("%d\n", div_count(atoi(argv[1])));
	return 0;
}
