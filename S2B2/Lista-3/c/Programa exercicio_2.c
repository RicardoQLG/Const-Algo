#include <stdio.h>

int main(int argc, char const *argv[])
{
	int num, b1, b2, b3, b4;
	num = 0;
	b1 = 0;
	b2 = 0;
	b3 = 0;
	b4 = 0;

	while (num >= 0)
	{
		printf("Digite um numero acima de 0 para ser registrado. (-1 para encerrar)");
		scanf("%i",&num);

		if (num >= 0 && num <= 25)
		{
			b1++;
		}

		if (num > 25 && num <= 50)
		{
			b2++;
		}

		if (num > 50 && num <= 75)
		{
			b3++;
		}

		if (num > 75 && num <= 100)
		{
			b4++;
		}
	}

	printf("São %i numeros entre 0 e 25\n",b1);
	printf("São %i numeros entre 26 e 50\n",b2);
	printf("São %i numeros entre 51 e 75\n",b3);
	printf("São %i numeros entre 76 e 100\n",b4);

	system("PAUSE");
	return 0;
}