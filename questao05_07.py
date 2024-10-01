#Desenvolva um programa que gere os primeiros N números da sequência de Fibonacci, onde N é fornecido pelo usuário.
#Utilize um loop para calcular e exibir os termos da sequência.
n = int(input("Quantos termos você deseja gerar? "))
t1 = 0
t2 = 1
print(f"Os primeiros {n} termos da sequência de Fibonacci são:")
if n == 1:
    print(t1)
else:
    print(f"{t1} {t2}")
    for i in range(2, n):
        t3 = t1 + t2
        print(t3, end=" ")
        t1 = t2
        t2 = t3
        
