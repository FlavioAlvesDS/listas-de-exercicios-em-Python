"""
6) - Desenvolva um programa em python que leia valores inteiros e armazene-os em um vetor, calcule e exiba as seguinte informações:
	a) - A quantidade de números pares.
	b) - Os números pares.
	c) - A quantidade de números ímpares.
	d) - Os valores ímpares.
	e) - A média dos valores pares.
	f) - A média dos valores ímpares.
	g) - A média da soma dos valores pares mais os valores ímpares.
"""
valores = []
pares = []
impares = []
continuar = True
par = 0
impar = 0
somaPar = 0
contPar = 0
somaImpar = 0
contImpar = 0


while(continuar):
    valores.append(int(input("Informe um valor, obs: numero 0 não é permitido: ")))
    print("-----------------------------------------------")
    resposta = input("Deseja continuar (S)im ou (N)ão :")
    print("-----------------------------------------------")
    if resposta.upper() == "N":
        continuar = False
    elif resposta.upper() != "S":
        print("-----------------------------------------")
        print(">>>>>>> A resposta não é valida <<<<<<<<")
        print("-----------------------------------------")

        break


for c in valores :

        if (c % 2 == 0):
            pares.append(c)
            par = par + 1
            somaPar = somaPar + c
            contPar = contPar + 1

        else:
            impares.append(c)
            impar = impar + 1
            somaImpar = somaImpar + c
            contImpar = contImpar + 1

print(">>>>>>>>>> Finalizando... <<<<<<<<<<<<")
print()
if par > 0 :
    mediaPar = somaPar / contPar
    print(">>>>>>>>>> Numeros Pares... <<<<<<<<<<<<")
    print("-------------------------------------------------|")
    print(f">>>>>  Numeros Pares informados : {pares}            ")
    print("|------------------------------------------------|")
    print(f">>>>>  A quantidade de valores pares é : {par}       ")
    print("|------------------------------------------------|")
    print(f">>>>>  A media dos numeros Pares é : {mediaPar}      ")
    print("|------------------------------------------------|")
    print()

if impar > 0 :
    mediaImpar = somaImpar/contImpar
    print(">>>>>>>>>> Numeros Impares... <<<<<<<<<<<<")
    print("|------------------------------------------------|")
    print(f">>>>>  A quantidade de valores Impares é : {impar}   ")
    print("|------------------------------------------------|")
    print(f">>>>>  Numeros Impares informados : {impares}        ")
    print("|------------------------------------------------|")
    print(f">>>>>  A media dos numeros impares é : {mediaImpar}  ")
    print("|------------------------------------------------|")

mediatot = (somaPar+somaImpar)/(contPar+contImpar)

print(">>>>> A media total dos valores Pares e Impares é ",mediatot)






