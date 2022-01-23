# Faça um Programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area_pintada = float(input("Insira o tamanho da área a ser pintada: "))
area_pintada_folga = area_pintada + (area_pintada * 10/100)
lata_de_tinta = float(18 * 6)
lata_de_tinta_preco = 80
galao_de_tinta = float(3.6 * 6)
galao_de_tinta_preco = 25
qtd_de_latas = round(float (area_pintada_folga / lata_de_tinta) + 0.5)
qtd_de_galao_de_tinta = round(float (area_pintada_folga / galao_de_tinta) + 0.5)
lata_e_galao_misturados = lata_de_tinta + galao_de_tinta
qtd_de_lata_e_galao_misturados = round(float (area_pintada_folga / lata_e_galao_misturados) + 0.5)

print("A area pintada com folga de 10% é: " + str(area_pintada_folga) + " metros quadrados.")
print("Caso você compre apenas latas de 18 litros, você terá que comprar: " +str(qtd_de_latas))
print("Caso você compre apenas galões de 3,6 litros, você terá que comprar: " +str(qtd_de_galao_de_tinta))
print("Caso você compre latas de 18 litros e galões de 3,6 litros para misturar, você terá que comprar: " +str(qtd_de_lata_e_galao_misturados) + " de cada.")

print("")
input("Pressione enter para sair...")