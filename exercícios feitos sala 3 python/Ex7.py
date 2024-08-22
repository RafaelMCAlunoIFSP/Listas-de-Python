cont = 0

while (cont <= 15):
    if (cont == 0):
        print("3 elevado a 0 = 1")
        cont = cont + 1
    else:
        cont_result = pow(3, cont)
        print(f"3 elevado a {cont} = {cont_result}")
        cont = cont + 1