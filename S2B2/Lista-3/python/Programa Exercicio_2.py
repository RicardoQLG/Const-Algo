num = 0;
b1  = 0;
b2  = 0;
b3  = 0;
b4  = 0;

while (num >= 0):
	print("Digite um numero acima de 0 para ser registrado. (-1 para encerrar)");
	num = input();
	num = int(num);

	if (num >=0 and num <=25):
		b1 = b1 + 1;

	if (num >=26 and num <=50):
		b2 = b2 + 1;

	if (num >=51 and num <=75):
		b3 = b3 + 1;

	if (num >=76 and num <=100):
		b4 = b4 + 1;

print ("São " + str(b1) + " numeros entre 0 e 25");
print ("São " + str(b2) + " numeros entre 26 e 50");
print ("São " + str(b3) + " numeros entre 51 e 75");
print ("São " + str(b4) + " numeros entre 76 e 100");