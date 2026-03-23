consumo = float(input("Digite o consumo de água em m3: "))
if consumo <= 10:
    valor = consumo = 44.95
elif consumo <= 20: 
    valor = consumo * 8.75
elif consumo <= 50: 
    valor = consumo * 16.76
else: valor = consumo * 17.46

print("-" * 40)
print(f"Consumo registrado: {consumo} m³")
print(f"O valor total da conta Comercial/Industrial é: R$ {valor:.2f}")
print("-" * 40)
