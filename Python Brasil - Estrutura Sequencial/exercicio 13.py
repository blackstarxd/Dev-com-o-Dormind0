#Tendo como dado de entrada a altura (h) de uma pessoa,
#construa um algoritmo que calcule seu peso ideal,utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input("Insira a altura, para calcular o peso ideal: "))

peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7

print("Caso você seja homem o seu peso ideal é: %.1f" % peso_ideal_homem + " kg, com base na altura inserida.")
print("Caso você seja mulher o seu peso ideal é: %.1f" % peso_ideal_mulher + " kg, com base na altura inserida.")

print("")
input("Pressione enter para sair...")