# Faça um Programa que peça dois números e imprima o maior deles.

primeiro_numero = int(input("Insira o primeiro numero: "))
segundo_numero = int(input("Insira o segundo numero: "))

if (primeiro_numero > segundo_numero):
    print("O primeiro numero escolhido foi o maior: " + str(primeiro_numero))
else:
    print("O segundo numero escolhido foi o maior: " + str(segundo_numero))
    
print("")
input("Pressione enter para sair...")