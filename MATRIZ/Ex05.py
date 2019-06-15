"""
5) - Entrar com valores para uma matriz A [3X4] gere e exiba uma matriz B que é o triplo da matriz A.
"""
vetor = []
matrizA = []
matrizB = []


for l in range(0,3,1):
    for c in range (0,4,1):
        vetor.append(int(input(f"Informe o numero na posição [{l}:{c}] :")))
    matrizA.append(vetor)
    vetor = []


for l in  range(len(matrizA)):
    for c in range(len(matrizA[l])):
        vetor = matrizA[l][c] * 3
    matrizB.append(vetor)
    vetor = []
for l in range(3):
    for c in range(4):
        print(f"{matrizB[l][c]}", end="")
    print()
