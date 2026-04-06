valor = float(input("Valor da compra: "))
pagamento = int(input("Forma de pagamento (1-4): "))

if pagamento == 1:
    desconto = 0.10
elif pagamento == 2:
    desconto = 0.05
elif pagamento == 3:
    desconto = 0.03
elif pagamento == 4:
    desconto = 0.075
else:
    print("Opção inválida")
    desconto = 0

final = valor - (valor * desconto)
print(f"Valor final: R$ {final:.2f}")
