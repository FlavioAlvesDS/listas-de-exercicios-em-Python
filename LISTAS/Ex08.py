"""

8) - Desenvolva um programa em python que receba 10 valores númericos e guarde-os em uma lista.
Verifique se os valores cadastrados são pares ou ímpares e cadastre os valores pares em uma nova
lista e os ímpares em outra lista.
No final exbibir o conteúdo das três listas.
"""
valores = []
pares = []
impares = []
cont = 0
for c in range (1,11):
    valores.append(int(input(f"Informe o {c}º numero :")))
for c in valores:
    if c % 2 == 0 :
        pares.append(c)
    else:
        impares.append(c)
print("-="*30)
print(f"Todos os valores Informaos : >> {valores}")
print("-="*30)
print(f"Todos os valores Pares informados : >> {pares}")
print("-="*30)
print(f"Todos os valores Impares Informados : >> {impares}")
print("-="*30)