"""
4) - Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número.
"""
continuar = True
negativo = 0
positivo = 0
zero = 0


while(continuar):
    numero = int(input(f"Informe o {contador}º numero : "))

    if(numero < 0 ):
        print("O numero é Positivo")
        negativo = negativo + 1
    elif(numero > 0 ):
        print("O numero é Negativo")
        positivo = positivo + 1
    else:
        print("O numero é Zero")
        zero = zero + 1
    if input("Deseja Continuar (S)im (N)ão ?").upper()=="N":
        continuar = False
print("----------------------------------------------")
print(f"Foram informados {positivo} numeros Positivos")

print(f"Foram informados {negativo} numeros Negativos")

print(f"Foram informados {zero} numeros Zero")
print("----------------------------------------------")