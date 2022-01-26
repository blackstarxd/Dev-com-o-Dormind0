# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input("Digite um número e mostrarei se é positivo ou negativo: "))
if(valor == 0):
    print("O zero é um número neutro, ou seja, não é um número nem positivo e nem negativo.")

else:
    if(valor > 0):
        print("O número escolhido é positivo.")
    else:
        print("O número escolhido é negativo.")
        
print("")
input("Pressione enter para sair...")