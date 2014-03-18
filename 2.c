#include <stdio.h>

int main(void) {
	int a = 0, b = 1, s = 0, t;
	while (b <= 4000000) {
		if (b % 2) {
			s += b;
		}
		t = b;
		b = a + b;
		a = t;
	}
	printf("%d\n", s);
	return 0;
}
