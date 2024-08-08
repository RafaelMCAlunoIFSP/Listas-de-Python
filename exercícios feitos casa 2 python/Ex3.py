nota = float(input("Digite a nota desejada: "))

resto = nota - int(nota)

if (resto > 0.5):

    nota = int(nota) + 1

    print("A nota foi arredondada para", nota)

elif (resto > 0):

    nota = int(nota)

    print("A nota foi arredondada para", nota)

else:

    print("A nota", nota, "não precisa ser arredondada.")