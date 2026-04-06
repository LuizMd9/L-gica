litros = float(input("Litros: "))
tipo = input("Tipo (A/G): ").upper()

if tipo == "A":
    preco = 2.89
    desconto = 0.03 if litros <= 20 else 0.05

elif tipo == "G":
    preco = 4.95
    desconto = 0.04 if litros <= 20 else 0.06

else:
    print("Tipo inválido")
    preco = 0
    desconto = 0

total = litros * preco * (1 - desconto)
print(f"Total: R$ {total:.2f}")
