#Implemente um programa que simule o lançamento de um dado de 6 faces várias vezes, conforme especificado pelo usuário.
#Utilize um loop para realizar os lançamentos e exibir os resultados.
#O programa deve continuar rodando até que o usuário decida pará-lo.
while True:
    #quantas vezes deseja lançar o dado
    vezes = int(input("Quantas vezes deseja lançar o dado? "))
    
    for i in range(vezes):
        #gerar um número aleatório entre 1 e 6
        import random
        dado = random.randint(1, 6)
        #mostrar o resultado
        print(f"Lançamento {i+1}: {dado}")
        