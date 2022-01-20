#[17:11, 23/12/2021] Igor (Dormindo): Ler do teclado 2 valores, converter para float e exibir a média deles.
#[17:11, 23/12/2021] Igor (Dormindo): Exemplo
#[17:12, 23/12/2021] Igor (Dormindo): Supondo que a primeira nota seja 8 e a segunda seja 6, então a média dele vai ser a soma da primeira com a segunda dividido por 2
#[17:13, 23/12/2021] Igor (Dormindo): (8+6)/2
#[17:13, 23/12/2021] Igor (Dormindo): 7
#[17:13, 23/12/2021] Igor (Dormindo): Logo a média dele é 7
#[17:13, 23/12/2021] Igor (Dormindo): Façam essa versão com 2 entradas
#[17:13, 23/12/2021] Igor (Dormindo): E depois façam a versão com 3 entradas

primeira_nota = float (input("Digite a primeira nota: "))
segunda_nota = float (input("Digite a segunda nota: "))
mediade2 = (primeira_nota + segunda_nota) / 2

print("O resultado da média é: " +str(mediade2))