alunos = []
dados = []

for linha in range (1):
    for coluna in range (4):
        if coluna == 0 :
            dados.append(input(f"Informe o nome do aluno {linha+1}º Aluno :"))
        else:
            dados.append(float(input(f"Informe a  {coluna}º nota do aluno :")))
    alunos.append(dados)
    dados = []
soma = 0
media = 0.0
for linha in range (1):

    for coluna in range (4):
        if coluna != 0 :
            soma = soma + alunos[linha][coluna]
    media = soma / 3
    alunos[linha].append(media)
    soma = 0

print(alunos)