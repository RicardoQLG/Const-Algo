#include <stdio.h>

main ()
{
	int cand_1, cand_2, cand_3, cand_4, branco, nulo, num_voto, total;
	char cont[1];

	cand_1 = 0;
	cand_2 = 0;
	cand_3 = 0;
	cand_4 = 0;
	branco = 0;
	nulo   = 0;
	total  = 0;
	cont   = 's';

	while (strcomp(cons,'s'))
	{
		total++;
		printf("Digite o número de seu candidato:\n");
		printf("1-Tiririca\n");
		printf("2-Batoré\n");
		printf("3-Vovó da Fiel\n");
		printf("4-Mulher Pêra\n");
		printf("5-Branco\n");
		printf("\n");
		scanf("%i",&num_voto);

		switch (num_voto)
		{
			case 1:
				cand_1 ++;
				break;

			case 2:
				cand_2 ++;
				break;

			case 3:
				cand_3 ++;
				break;

			case 4:
				cand_4 ++;
				break;

			case 5:
				branco ++;
				break;

			else:
				nulo++;
		}

		printf("Mais algum eleitor para votar?\n[s/n]");
		scanf("%s",&cont);
	}

	printf("Apuração dos votos\n");
	printf("Votos para Tiririca:", cand_1,"\n");
	printf("Votos para Batoré:",cand_2,"\n");
	printf("Votos para Vovó da Fiel:",cand_3,"\n");
	printf("Votos para Mulher Pêra:",cand_4,"\n");
	printf("\n");
	printf("Votos nulo:",nulo,"\n");
	printf("Votos em brancos:",branco,"\n");
	printf("\r");
	printf("A percentagem de votos nulos sobre o total de votos: ", nulo * total / 100);
	printf("A percentagem de votos em branco sobre o total de votos: ", branco * total / 100);

	system("Pause");
}