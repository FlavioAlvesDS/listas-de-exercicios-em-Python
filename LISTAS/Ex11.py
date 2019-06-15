"""
11) - Desenvolva um programa em python que leia 10 valores inteiros informado pelo usuário. No final exbibir o Maior valor cadastrado no vetor.
"""
valores = []
maior = 0


for c in range (0,10):
    valores.append(int(input(f"Informe {c}º numero : ")))
    if c == 0:
        maior = valores[c]
    else:
        if valores[c]> maior:
            maior = valores[c]

print("-="*30)
print(f"Os numeros informados são : {valores}")
print("-="*30)
print(f"O Maior valor informado foi : {maior}", end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f" >>>> Na posição ... {i}", )
print("-=" * 30)

print(">"*15," Fim ...","<"*15)


