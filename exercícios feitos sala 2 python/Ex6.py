import math

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

delta = B**2 - 4*A*C

if A == 0:
    print("O valor de A não pode ser 0 em uma equação de segundo grau.")
elif delta < 0:
    print("Não existem raízes reais para os valores informados.")
else:
    x1 = (-B + math.sqrt(delta)) / (2 * A)
    x2 = (-B - math.sqrt(delta)) / (2 * A)

    print(f"As raízes da equação são: x1 = {x1} e x2 = {x2}")