#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
#
#Para fazer o cálculo da área do quadrado é necessário realizar o produto entre dois lados.
#Como o quadrado tem lados iguais, basta pegar a medida de um dos lados e elevar ao quadrado.
#Para a realização usamos a fórmula da área A = b. h, assim um de seus lados será a base (b) e o outro a altura (h)


base = int(input("Digite a medida da base: "))
height = int(input("Digite a medida da altura: "))

area = base * height

dobro_area = area * 2

print("A área do quadrado de acordo com as medidas escolhidas é de: " +str (area))
print("O dobro desta área será: " +str (dobro_area))