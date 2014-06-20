#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
	size_t num = 20*19*17*13*11*7*3;
	bool found = false;

	while(!found) {
		found = true;

		for(size_t i = 1; i <= num; ++i) {
			if(num % i != 0)
				found = false;
		}
		num += 20*19*17*13*11*7*3;
	}

	printf("Deelbaar door 1 t/m 20: %zu\n", num - 1);

	return 0;
}
