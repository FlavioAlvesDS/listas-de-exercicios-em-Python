"""
11) Uma Companhia de Seguros possui nove categorias de seguro baseadas na idade e ocupação do segurado.
Somente pessoas com pelo menos 17 anos e não mais de 70 anos podem adquirir apólices de seguro.
Quanto às classes de ocupações, foram definidos três grupos de risco.
A tabela abaixo fornece as categorias em função da faixa etária e do grupo de risco.
Dados nome, idade e grupo de risco, determinar a categoria do pretendente à aquisição de tal seguro.
Imprimir o nome a idade e a categoria do pretendente e caso a idade não esteja na faixa necessária, imprimir uma mensagem.
	GRUPO DE RISCO
	IDADE		BAIXO		MEDIO		ALTO
	17 A 20		1			2			3
	21 A 24		2			3			4
	25 A 34		3			4			5
	35 A 64		4			5			6
	65 A 70		7			8			9

"""

continuar = True

while(continuar):
    nome = input("Informe o nome : ")
    idade = int(input(f"Informe a idade de {nome} : "))
    grupoDeRisco = input(f"Informe o Grupo de risco que {nome} : (Baixo/medio/alto :)")
    if(idade <17 ):
        print("idade invalida")
    elif(idade <=20 ):
        if(grupoDeRisco=="baixo"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 1 ")
        elif(grupoDeRisco=="medio"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 2 ")
        elif(grupoDeRisco=="alto"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 3 ")
        else:
            print("Grupo de risco invalido (baixo|medio|alto)")
    elif(idade <=24 ):
        if(grupoDeRisco=="baixo"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 2 ")
        elif(grupoDeRisco=="medio"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 3 ")
        elif(grupoDeRisco=="alto"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 4 ")
        else:
            print("Grupo de risco invalido (baixo|medio|alto)")
    elif(idade <=34 ):
        if(grupoDeRisco=="baixo"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 3 ")
        elif(grupoDeRisco=="medio"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 4 ")
        elif(grupoDeRisco=="alto"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 5 ")
        else:
            print("Grupo de risco invalido (baixo|medio|alto)")
    elif ( idade <= 64):
        if (grupoDeRisco == "baixo"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 4 ")
        elif (grupoDeRisco == "medio"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 5 ")
        elif (grupoDeRisco == "alto"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 6 ")
        else:
            print("Grupo de risco invalido (baixo|medio|alto)")
    elif (idade <= 70):
        if (grupoDeRisco == "baixo"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 7 ")
        elif (grupoDeRisco == "medio"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 8 ")
        elif (grupoDeRisco == "alto"):
            print(f"Nome: {nome} | Idade: {idade} | Categoria : 9 ")
        else:
            print("Grupo de risco invalido (baixo|medio|alto)")
    else:
        print("A idade informada é invalida , deve ser maior ou igual 17 e menor ou igual 70")
    if input("Deseja continuar (S)im (N)ão :").upper()=="N":
        continuar = False