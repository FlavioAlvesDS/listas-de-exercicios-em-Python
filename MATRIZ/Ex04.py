"""

4) - Crie um algoritmo que leia os elementos de uma matriz inteira de 10 X 10 e imprima as seguintes informações:
	a)	A soma dos elementos onde a soma do índice da linha + o índice da coluna for par;
	b)	A soma dos elementos onde a soma do índice da linha + o índice da coluna for ímpar;
	c)	A quantidade de valores pares na matriz;
	d)	A quantidade de valores ímpares na matriz;
"""
vetor = []
matriz = []
par = impar = contImpar = contPar = 0
for l in range(0,10,1):
    for c in range (0,10,1):
        vetor.append(int(input(f"Informe o numero na posição [{l}:{c}] :")))
    matriz.append(vetor)
    vetor = []
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if (l + c)% 2 == 0 :
            par = par + matriz[l][c]
        else:
            impar = impar + matriz[l][c]
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if matriz[l][c] % 2 == 0 :
            contPar = contPar + 1
        else:
            contImpar = contImpar + 1
print("-="*60)
print(f"A soma dos elementos onde a soma do índice da linha + o índice da coluna for Par é : {par}")
print(f"A soma dos elementos onde a soma do índice da linha + o índice da coluna for Impar é : {impar}")
print("-="*60)
print(f"A quantidade de valores pares na matriz é : {contPar}")
print(f"A quantidade de valores impares na matriz é : {contImpar}")
print("-="*25)
