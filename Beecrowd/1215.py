""" while True:
    try:
    #seu código entra aqui
    print("asdsa")
    
except EOFError:
    break """

dicionario = []

texto = input("digite um texto: ")

caracteres = len(texto)
linha = float((caracteres) / 200)

if(linha >= 10000):
  print("A entrada contém no máximo 10000 linhas de texto.")
  quit()
  

else:
  
  palavras = texto.split()

for palavra in palavras:
  if(range(len(dicionario) == 5000)):
    print("O dicionário atingiu o máximo de 5000 palavras, não será possível adicionar todas...")
  else:
    (palavra.lower() not in dicionario)
    dicionario.append(palavra.lower()) 
    
#print(dicionario)
dicionario.sort()

for dic in dicionario:
    print(dic)

#print(f"O texto possui {linha:.1f} linhas e {caracteres} caracteres.")
#print("")