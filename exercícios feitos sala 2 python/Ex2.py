nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2)/2

if media >= 6:
    print("Aprovado. Média:" '%.2f' %media)

else:
    nota_exame = float(input("Reprovado. Digite a nota de exame: "))

    media = media + nota_exame

    if media >= 5:
        print("Aprovado. Média:" '%.2f' %media)
    else:
        print("Reprovado. Média:" '%.2f' %media)