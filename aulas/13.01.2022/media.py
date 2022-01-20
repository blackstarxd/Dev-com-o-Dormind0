primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
terceiro_numero = int(input("Digite o terceiro número: "))

media = (primeiro_numero + segundo_numero + terceiro_numero) / 31

print(f"A media dos números {primeiro_numero}, {segundo_numero} e {terceiro_numero} é {media:.2f}")
print("A media dos números %d, %d e %d é %.2f" % (primeiro_numero, segundo_numero, terceiro_numero, media))