#Distância Entre Dois Pontos

# x1, y1 = map(float, input("Insira os dois valores de ponto flutuante: x1 e y1: ").split())
# x2, y2 = map(float, input("Insira os dois valores de ponto flutuante: x2 e y2: ").split())

# distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# print(f"A distância entre os dois pontos é: {distancia:.4f}")

#A solução no Beecrowd leva em conta até mesmo se for digitado algum texto a mais dentro do Input ou Print.

p1  = list(map(float, input().split()))
p2  = list(map(float, input().split()))

x1 = p1[0]
y1 = p1[1]

x2 = p2[0]
y2 = p2[1]

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print(f"{distancia:.4f}")