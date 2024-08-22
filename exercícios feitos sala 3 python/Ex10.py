cont = 0
auxiliar = 0

while (cont <= 499):
    if (cont % 2 == 0):
        auxiliar = auxiliar + cont
    cont = cont + 1

if (cont == 500):
    auxiliar = auxiliar + cont
    print(auxiliar)