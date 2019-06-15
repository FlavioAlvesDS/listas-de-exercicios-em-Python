"""
2) - Desenvolva um algoritmo que leia os elementos de uma matriz inteira de 5 X 5 e imprima a soma dos elementos da matriz.
"""

matriz = []
vetor =[]
soma = 0
for l in range (5):
    for c in range (5):
        vetor.append(int(input(f" Informe o numero da posiçao [{l},{c}] : ")))
        soma = soma + vetor[c]

    matriz.append(vetor)
    vetor = []

for l in range(0,5,1):
    for c in range(0,5,1):
        print(f"[{matriz[l][c]:^5}]",end=" ")
    print()
print(f"A soma dos valores armazenados na matriz é = {soma}")