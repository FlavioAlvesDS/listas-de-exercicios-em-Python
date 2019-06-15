"""
5) - Escrever um algoritmo para uma empresa que decide dar um reajuste a seus 584 funcionários de
acordo com os seguintes critérios:
	a) 50% para aqueles que ganham menos do que três salários mínimos;
	b) 20% para aqueles que ganham entre três até dez salários mínimos;
	c) 15% para aqueles que ganham acima de dez até vinte salários mínimos;
	d) 10% para os demais funcionários.
	Leia o nome do funcionário, seu salário e o valor do salário mínimo.
	Calcule o seu novo salário reajustado.
	Escrever o nome do funcionário, o reajuste e seu novo salário. Calcule quanto à empresa vai
	aumentar sua folha de pagamento.
"""
contador = 1
reajuste = 0
salNovo = 0
aumentoFolha = 0

salMinimo = float(input("Informe o Valor do salario Minino :"))
while(contador <= 584):

    nome = input(f"Informe o nome do {contador} º do Funcionario : ")
    salario = float(input("Informe o Salario :"))


    if(salario < (3 * salMinimo)):
        reajuste = (salario * 50)/100
        salNovo = salario + reajuste
        aumentoFolha = aumentoFolha + reajuste
        print("---------------------------------------------------------------------------------")
        print(f"{nome} teve um reajuste de R${reajuste} reais seu novo salario sera R${salNovo} reais")
        print("---------------------------------------------------------------------------------")
    elif(salario < (10 * salMinimo)):
        reajuste = (salario * 20) / 100
        salNovo = salario + reajuste
        aumentoFolha = aumentoFolha + reajuste
        print("---------------------------------------------------------------------------------")
        print(f"{nome} teve um reajuste de R${reajuste} reais seu novo salario sera R${salNovo} reais")
       

    elif (salario < (20 * salMinimo)):
        reajuste = (salario * 15) / 100
        salNovo = salario + reajuste
        aumentoFolha = aumentoFolha + reajuste
        print("---------------------------------------------------------------------------------")
        print(f"{nome} teve um reajuste de R${reajuste} reais seu novo salario sera R${salNovo} reais")
    
    else:
        reajuste = (salario * 10) / 100
        salNovo = salario + reajuste
        aumentoFolha = aumentoFolha + reajuste
        print("---------------------------------------------------------------------------------")
        print(f"{nome} teve um reajuste de R${reajuste} reais seu novo salario sera R${salNovo} reais")
    contador = contador + 1
print("---------------------------------------------------------------------------------")    
print(f"A Empresa teve um aumento de R$ {aumentoFolha} Reais na sua folha de Pagamento")
