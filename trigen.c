#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
	int		c = 0, i, j, r;
	FILE	*ifp;

	// scanf("%i", &r);
	if (argc != 2) {
		printf("ERROR: Program takes exactly one argument!\n");
		return 1;
	}
	else {
		ifp = fopen("/Users/Toine/Desktop/c_trigen.txt", "w");
		r = atoi(argv[1]);
		/* printf("r = %d\n", r); */
	}

	/* for (i = 0; i < argc; ++i) {
	 		printf("%d: %s\n", i, argv[i]);
		} */

	for (i = 1; i <= r; ++i) {
		for (j = 1; j <= i; ++j) {
			c = rand() % 100;
			fprintf(ifp, "%02i", c);
			if (j == i && i != r) {
				fprintf(ifp, "\n");
			}
			else if (j != i) {
				fprintf(ifp, " ");
			}
			// c += 1;
			}
		fprintf(ifp, "\n");
		}
	fclose(ifp);
	printf("Aantal rijen: %i\n", r);
	// system("rm ~/Desktop/c_trigen.txt");
	return 0;
	}
