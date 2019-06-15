"""
3) - Crie um algoritmo que leia os elementos de uma matriz inteira de 8 X 8 e imprima as seguintes informações:
	a)	A soma dos elementos da matriz;
	b)	A soma dos elementos da matriz cujo seu valor é par;
	c)	A soma dos elementos da matriz cujo seu valor é ímpar;
"""
matriz = []
vetor =[]
soma = 0
somaPar = somaImpar = 0
for l in range (8):
    for c in range (8):
        vetor.append(int(input(f" Informe  elementos da matriz [{l},{c}] : ")))
        soma = soma + vetor[c]
    matriz.append(vetor)
    vetor = []

for l in range(0,8,1):
    for c in range(0,8,1):
        print(f"[{matriz[l][c]:^5}]",end="")
        if matriz[l][c] % 2 == 0:
            somaPar = matriz[l][c] + somaPar
        else:
            somaImpar = matriz[l][c] + somaImpar
    print()
print("=-"*30)
print(f"A soma dos valores armazenados na matriz é = {soma}")
print("=-"*30)
print(f"A soma dos valores Pares na matriz é : {somaPar}")
print("=-"*30)
print(f"A soma dos valores Impares na matriz é : {somaImpar}")
print("=-"*30)