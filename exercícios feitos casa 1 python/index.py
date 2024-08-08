t = float(input("Digite o valor do tempo em segundos: "))

print("O valor do tempo digitado foi:", t)

s0 = 2
v0 = 3
a = 10

s = s0 + v0 * t + 1/2 * a * t**2

print("O valor de metros é de:", '%.2f' %s)