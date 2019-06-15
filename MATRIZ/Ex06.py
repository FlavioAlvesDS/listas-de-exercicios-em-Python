"""
6) - Considere uma turma com 10 alunos, cada um com 4 notas. Estes dados são  armazenados em uma matriz 10 x 5, em que a primeira coluna armazena a matrícula do aluno e as 4 últimas armazenam as suas notas. Fazer um algoritmo que:
	a) Leia estes dados, armazenando-os;
	b) Imprima a média de cada aluno;
	c) Imprima a maior média e a matrícula do aluno que a possui;
"""
matriz = []
vetor = []
soma = 0
maiorMedia = 0.0


for l in range(0,10,1):
    print("-" * 30)
    vetor.append(input(f"Informe o nome do {l+1}º Aluno :"))
    print("-" * 30)
    for c in range (0,4,1):
        vetor.append(float(input(f"Informe a {c+1}º nota de {vetor[0]} :")))
        soma = vetor[c+1] + soma

    media = soma/4
    if media > maiorMedia:
        maiorMedia = media
    soma = 0
    vetor.append(media)
    matriz.append(vetor)
    vetor = []


print("-="*15)
for l in range(len(matriz)):
    print("-=" * 25)
    print(f"A  Media  do Aluno {matriz[l][0]}  : {matriz[l][5]}      ")
    print("-="*25)

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if maiorMedia == matriz[l][c]:
            print(f"A maior media foi {maiorMedia} do Aluno {matriz[l][0]}")



