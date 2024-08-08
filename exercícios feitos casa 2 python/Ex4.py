A = float(input("Digite o número de A: "))
B = float(input("Digite o número de B: "))
C = float(input("Digite o número de C: "))

maior = max(A, B, C)

menor = min(A, B, C)

meio = (A + B + C) - (maior + menor)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"O número do meio é: {meio}")