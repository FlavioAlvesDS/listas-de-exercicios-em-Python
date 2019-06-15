continuar = True;

while continuar:
    resposta = input("deseja continuar (S)im (N)ão ?")
    if resposta.upper() == "N":
        continuar = False;
    elif(resposta.upper() != "S"):
        print("opção invalida")