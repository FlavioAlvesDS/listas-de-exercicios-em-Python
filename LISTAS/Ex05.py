"""
5) - Desenvolva um programa em python que leia 30 valores inteiros e armazene-os em um vetor. Exiba os valores do vetor
ao contrário da ordem de leitura dos valores.
"""
valor = []

for c in range(1,5):
    valor.append(int(input(f"Informe o {c}º numero : ")))

for c in range(3,-1,-1):
    print(valor[c])
