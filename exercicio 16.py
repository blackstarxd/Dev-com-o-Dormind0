#Faça um programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
#
#       print("Arredondado pra baixo: ", round(num-0.5) )
#       print("Arredondado pra cima : ", round(num+0.5) )
# Por exemplo:
# numero = 1.23456789

# round(numero, 1) = 1.2
# round(numero, 2) = 1.23
# round(numero, 3) = 1.235

area_pintada = float(input("Insira o tamanho em metros quadrados da área a ser pintada: "))
cobertura_da_tinta_lata = float(18 * 3)
valor_da_lata = float(80)
qtd_de_latas = round(float(area_pintada / cobertura_da_tinta_lata) + 0.5)

print("Você precisará de " +str (qtd_de_latas)  + " latas de tinta arredondando para cima.")
print("O valor será de: R$ " +str(qtd_de_latas * valor_da_lata) + "0")


