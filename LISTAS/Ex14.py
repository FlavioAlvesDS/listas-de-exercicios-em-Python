"""
14) - Desenvolva um programa em python que leia o nome e uma nota para um aluno, crie duas listas para armazenar estes valores,
      o usuário deverá informar um nome de aluno para a pesquisar, se o aluno existir na lista com os nomes do aluno, exbibir o
       nome e a nota do aluno, caso contrário informar a mesnsagem "Aluno não cadastrado."

"""
aluno = []
nota = []
while True:
    print("|---------------------------------|")
    print("|>>>> Escolha uma das Opçoes <<<<<|")
    print("|_________________________________|")
    print("| 1  - Cadastrar                  | ")
    print("|_________________________________|")
    print("| 2  - Cosulta Cadastro           | ")
    print("|_________________________________|")
    print("| 3  - Encerrar Sistema           | ")
    print("|---------------------------------|")
    print()
    opcao = int(input("Informe a opção desejada :"))
    print()

    if opcao == 1 :
        print("|------------------------------------|")
        print("|>>>>     Cadastradar Aluno      <<<<|")
        print("|------------------------------------|")
        print()
        aluno.append(str(input("Informe o nome do Aluno : ")))
        nota.append(float(input(f"Informe a nota do Aluno : ")))
        print()
        print("|------------------------------------|")
        print("|>>  Aluno Cadastrado com sucesso  <<|")
        print("|------------------------------------|")
        print()
        print()
    elif opcao == 2 :
        if len(aluno)== 0:
            print("|------------------------------------|")
            print(">>>>>>>>  A lista esta Vazia <<<<<<<<")
            print("|------------------------------------|")
        else:
            print("|------------------------------------|")
            print("|>>>>    Consultar Cadastro      <<<<|")
            print("|------------------------------------|")
            print()

            consulta = str(input("Informe o Nome do Aluno que deseja Consultar :"))
            print("|-------------------------------------------------------------|")

            if consulta not in aluno:
                print("O Aluno não esta cadastrado")
            else:
                posicao =  aluno.index(consulta)
                print("|--------------------------|")
                print(f"| Aluno : {aluno[posicao]}")
                print(f"| Nota  : {nota[posicao]}")
                print("|--------------------------|")
                print()
                print()
    if opcao == 3:
        print()
        print(">>>>> FINALIZANDO PROGRAMA ... <<<<<")
        break