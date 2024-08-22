cont = 0
cont2 = 1
cont_vezes = 1

while (cont_vezes <= 15):
    cont = cont + cont2
    cont2 = cont - cont2
    print(cont)

    cont_vezes = cont_vezes + 1