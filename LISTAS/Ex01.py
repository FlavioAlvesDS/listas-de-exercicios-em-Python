'''
1) - Desenvolva um programa em python que receba 10 valores informados pelo usuário, armazene-os em um vetor, depois exiba os dados do vetor.
'''

numero = []

for c in range(1,11,1):
    numero.append(int(input(f"Informe o {c}º valor :")))
print(numero)
