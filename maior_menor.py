num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

# Maior número
maior = max(num1, num2, num3)

# Menor número
menor = min(num1, num2, num3)

soma = num1 + num2 + num3
media = soma / 3

print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Soma: {soma}")
print(f"Média: {media}")
