#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

#include "Functions.h"

int* pfactors(int num) {
	bool finished = false;
	int f[10];
	int c = 0, d;

	for (d = 2; d <= sqrt(num) + 1; d++) {
		if (finished == false) {
			while (1) {
				if (isPrime(num) == true) {
					c++;
					f[c - 1] = num;
					finished = true;
					break;
				}
					else if (num % d == false and isPrime(d) == true) {
						num /= d;
						c++;
						f[c - 1] = d;
				}
				else break;
			}
		}
		else break;
	}
	return f;
}

int rad(int n) {
	int p = 1, a;

	for (a = 0; a < sizeof(struct pfactors(n)), a++) {
		p *= pfactors(n)[a];
	}
	return p;
}

int main(void) {
	int* E[100000];
	int n;

	for (n = 1; n < 100000 + 1; n++) {
		E[n - 1] = {rad(n), n};
	}
	qsort(E, 100000, 2, 0);
	printf("%d\n", E[10000 - 1][1]);
}