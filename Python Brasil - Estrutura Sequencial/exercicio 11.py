#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a - o produto do dobro do primeiro com metade do segundo .
#b - a soma do triplo do primeiro com o terceiro.
#c - o terceiro elevado ao cubo.

primeiro_numero = int(input("Digite o primeiro número inteiro: "))
segundo_numero = int(input("Digite o segundo número inteiro: "))
terceiro_numero = float(input("Digite o terceiro número real: "))

a = primeiro_numero * 2 + (segundo_numero / 2)
b = primeiro_numero * 3 + (terceiro_numero)
c = terceiro_numero ** 3

print("O resultado do dobro do primeiro com metade do segundo: " + str(a))
print("O resultado da soma do triplo do primeiro com o terceiro: " + str(b))
print("O resultado do terceiro elevado ao cubo." + str(c))

print("")
input("Pressione enter para sair...")