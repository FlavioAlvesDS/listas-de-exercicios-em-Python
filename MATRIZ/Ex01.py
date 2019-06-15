"""
1) - Criar um algoritmo que leia os elementos de uma matriz inteira de 5 X 5 e imprima a matriz (em forma de matriz).
"""
matriz = []
vetor =[]

for l in range (5):
    for c in range (5):
        vetor.append(int(input(f" Informe o {c+1}º numero da {l+1}º coluna : ")))

    print()
    matriz.append(vetor)
    vetor = []

for l in range(5):
    for c in range(5):
        print(f"[{matriz[l][c]:^5}]", end=" ")
