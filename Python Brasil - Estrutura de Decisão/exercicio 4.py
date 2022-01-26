# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra_digitada = input("Digite uma letra e informarei se é vogal ou consoante: ")

if(letra_digitada == "A" or letra_digitada == "a" or letra_digitada == "E" or letra_digitada == "e" or letra_digitada == "I" or letra_digitada == "i" or letra_digitada == "O" or letra_digitada == "o" or letra_digitada == "U" or letra_digitada == "u"):
    print("Essa letra é Vogal.")
else:
    print("Essa letra é Consoante.")
    
print("")
input("Pressione enter para sair...")