'''Criar um algoritmo para calcular o salario congforme a qunatidade de horas '''
'''
declarando variaveis
'''
gerente = "gerente"
supervisor = "supervisor"
operador= "operador"
fabrica = "fabrica"
escritorio = "escritorio"
salario = 0

nome = input("Informe o nome do Funcionario : ")
cargo = input('Informe o cargo de '+nome+' : ')
local = input('Informe o local onde '+nome+' trabalha : ')
quantHora = float(input("Informe a quantidade de horas trabalhadas : "))

if cargo == gerente :
    if local == escritorio:
        salario = quantHora * 70.00
    else:
        if local == fabrica:
            salario = quantHora * 80.00
        else:
            print("O local informado é invalido")
else:
    if cargo == supervisor:
        if cargo == escritorio:
            salario = quantHora * 50.00
        else:
            if local == fabrica:
                salario = quantHora * 60.00
            else:
                print("O local informado é invalido")
    else:
        if cargo == operador:
            if local == fabrica:
                salario = quantHora * 40.00
            else:
                print("O local informado é invalido")
        else:
            print("O cargo informado é invalido")
if salario != 0:
    print("O salario de ", nome, " é : ", salario)
