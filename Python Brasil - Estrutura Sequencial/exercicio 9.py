#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

Fahrenheit = float(input("Informe uma temperatura em graus Fahrenheit: "))

Celsius = 5 * ((Fahrenheit-32) / 9)

print("A temperatura informada convertida será de: %.1f"  % Celsius + " graus Celsius.")

print("")
input("Pressione enter para sair...")