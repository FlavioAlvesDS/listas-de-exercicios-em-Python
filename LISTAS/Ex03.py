"""
3) - Desenvolva um programa em python que receba 15 valores informados pelo usuário armazene-os em vetor chamdado num,
e imprima uma listagem numerada contendo a seguinte mesnsagem "Par" ou "Ímpar" de acordo com os valores cadastrados no vetor.
"""
num = []

for c in range(1,6):
    num.append(int(input(f"Informe o {c}º numero : ")))

for c in range(len(num)):
    if num[c] % 2 == 0:
        print(f"{c + 1}º numero - {num[c]} é PAR " )
    else:
        print(f"{c + 1}º numero - {num[c]} é IMPAR ")