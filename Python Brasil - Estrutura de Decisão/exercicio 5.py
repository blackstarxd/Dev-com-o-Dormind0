# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

primeira_nota = int(input("Digite a primeira nota: "))
segunda_nota = int(input("Digite a segunda nota: "))

media = int((primeira_nota + segunda_nota) / 2)

print("A média foi: " +str(media))
if(media == 10):
    print("Aprovado com Distinção.")
else:
    if(media >= 7):
        print("Aprovado.")
    else:
        if(media < 7):
            print("Reprovado.")
            
print("")
input("Pressione enter para sair...")