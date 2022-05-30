#Montar um dicionario de quantidade de palavras do seguinte texto
#Ex(*$a#.mpl.e: Adventures in Disneyland Two blondes were going to Disneyland when they came to a fork in the road. The sign read: "Disneyland LEFT." So they went home.
#[19:51]
#Utilizar split, for, if e dicionario

dicionario = {}

texto = input()
palavras = texto.split()

for palavra in palavras:
    if palavra not in dicionario.keys():
        dicionario[palavra] = 1
    else:
        dicionario[palavra] += 1
  
keys_ordenadas = sorted(dicionario)
for key in keys_ordenadas:
  print(f"{key} aparece {dicionario[key]} vez(es)")