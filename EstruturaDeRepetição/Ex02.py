'''
2) - Escrever um algoritmo que leia os dados de “N” pessoas (nome, sexo, idade e saúde) e informe se
está apta ou não para cumprir o serviço militar obrigatório. Informe os totais.
'''


continuar = True
qtApto = 0
qtNapto = 0

while(continuar):

    print("----------------------------------------------------------------")
    nome = input("Informe o Nome do candidato :")
    print("----------------------------------------------------------------")
    sexo = input("Informe o sexo  (m)asculino (f)eminino :")
    print("----------------------------------------------------------------")
    idade = int(input(f"Informe a idade de {nome} : "))
    print("----------------------------------------------------------------")
    saude = input(f"{nome} esta bem de  Saúde (s)im (n)ão ? : ")
    print("----------------------------------------------------------------")

    if(sexo.upper()=="M"):
        if(idade >=18):
            if(saude.upper()=="S"):
                print(f"{nome} esta apto a cumprir o serviço militar, pois cumpriu todas as exigências ")
                qtApto = qtApto + 1
            elif(saude.upper() =="N"):
                print(f"{nome} não esta apto a cumprir o serviço militar, pois não esta bem de saude ")
                qtNapto = qtNapto + 1
            else:
                print("Resposta Invalida espera-se (s) ou (n)");
        else:
            print(f"{nome} não esta apto a cumprir o serviço militar, pois não tem idade suficiente para ingressar no serviço militar ");
            qtNapto = qtNapto + 1

    else:
        print(f"{nome} não esta apto a cumprir o serviço militar, pois so serão convocados pessoas do sexo Masculino ");
        qtNapto = qtNapto + 1
    print("----------------------------------------------------------------")
    resposta = input("Deseja Consultar mais algum candidato (s)im (n)ão ? ")
    print("----------------------------------------------------------------")
    if(resposta.upper()=="N"):
        continuar = False;
    elif(resposta.upper()!= "S"):
        print("----------------------------------------------------------------")
        print("O valor digitado é invalido")
        print("----------------------------------------------------------------")
print(f"{qtApto} Estão aptos a seguir o serviço militar ")
print(f"{qtNapto} Não estão aptos a seguir o serviço militar ")





