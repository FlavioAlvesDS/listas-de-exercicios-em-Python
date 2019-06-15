"""
7) - 6.	Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos. Mostre como resultado se houve lucro,
prejuízo ou empate para cada produto. Informe média de preço de custo e do preço de venda.
"""
continuar = True
mediaVenda = 0.0
mediaCusto = 0.0
qtProduto = 0

while(continuar):
    valorCusto = float(input("Informe o Valor de Custo do Produto : "))
    valorVenda = float(input("Informe o Valor de Venda do Produto : "))
    mediaCusto = mediaCusto + valorCusto
    mediaVenda = mediaVenda + valorVenda
    qtProduto = qtProduto + 1
    if(valorCusto == valorVenda):
        print("O produto esta sendo vendido Do mesmo preço de custo ")
    elif(valorCusto < valorVenda):
        lucro = valorVenda - valorCusto
        print("----------------------------------------------------------")
        print(f"O produto esta sendo vendido com um Lucro de {lucro} Reais ")
    else:
        preju = valorVenda - valorCusto
        print("----------------------------------------------------------")
        print(f"O produto esta sendo vendido com um Prejuizo de {preju} Reais ")

    if input("Deseja continuar (s)im (n)ão ?").upper() == "N":
        continuar = False
    mediaTotalCusto = mediaCusto / qtProduto
    mediaTotalVenda = mediaVenda / qtProduto
print("----------------------------------------------------------")
print(f"A media dos Preços de Custos é : {mediaTotalCusto} :")
print("----------------------------------------------------------")
print(f"A media dos Preços de Vendas é : {mediaTotalVenda} :")
print("----------------------------------------------------------")
