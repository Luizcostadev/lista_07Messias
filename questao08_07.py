#Desenvolva um programa que converta um número decimal fornecido pelo usuário para sua representação binária.
#Utilize um loop para realizar as divisões sucessivas por 2 e armazenar os restos.
def decimal_para_binario(numero):
    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    return binario

numero = int(input("Digite um número decimal: "))
binario = decimal_para_binario(numero)
print(f"O número {numero} em binário é {binario}")