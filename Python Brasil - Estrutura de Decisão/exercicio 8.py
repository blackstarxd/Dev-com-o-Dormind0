# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

primeiro_produto = float(input("Qual o valor em R$ do primeiro produto?"))
segundo_produto = float(input("Qual o valor em R$ do segundo produto?"))
terceiro_produto = float(input("Qual o valor em R$ do terceiro produto?"))

if(primeiro_produto < segundo_produto or primeiro_produto < terceiro_produto):
    print("O primeiro produto é o mais barato, no valor de: R$ " +str(primeiro_produto) + "0")
else:
    if(segundo_produto < terceiro_produto):
        print("O segundo produto é o mais barato, no valor de: R$ " +str(segundo_produto) + "0")
    else:
        print("O terceiro produto é o mais barato, no valor de: R$ " +str(terceiro_produto) + "0")