"""
17) - A escola “APRENDER” faz o pagamento de seus professores por hora/aula. Faça um algoritmo
que calcule e exiba o salário do professor. Sabe-se que o valor da hora/aula segue a tabela abaixo:
Professor Nível 1 R$12,00 por hora/aula
Professor Nível 2 R$17,00 por hora/aula
Professor Nível 3 R$25,00 por hora/aula
A escola "APRENDER” possui 50 professores.
"""

cont = 0
salario = 0.0

for cont in range(50):
    nome = input("Informe o Nome do professor : ")
    nivel = int(input(f"Informe o numero correspondente ao nivel de {nome} | nivel (1) | nivel (2) | nivel(3) : "))
    qtHoras = int(input(f"Informe quantos horas trabalhadas {nome} tem :"))
    print("---------------------------------------------------------------------------")
    if nivel == 1 :
        salario = qtHoras * 12
        print(f"{nome} Trabalhou {qtHoras} Horas portanto ira receber um salario de R${salario} reais")

    elif nivel == 2:
        salario = qtHoras * 17
        print(f"{nome} Trabalhou {qtHoras} Horas portanto ira receber um salario de R${salario} reais")

    elif nivel == 3 :
        salario = qtHoras * 25
        print(f"{nome} Trabalhou {qtHoras} Horas portanto ira receber um salario de R${salario} reais")
    else:
        print("O numero Informado Para nivel  é invalido")
    print("---------------------------------------------------------------------------")