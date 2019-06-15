"""

20) - Escrever um algoritmo que leia três valores inteiros e verifique se eles podem ser os lados de um triângulo.
 Se for, informar qual o tipo de triângulo que eles formam: equilátero, isóscele ou escaleno. Propriedade:
 o comprimento de cada lado de um triângulo é menor do que a soma dos comprimentos dos outros dois lados.

Triângulo Equilátero: aquele que tem os comprimentos dos três lados iguais;
Triângulo Isóscele: aquele que tem os comprimentos de dois lados iguais.
Portanto,todo triângulo equilátero é também isóscele
Triângulo Escaleno: aquele que tem os comprimentos de seus três lados diferentes.
Repita esse processo 5 vezes.
"""
tri = 1
a = 0
b = 0
c = 0
for cont in range(5):

    for tri in range(1):
        a = int(input(f"Informe o 1º numero :"))
        b = int(input(f"Informe o 2º numero :"))
        c = int(input(f"Informe o 3º numero :"))
        print("---------------------------------------------")

        if(c > a+b)|( b > a+c )|( a > b+c):
            print("Os numeros informados nao formam um Triângulo")
        elif (a==b) & (b==c):
                print(f"os numeros formam Um triangulo Equilátero")
        elif (a==b)|( a==c )|(b==c):
                print(f"os numeros formam Um triangulo Isóscele")
        else:
            print("Os numeros informados nao formam um Escaleno")
        print("---------------------------------------------")
