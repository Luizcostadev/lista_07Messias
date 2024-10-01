#Crie um programa que peça ao usuário uma frase e conte o número de vogais e consoantes presentes nela.
#Utilize um loop para percorrer cada caractere da frase e realizar a contagem.
frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
contagem_vogais = 0
contagem_consoantes = 0
for i in frase:
    if i in vogais:
        contagem_vogais += 1
    elif i in consoantes: +1
print(f" O total de vogais é :{contagem_vogais}  ")
print(f'O total de consoantes é : {contagem_consoantes}')
