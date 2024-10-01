#Crie um programa que peça ao usuário um número inteiro e verifique se ele é primo.
#Utilize um loop para testar a divisibilidade do número por outros números menores.
def eh_primo(n):
    def eh_primo(n):
        if n <= 1:
            return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True