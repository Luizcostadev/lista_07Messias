#Implemente um programa que calcule o fatorial de um número fornecido pelo usuário.
#Utilize um loop para realizar as multiplicações necessárias.
def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial


numero = int(input("Digite um número: "))
fatorial = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {fatorial}")
