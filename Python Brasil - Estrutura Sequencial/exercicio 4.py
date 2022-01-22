#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota_um = int(input("Digite a primeira nota: "))
nota_dois = int(input("Digite a segunda nota: "))
nota_tres = int(input("Digite a terceira nota: "))
nota_quatro = int(input("Digite a quarta nota: "))

mediainteiro = int (nota_um + nota_dois + nota_tres + nota_quatro / 4)
mediavariavel = nota_um + nota_dois + nota_tres + nota_quatro / 4

print("A média das quatro notas em inteiro foi: " + str(mediainteiro))
print("A média das quatro notas em variavel foi: " + str(mediavariavel))