"""
6) - A concessionária de veículos “CARANGO VELHO” está vendendo os seus veículos com desconto.
    Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de vários carros.
    O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%.
O sistema deverá perguntar se o usuário deseja continuar calculando desconto até que a resposta seja:
“(N) Não”. Informar total de carros com ano até 2000 e total geral.
"""

continuar = True
desconto = 0.0
valorFinal = 0.0

while (continuar):
    valorCarro = float(input("Informe o Valor do Veiculo :"))
    anoCarro = int(input("Informe o Ano do Veiculo :"))
    if (anoCarro <= 2000):
        desconto = (valorCarro*12)/100
        valorFinal = valorCarro - desconto
        print(f"Com um desconto de R${desconto} reais o valor do veiculo passa a ser de R${valorFinal} reais")
    else:
        desconto = (valorCarro*7)/100
        valorFinal = valorCarro - desconto
        print(f"Com um desconto de R${desconto} reais o valor do veiculo passa a ser de R${valorFinal} reais")
    if input("Deseja continuar (s)im (n)ão ?").upper()=="N":
        continuar = False