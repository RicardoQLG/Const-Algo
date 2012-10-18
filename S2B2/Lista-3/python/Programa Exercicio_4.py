continuar      = 's';
lista_produtos = '';
total          = 0;

prd_0_0 = 'Cachorro Quente ';
prd_1_0 = 'Bauru Simples   ';
prd_2_0 = 'Bauru com Ovo   ';
prd_3_0 = 'X-Burguer       ';
prd_4_0 = 'X-Salada        ';
prd_5_0 = 'Refrigerante    ';
prd_6_0 = 'Suco Natural    ';

prd_0_1 = 3.20;
prd_1_1 = 4.00;
prd_2_1 = 4.50;
prd_3_1 = 5.20;
prd_4_1 = 5.80;
prd_5_1 = 2.50;
prd_6_1 = 3.00;

prd_0_2 = 100;
prd_1_2 = 101;
prd_2_2 = 102;
prd_3_2 = 103;
prd_4_2 = 104;
prd_5_2 = 105;
prd_6_2 = 106;

while (continuar == 's'):
	print("Digite o código do produto:");
	cdg_produto = input();
	cdg_produto = int(cdg_produto);

	print("Digite a quantidade:");
	qtd_produto = input();
	qtd_produto = int(qtd_produto);

	vl_produto = 0;

	if (cdg_produto == prd_0_2):
		vl_produto = qtd_produto * prd_0_1;
		lista_produtos = lista_produtos + str(prd_0_0) + str(prd_0_1) + " " + str(vl_produto) + "\n";

	if (cdg_produto == prd_1_2):
		vl_produto = qtd_produto * prd_1_1;
		lista_produtos = lista_produtos + str(prd_1_0) + str(prd_1_1) + " " + str(vl_produto) + "\n";
		
	if (cdg_produto == prd_2_2):
		vl_produto = qtd_produto * prd_2_1;
		lista_produtos = lista_produtos + str(prd_2_0) + str(prd_2_1) + " " + str(vl_produto) + "\n";
		
	if (cdg_produto == prd_3_2):
		vl_produto = qtd_produto * prd_3_1;
		lista_produtos = lista_produtos + str(prd_3_0) + str(prd_3_1) + " " + str(vl_produto) + "\n";

	if (cdg_produto == prd_4_2):
		vl_produto = qtd_produto * prd_4_1;
		lista_produtos = lista_produtos + str(prd_4_0) + str(prd_4_1) + " " + str(vl_produto) + "\n";

	if (cdg_produto == prd_5_2):
		vl_produto = qtd_produto * prd_5_1;
		lista_produtos = lista_produtos + str(prd_5_0) + str(prd_5_1) + " " + str(vl_produto) + "\n";

	if (cdg_produto == prd_6_2):
		vl_produto = qtd_produto * prd_6_1;
		lista_produtos = lista_produtos + str(prd_6_0) + str(prd_6_1) + " " + str(vl_produto) + "\n";


	total = total + vl_produto;
	print("Deseja adicionar mais produtos? [s/n]");
	continuar = input();

print(lista_produtos);
print("---------------------------\n");
print("total               "+str(total));