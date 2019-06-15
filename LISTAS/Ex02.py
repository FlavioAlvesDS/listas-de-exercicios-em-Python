"""
2) - Desenvolva um programa em python que receba 10 nomes informados pelo usuário e armazene-os em um vetor chamdado nomes.
 No final exiba uma lista numerada com os nomes cadastrados no vetor.
"""
nomes = []

for c in range (1,11):
    nomes.append(input(f"Informe o {c}º nome a ser armazenados :"))
print()
print("="*5,"<< Nomes cadastrados com sucesso >> ","="*5)

for c in range(0,10):
    print(f"{c+1} - {nomes[c]}")
    print("="*30)