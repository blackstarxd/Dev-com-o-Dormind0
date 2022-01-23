#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
#o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

hora_trabalhada = float(input("Quanto você ganha por hora trabalhada? "))
numero_de_horas_trabalhadas = float(input("Quantas horas você trabalha por mês?"))

salario_bruto = hora_trabalhada * numero_de_horas_trabalhadas
ir = salario_bruto * 11/100
inss = salario_bruto * 8/100
sindicato = salario_bruto * 5/100
salario_liquido = salario_bruto - ir - inss - sindicato

print("Salário Bruto: R$ " +str(salario_bruto))
print("IR (11%): R$ " + str(ir))
print("INSS (8%): R$ "+ str(inss))
print("Sindicato ( 5%): R$ " + str(sindicato))
print("Salário Liquido: R$ " + str(salario_liquido))

print("")
input("Pressione enter para sair...")