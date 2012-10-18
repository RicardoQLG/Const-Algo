cand_1 = 0;
cand_2 = 0;
cand_3 = 0;
cand_4 = 0;
branco = 0;
nulo   = 0;
total  = 0;
cont   = 's';

while (cont == 's' or cont == 'sim'):
	total = total + 1;
	print("Digite o numero do seu candidato:\n");
	print("1 - Tiririca\n");
	print("2 - Batoré\n");
	print("3 - Vovó da Fiel\n");
	print("4 - Mulher Pêra\n");
	print("5 - Branco\n");
	print("\n");
	num_voto = input();
	num_voto = int(num_voto);

	if (num_voto == 1):
		cand_1 = cand_1 + 1;
	elif (num_voto == 2):
		cand_2 = cand_2 + 1;
	elif (num_voto == 3):
		cand_3 = cand_3 + 1;
	elif (num_voto == 4):
		cand_4 = cand_4 + 1;
	elif (num_voto == 5):
		branco = branco + 1;
	else:
		nulo = nulo + 1;

	print("Mais algum eleitor para votar? [s/n]");
	cont = input();

print("Apuração dos votos");
print("Votos para o Tiririca: " + str(cand_1) + "\n");
print("Votos para o Batoré: " + str(cand_2) + "\n");
print("Votos para o Vovó da Fiel: " + str(cand_3) + "\n");
print("Votos para o Mulher Pêra: " + str(cand_4) + "\n");
print("\n");
print("Votos nulos:" + str(nulo) + "\n");
print("Votos em branco:" + str(branco) + "\n");
print("\n");
print("A percentagem de votos nulos sobre o total de votos: " + str(nulo * total / 100));
print("A percentagem de votos em branco sobre o total de votos: " + str(branco * total / 100));