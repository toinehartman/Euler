#include <stdio.h>

int main(void) {
	int sum = 0, m, n;

	for (m = 1; m <= 333; ++m) {
		// printf("%i\n", m * 3);
		sum += (m * 3);
	}

	for (n = 1; n <= 199; ++n)
		if ((5 * n) % 3 != 0) {
			sum += (n * 5);
			// printf("%i\n", n * 5);
		}
		
	printf("%i\n", sum);
}
