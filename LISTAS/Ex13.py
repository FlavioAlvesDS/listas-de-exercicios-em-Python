"""
13) - Desenvolva um programa em python que leia 15 valores informado pelo usuário e cadastre-os em uma lista.
O usuário deverá infomar um valor a ser procurado no vetor, caso encontre este valor exiba o índice desse elemento.

"""
valores = []
for c in range(1,4):
    valores.append((input("Informe um valor : ")))
consulta = input("Informe um valor para descobrir em qual indice ele esta armazenado :")
if consulta not in valores:
    print()
    print(">>>   O valor informado nao esta armazenado na lista   <<<")
    print()

else:
    posicao = valores.index(consulta)
    print("|------------------------------------------------|")
    print(f"({valores[posicao]}) Esta armazendado no indice :  {posicao} ")
    print()