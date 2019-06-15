"""
7) - Desenvolva um programa em python que receba valores númericos informado pelo usuário e cadastre-os em uma lista,
caso a lista já contenha o valorr informado, exbibir a mensagem "Valor já cadastrado".
No final exiba todos os valores cadastrados.
"""
continuar = True
valores = []

while True:
    valor = int(input("Informe uma Valor Para ser Armazenado na Lista :"))
    print("----------------------------------------------------")
    if valor not in valores:
        valores.append(valor)
    else:
        print("----------------------------------------------------")
        print(">"*20,"O Valor informado Ja esta cadastrado","<"*20)
        print("----------------------------------------------------")
    resposta = str(input("Deseja continuar ? [S/N] :"))
    print("----------------------------------------------------")
    if resposta in "Nn":
        break
valores.sort()
print(">"*5," Fim .... ","<"*5)
print("----------------------------------------------------")
print(f"Estes são os valores  armazenados na Lista >>> {valores} ")
print("----------------------------------------------------")