"""
10) - Desenvolva um programa em python que leia 10 valores inteiros informado pelo usuário. No final exbibir o menor valor cadastrado no vetor.
"""
valores = []
menor = 0


for c in range (0,9):
    valores.append(int(input(f"Informe {c}º numero : ")))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c]< menor:
            menor = valores[c]

print("-="*30)
print(f"Os numeros informados são : {valores}")
print(f"O Menor valor informado foi : {menor}", end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f" >>>> Na posição ... {i}", )
print("-=" * 30)

print(">"*15," Fim ...","<"*15)


