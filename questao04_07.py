# Implemente um jogo onde o computador escolhe um número aleatório entre 1 e 100, e o usuário tenta adivinhar.
#Utilize um loop para permitir que o usuário faça várias tentativas, fornecendo dicas (maior ou menor) a cada tentativa.
import random
numero_sortido = random.randint(1,100)

print("Eu escolhi um número de 1 a 100, Tu não vai acertar nem a pau!")

while True:
    tentativa = int(input('Manda bala!'))
    if tentativa < numero_sortido:
        print('tá frio, é menor', tentativa)
    elif tentativa > numero_sortido:
        print('tá quente, é maior', tentativa)
    elif tentativa == numero_sortido:
        print ('Marrapais não é que tu acertou mermo!')
        break