"""
3) - Faça um algoritmo que receba um número e mostre uma mensagem caso este número
seja maior que 80, menor que 25 ou igual a 40. O usuário deverá informar se deseja
continuar informando os valores.
"""
continuar = True

while(continuar):
    numero = int(input("Informe um numero : "))

    if (numero < 25):
        print("este numero é menor que 25 :")
    elif(numero == 40):
        print(" este numero é igual a 40 :")
    elif(numero > 80):
        print("este numero é maior que 80  :")

    resposta = input("Deseja continuar (s)im (n)ão ?")
    if resposta.upper() == "n":
        continuar = False
