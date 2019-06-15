"""
15) - Desenvolva um algoritmo que receba um valor como limite inicial e outro valor como limite final.
      Ao final exibir quantos valores no intervalo informados são pares e ímpares.
"""
impar = 0
par = 0
limiteInicial  = int(input("Informe o limite inical :"))
limiteFinal  = int(input("Informe o limite final :"))
for cont in range(limiteInicial,limiteFinal+1):
    if (cont % 2 == 0) :
        par = par + 1
    else:
        impar = impar + 1

print(f"Foram informados {par} numeros Pares e {impar} numeros impares")