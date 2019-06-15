"""
8) - Faça um algoritmo que receba o nome a idade e o sexo de dez funcionário. Para cada funcionário mostre o nome e o salário líquido:
	SEXO	IDADE	SALÁRIO LÍQUIDO
	M		>= 30	R$ 100,00
	M		< 30	R$ 50,00
	F		>= 30	R$ 200,00
	F		< 30	R$ 80,00
"""

continuar = 1

while(continuar <= 10):
    nome = input("Informe o nome do Funcionario : ")
    sexo = input(f"Informe o sexo de {nome} (M)asculino (F)eminino  : ")
    idade = int(input(f"Informe a idade de {nome} : "))


    if (sexo.upper()=="M"):
        if (idade >= 30):
            salarioLiquido = 100.00
        else:
            salarioLiquido = 50.00
    elif (sexo.upper() != "F"):
        print("SEXO INFORMADO NAO É VALIDO")

    else:
        if (idade >= 30):
            salarioLiquido = 200.00
        else:
            salarioLiquido = 80.00

    print(f"{nome} Tem {idade} anos de idade recebe um salario liguido de R${salarioLiquido} Reais ")