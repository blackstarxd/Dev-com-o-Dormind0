#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#F = C x 1,8 + 32

Celsius = float(input("Informe uma temperatura em graus Celsius: "))

Fahrenheit = Celsius * 1.8 + 32

print("A temperatura informada convertida será de: %.1f" % Fahrenheit + " graus Fahrenheit.")

print("")
input("Pressione enter para sair...")