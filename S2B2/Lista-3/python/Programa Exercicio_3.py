cont  = 's';

while (cont == 's'):
	print("Qual o nome do competidor?");
	nome = input();

	print("Qual a nota 1:");
	n1 = input();
	n1 = float(n1);

	maior = n1;
	menor = n1;

	print("Qual a nota 2:");
	n2 = input();
	n2 = float(n2);

	if (n2 > maior):
		maior = n2;

	if (n2 < menor):
		menor = n2;

	print("Qual a nota 3:");
	n3 = input();
	n3 = float(n3);

	if (n3 > maior):
		maior = n3;

	if (n3 < menor):
		menor = n3;

	print("Qual a nota 4:");
	n4 = input();
	n4 = float(n4);

	if (n4 > maior):
		maior = n4;

	if (n4 < menor):
		menor = n4;

	print("Qual a nota 5:");
	n5 = input();
	n5 = float(n1);

	if (n5 > maior):
		maior = n5;

	if (n5 < menor):
		menor = n5;

	print("Qual a nota 6:");
	n6 = input();
	n6 = float(n6);

	if (n6 > maior):
		maior = n6;

	if (n6 < menor):
		menor = n6;

	print("Qual a nota 7:");
	n7 = input();
	n7 = float(n7);

	if (n7 > maior):
		maior = n7;

	if (n7 < menor):
		menor = n7;

	media = (n1 + n2 + n3 + n4 + n5 + n6 + n7 - maior - menor) / 5;

	print ("resultado final:");
	print ("Atleta: " + nome);
	print ("Melhor nota: " + str(maior));
	print ("Pior nota: " + str(menor));
	print ("Média: " + str(media));
	print ("");
	print ("DeSeja avaliar mais um competidor: [s/n]");
	cont = input();
