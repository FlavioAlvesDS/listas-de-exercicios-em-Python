"""
18) - Faça um algoritmo que calcule o valor da conta de luz de 30 pessoas.
Sabe-se que o cálculo da conta de luz segue a tabela abaixo:

Tipo de Cliente		Valor do KW/h
1 (Residência)		R$ 0,60
2 (Comércio)		R$ 0,48
3 (Indústria)		R$ 1,29
"""
gasto = 0.0
for cont in range(3):
    print("1 (Residência)")
    print("2 (Comércio)")
    print("3 (Indústria)")
    cliente = int(input("Informe o numero correspondente ao tipo de cliente conforme a tabela acima :"))
    consumo = int(input("Informe o consumo de KW/h : "))
    print("---------------------------------------")
    if cliente == 1 :
        gasto = consumo * 0.60
        print(f"O seu consumo foi de {consumo} KW/h")
        print(f"Sua conta tera um valor de R$ {gasto} ")
    elif cliente == 2 :
        gasto = consumo * 0.48
        print(f"O seu consumo foi de {consumo} KW/h")
        print(f"Sua conta tera um valor de R$ {gasto} ")
    elif cliente == 3 :
        gasto = consumo * 1.29
        print(f"O seu consumo foi de {consumo} KW/h")
        print(f"Sua conta tera um valor de R$ {gasto}")
    else:
        print("O numero informado é invalido ")
    print("---------------------------------------")