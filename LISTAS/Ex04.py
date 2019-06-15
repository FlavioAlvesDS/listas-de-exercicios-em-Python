"""
4) - Desenvolva um programa em python que leia valores inteiros para o vetor A e construa outro vetor B da seguinte forma:
VETOR - A [3,  8,   4,  2,  ...,  10]
VETOR - B [9,  4,  12,  1,  ...,  5]
"""
A = []
B = []
for c in range(1,11):
    A.append(int(input(f"Informe o {c}º numero :")))

for c in range(0,10):
    if c % 2 == 0:
        B.append(A[c]*3)
    else:
        B.append(A[c] / 2)

print(A)
print(B)
