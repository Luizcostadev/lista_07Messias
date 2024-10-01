#Desenvolva um programa que peça ao usuário um número e gere a tabuada completa desse número (de 1 a 10).
# Utilize um loop para realizar as multiplicações e exibir os resultados de forma organizada.
numero = float(input("Insira um número (ou -1 para encerrar): "))

if numero == -1:
    print("Finalizando...")
else:
    print("A tabuada do número", numero, "é:")
    for i in range(1, 11):
        tabuada = numero * i
        print(f"{numero} x {i} = {tabuada}")