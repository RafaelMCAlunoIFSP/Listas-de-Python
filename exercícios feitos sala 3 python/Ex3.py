mult = 0
mult_result = 0

numero = int(input("Digite o número da tabuada desejada: "))

while (mult <= 10):
    mult_result = numero * mult
    print(f"{numero} x {mult} = {mult_result}")
    mult = mult + 1