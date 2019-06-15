"""
19) - Desenvolva um algoritmo que leia 10 valores e ao final exiba a quantidade de valores múltiplo de 5.
"""
mult5 = 0
for cont in range(1,11):
    numero = int(input(f"Informe o {cont}º numero : "))
    print("------------------------------------")
    if numero % 5 == 0 :
        mult5 = mult5 + 1
print(f"Foram informados {mult5} numeros multiplos de 5  ")
print("------------------------------------")
