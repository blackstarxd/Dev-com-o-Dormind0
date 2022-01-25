# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra_digitada = input("Digite uma letra, se for F ou f = Feminino e se for M ou m = Masculino, outras letras = Sexo Inválido: ")
if(letra_digitada == "F" or letra_digitada == "f"):
    print("F ou f é de Feminino.")
else:
    if(letra_digitada == "M" or letra_digitada == "m"):
        print("M ou m é de Masculino.")
    else:
        print("Sexo Inválido.")