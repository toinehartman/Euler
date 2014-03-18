#include <time.h>
#include "Functions.h"

#define LIM		500
#define REPS	100


int main(int argc, char* argv[]) {
	int clock_t, i, j, g, r;
	double av, start, stop;

	/* gcd */
	av = 0;
	for (r = 0; r < REPS; r++) {
		start = clock();
		for (i = 1; i <= LIM; i++) {
			for (j = 1; j <= LIM; j++) {
				g = gcd(i, j);
			}
		}
		stop = clock();
		av += stop - start;
	}

	printf("'gcd'     took %.02f ms\n", av / (1000 * REPS));

	/* rec_gcd */
	av = 0;
	for (r = 0; r < REPS; r++) {
		start = clock();
		for (i = 1; i <= LIM; i++) {
			for (j = 1; j <= LIM; j++) {
				g = rec_gcd(i, j);
			}
		}
		stop = clock();
		av += stop - start;
	}

	printf("'rec_gcd' took %.02f ms\n", av / (1000 * REPS));

	/* euc_gcd */
	av = 0;
	for (r = 0; r < REPS; r++) {
		start = clock();
		for (i = 1; i <= LIM; i++) {
			for (j = 1; j <= LIM; j++) {
				g = euc_gcd(i, j);
			}
		}
		stop = clock();
		av += stop - start;
	}

	printf("'euc_gcd' took %.02f ms\n", av / (1000 * REPS));

	/* bit_gcd */
	av = 0;
	for (r = 0; r < REPS; r++) {
		start = clock();
		for (i = 1; i <= LIM; i++) {
			for (j = 1; j <= LIM; j++) {
				g = bit_gcd(i, j);
			}
		}
		stop = clock();
		av += stop - start;
	}

	printf("'bit_gcd' took %.02f ms\n", av / (1000 * REPS));

	

}
