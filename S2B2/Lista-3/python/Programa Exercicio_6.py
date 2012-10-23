total_entrevistados = 0;
idade               = 0;
mulheres            = 0;
total_salarial      = 0;
maior_idade         = 0;
menor_idade         = 1000;

while (idade >= 0):
    print("Digite a idade do entrevistado numero " + str(total_entrevistados + 1) + ':');
    idade = int(input());

    if (idade >= 0):
        print("Digite o sexo[M/F]: ");
        sexo = input();

        print("Digite o salário:");
        salario = float(input());

        total_salarial = total_salarial + salario;

        if (sexo == 'F'):
            mulheres = mulheres + 1;

        if (idade < menor_idade):
            menor_idade = idade;

        if (idade > maior_idade):
            maior_idade = idade;

        total_entrevistados = total_entrevistados + 1;

print ("Média salárial do grupo :", str(total_salarial / total_entrevistados));
print ("Maior idade do grupo:    ", str(maior_idade));
print ("Menor idade do grupo:    ", str(menor_idade));
print ("Mulheres com salário até R$1200,00: " + str(mulheres));
