"""
9) - Desenvolva um programa em python que leia 10 valores númericos informados pelo usuário e armazene-os em um vetor A,
leia mais 10 valores númericos informado pelo usuário armazene-os em outro vetor B, Gere um vetor C, que receberá a soma
 dos elementos do vetor A e B na sua respectiva posição. Ao final exibir os três vetores A, B e C.
"""
listA = []
listB = []
listC = []
print(">"*10,"LISTA 1","<"*10)
for c in range (1,5):
    listA.append(int(input(f"Informe o {c}º VALOR para armazer na Lista A  :")))
print(">"*10,"LISTA 2","<"*10)
for c in range (1,5):
    listB.append(int(input(f"Informe o {c}º VALOR para armazer na Lista B  :")))

for c in range (0,4):
    listC.append(listA[c]+listB[c])

print(listA)
print(" + "*4)
print(listB)
print(" = "*4)
print(listC)
