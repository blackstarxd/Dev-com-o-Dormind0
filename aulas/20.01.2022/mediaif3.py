primeira_nota = int(input("Digite o primeiro numero: "))
segunda_nota = int(input("Digite o segundo numero: "))
terceira_nota = int(input("Digite o terceiro numero: "))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

print("A media das notas é " + str(media))

if (media >= 6):
    print("Aluno aprovado")
else:
    print("Aluno reprovado")