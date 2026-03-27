import math

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("1-Soma, 2-Sub, 3-Mult, 4-Div, 5-Pot, 6-Raiz, 7-Par/Ímpar")
op = int(input("Escolha a operação: "))

if op == 1: print(f"Soma: {n1 + n2}")
elif op == 2: print(f"Subtração: {n1 - n2}")
elif op == 3: print(f"Multiplicação: {n1 * n2}")
elif op == 4: print(f"Divisão: {n1 / n2}" if n2 != 0 else "Erro: Divisão por zero")
elif op == 5: print(f"Potência: {n1 ** n2}")
elif op == 6: print(f"Raiz de {n1}: {math.sqrt(n1)} | Raiz de {n2}: {math.sqrt(n2)}")
elif op == 7 or op == 8:
    check = n1 # Exemplo com o primeiro número
    print(f"{check} é {'Par' if check % 2 == 0 else 'Ímpar'}")
