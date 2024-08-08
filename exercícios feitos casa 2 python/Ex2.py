num = int(input("Digite um número inteiro entre 0 e 100: "))

num_chave = 45

if (num >= 101):

    print("Número maior do que 100, refaça.")

elif (num <= -1):
    
    print("Número menor do que 0, refaça.")

elif (num_chave > num):

    print("Seu número está a", num_chave - num, "unidades de distância do número chave.")

elif (num_chave < num):

    print("Seu número está a", num - num_chave, "unidades de distância do número chave.")