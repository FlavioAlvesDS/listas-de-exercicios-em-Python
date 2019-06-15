"""
15) - [DESAFIO] Desenvolva um procurado em python que leia valores inteiros para um vetor de 20 posições e mostre-o.
Em seguida, troque o primeiro elemento pelo o último, o segundo com o penúltimo, o terceiro com o antepenúltimo e, assim, sucessivamente.
Mostre o novo vetor após todas as trocas.
"""
valores = []
troca = []
inicio = 0
fim = 5

for c in range(5):
    valores.append(int(input(f"Informe o {c+1}º numero : ")))

print(f"Esses foram os informados -> {valores}")

for c in range(2):
    troca.append(valores[inicio])
    valores[inicio] = valores[fim-1]
    valores[fim-1] = troca[c]
    inicio = inicio + 1
    fim = fim - 1

print(f"Esses sao os valores apos a troca de posições -> {valores} ")




