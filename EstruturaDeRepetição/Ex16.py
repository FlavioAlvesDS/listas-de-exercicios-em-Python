"""
16) - Dados três valores A, B e C, em que A e B são números reais e C é um caractere,
pede-se para imprimir o resultado da operação de A por B se C for um símbolo de operador aritmético;
 caso contrário deve ser impressa uma mensagem de
operador não definido. Tratar erro de divisão por zero. Repita esse processo cinco vezes.
"""
soma = 0.0
div = 0.0
sub = 0.0
mult = 0.0
for cont in range (1,6):
    valorA = float(input("Informe um Valor para A :"))
    operador = input("Informe um Operador logico :")
    valorB = float(input("Informe um Valor para B :"))

    if operador=="+":
        soma = valorA + valorB
        print(f"{valorA} {operador} {valorB} = {soma}")
        print("---------------------------------------")
    elif operador == "-":
        sub = valorA - valorB
        print(f"{valorA} {operador} {valorB} = {sub}")
        print("---------------------------------------")
    elif operador == "/":
        if (valorA==0)|(valorB==0):
            print("O numero não pode ser dividido por 0 ")
        else:
            div = valorA / valorB
            print(f"{valorA} {operador} {valorB} = {div}")
            print("---------------------------------------")
    elif operador == "*":
        mult= valorA * valorB
        print(f"{valorA} {operador} {valorB} = {mult}")
        print("---------------------------------------")
    else:
        print("operador não definido. ")