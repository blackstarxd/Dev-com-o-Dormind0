# Faça um Programa que leia três números e mostre o maior deles.

# primeiro_numero = int(input("Digite o primeiro numero: "))
# segundo_numero = int(input("Digite o segundo numero: "))
# terceiro_numero = int(input("Digite o terceiro numero: "))
# numeros = [primeiro_numero, segundo_numero, terceiro_numero]

# print(str(numeros))

primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))
terceiro_numero = int(input("Digite o terceiro numero: "))
numeros = [primeiro_numero, segundo_numero, terceiro_numero]
list.sort(numeros)
maior = numeros[2]
print(f'O maior número: {maior}.')

if(primeiro_numero > segundo_numero or primeiro_numero > terceiro_numero):
    print("O primeiro numero escolhido foi o maior: " +str(primeiro_numero))
else:
    if(segundo_numero > terceiro_numero):
        print("O segundo numero escolhido foi o maior: " +str(segundo_numero))
    else:
        print("O terceiro numero escolhido foi o maior: " +str(terceiro_numero))

# maior_numero = None

# for num in numeros:
#     if (maior_numero is None or num > maior_numero):
#         maior_numero = num

# print('O maior número foi:', maior_numero)