#Tendo como dados de entrada a altura de uma pessoa,
#construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Insira a altura, para calcular o peso ideal: "))

peso_ideal = (72.7 * altura) - 58

print("O seu peso ideal é: %.1f" % peso_ideal + " kg, com base na altura inserida.")

print("")
input("Pressione enter para sair...")