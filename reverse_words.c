#include <stdio.h>
#include <string.h>
void main()
{
	int n;
	char s[2000];
	char c[2000];
	int len;
	int flag;
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++) {
		gets(s);
		printf("%s\n", s);
		len = strlen(s);
		int j = 0;
		int first = 1;
		flag = 1;
		for (int i = len - 1; i >= 0; i--) {
			if (s[i] != ' ') {
				c[j] = s[i];
				j++;
			}
			else {
				flag = 0;
			}
			if (flag == 0|| i == 0) {
				if (first == 1)
					first = 0;
				else
					printf(" ");
				for (j = j - 1; j >= 0; j--) {
					printf("%c", c[j]);
				}
				flag = 1;
				j = 0;
			}
		}
		printf("\n");
	}
}
