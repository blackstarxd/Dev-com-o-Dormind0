#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

numero_de_horas_trabalhadas = float(input("Quantas horas você trabalha por mês? ")) #(16:00 - 06:00) =  10h - 1h de almoço = 9h * 21 dias = 189 horas (Média de dias uteis no mês em 2022.)

hora_de_trabalho = float(input("Quanto você ganha por hora? ")) # R$ 1701 / 189 horas no mês = 9


salario = numero_de_horas_trabalhadas * hora_de_trabalho

hora_extra = hora_de_trabalho * 1.5

print("Você recebe: R$ " +str(salario) + " por mês.")
print("Você receberá : R$ " +str(hora_extra) + " por cada hora extra, de segunda a sabado.")