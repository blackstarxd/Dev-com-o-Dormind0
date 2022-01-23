#Faça um programa que peça o tamanho de um arquivo para download (em MB)
#e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
#aproximado de download do arquivo usando este link (em minutos).

tamanho_download = float(input("Insira o tamanho do arquivo de download (em MB): "))
velocidade_internet = float(input("Insira a velocidade da internet (em Mbps): "))

calc_velocidade_internet = float(velocidade_internet / 8)
calc_tamanho_download = float(tamanho_download / calc_velocidade_internet)

calc_tempo_download_seg = int(calc_tamanho_download / velocidade_internet)

#Divide pelo inteiro e "pega" o resto dos segundos, depois exibe nas variaveis.
dias = calc_tempo_download_seg // 86400 # Operador // Divisão inteira, sem considerar o resto.
segundos_rest = calc_tempo_download_seg % 86400 # Operador % Resto da divisão.
horas = segundos_rest // 3600 # Operador // Divisão inteira, sem considerar o resto novamente.
segundos_rest = segundos_rest % 3600 # Operador % Resto da divisão.
minutos = segundos_rest // 60 # Operador // Divisão inteira, sem considerar o resto novamente.
segundos_rest = segundos_rest % 60 # Operador % Resto da divisão.

print("O tempo total em segundos é: " + str(calc_tempo_download_seg))
print("O tempo aproximado de download, baseado nas informações inseridas será de: " + str(dias) + " dias " + str(horas) + " horas " + str(minutos) + " minutos e " + str(segundos_rest) + " segundos.")

#Caso fosse só em minutos e segundos seria assim:

min = int(calc_tempo_download_seg // 60)
seg = int(calc_tamanho_download % 60)

print("")
print("Somente minutos e segundos : " + str(min) + " minutos e " + str(seg) + " segundos.")

print("")
input("Pressione enter para sair...")