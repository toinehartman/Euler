#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

bool isPrime(int num) {
	int i;
	bool p = true;
	if (num <= 1) {
		return false;
	}
	for (i = 2; i <= sqrt(num); ++i) {
		if (num % i == 0) {
			p = false;
			break;
		}
		else {
			p = true;
		}
	}
	return p;
}

int div_count(int num) {
	int n, c = 0;

	for (n = 1; n <= sqrt(num) ; n++) {
		if (num % n == 0) {
			c += 2;
			/* printf("%d\n%d\n", n, num / n); */
		}
	}
	return c;
}

int largest_factor(long int num) {
	int d;
	bool finished = false;

	if (isPrime(num))
		return num;
	for (d = 1; d < sqrt(num); d++) {
		if (!finished) {
			while (1) {
				if (isPrime(num)) {
					finished = true;
					return num;
				}
				else if (num % d == 0 && isPrime(d))
					num /= d;
				else
					break;
			}
		}
		else
			break;
	}
	return d;
}

int gcd(int p, int q) {
	int t;

	while (p % q) {
		t = q;
		q = p % q;
		p = t;
	}
	return q;
}

int rec_gcd(int p, int q) {
	if (q == 0)
		return p;
	return rec_gcd(q, p % q);
}

int euc_gcd(int p, int q) {
	while (p != q) {
		if (p > q)
			p -= q;
		else
			q -= p;
	}
	return p;
}

int bit_gcd(int u, int v) {
	if (u == v) return u;
	if (u == 0) return v;
	if (v == 0) return u;
	if (~u & 1) {
		if (v & 1) return bit_gcd(u >> 1, v);
		else return gcd(u >> 1, v >> 1) << 1;
	}
	if (~v & 1) return gcd(u, v >> 1);
	if (u > v) return gcd((u - v) >> 1, v);
	return gcd((v - u) >> 1, u);
}
