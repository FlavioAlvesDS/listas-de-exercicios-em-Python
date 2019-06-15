x = [10,20,30]
print (x)

x[2]=40

x[2] = x[1]+x[0]

print(x[2])
for valor in x:
    print(valor)

listaVazia = []# criando um alista vazia
listaVazia.append(10)#adcionando o valor 10
listaVazia.append("flavio")#adcionar o nome flavio dentro do proximo indice
print("-----------------------------")
print(listaVazia)

listaVazia.pop()#função para apagar o ultimo indice da lista
print("-----------------------------")
print("esses são os valores dentro da lista apos apagar o ultimo indice",listaVazia)

#para apgar usando o del necessita falar o indice que deseja apagar
del x[1]
print(x)

