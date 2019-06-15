L1 = [10,30,40]
L2 = [50,60,25]
print("O valores armazenados em cada lista",L1)
print("O valores armazenados em cada lista",L2)
L3 = L1+L2
print("O valores armazenados na lista apos fazer a concatenação",L3)

#para exibir a lista varias vezes
L5=[10,20,30]
L4 = (L5*2)
print(L4)
#usando o for
for intem in L1:
    print(intem)

#para adicionar um valor dentro de um indice
print(L1)
#apos inserir o valor
L1.insert(1, 100)
print(L1)

#para saber em qual indice estar o valor
x = L1.index(30)
print(x)