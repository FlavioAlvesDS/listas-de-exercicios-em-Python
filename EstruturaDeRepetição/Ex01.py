'''
1) - Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive).
'''
numero = 0
contador = 1
qtIntervalo = 0

while contador <= 80:
    numero = int(input(f"Informe o {contador}° numero :"))
    contador = contador + 1
    if numero >=10:
        if numero <=150:
                qtIntervalo = qtIntervalo + 1

print(f"Foram encontrados {qtIntervalo} numeros entre 10 e 150 .")