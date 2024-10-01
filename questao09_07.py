#Crie um programa que desenhe padrões simples com caracteres, como triângulos, quadrados ou losangos.
#Utilize loops aninhados para controlar a quantidade de linhas e colunas e a exibição dos caracteres.
def desenhar_triângulo(tamanho):
    for i in range(tamanho):
        print(" " * (tamanho - i - 1) + "*" * (2 * i + 1))

def desenhar_quadrado(tamanho):
    for i in range(tamanho):
        print("*" * tamanho)

def desenhar_losango(tamanho):
    for i in range(tamanho):
        print(" " * (tamanho - i - 1) + "*" * (2 * i + 1))
    for i in range(tamanho - 2, -1, -1):
        print(" " * (tamanho - i - 1) + "*" * (2 * i + 1))

print("Escolha um padrão:")
print("1. Triângulo")
print("2. Quadrado")
print("3. Losango")

opcao = int(input("Digite a opção: "))

if opcao == 1:
    tamanho = int(input("Digite o tamanho do triângulo: "))
    desenhar_triângulo(tamanho)
elif opcao == 2:
    tamanho = int(input("Digite o tamanho do quadrado: "))
    desenhar_quadrado(tamanho)
elif opcao == 3:
    tamanho = int(input("Digite o tamanho do losango: "))
    desenhar_losango(tamanho)
else:
    print("Opção inválida")




