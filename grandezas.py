print("1. Tensão")
print("2. Resistência")
print("3. Corrente")
print("4. Sair")

opcao = int(input("Escolha: "))

# Estrutura de decisão para menu
if opcao == 1:
    R = float(input("Resistência: "))
    I = float(input("Corrente: "))
    U = R * I
    print(f"Tensão: {U}")

elif opcao == 2:
    U = float(input("Tensão: "))
    I = float(input("Corrente: "))
    R = U / I
    print(f"Resistência: {R}")

elif opcao == 3:
    U = float(input("Tensão: "))
    R = float(input("Resistência: "))
    I = U / R
    print(f"Corrente: {I}")

elif opcao == 4:
    print("Encerrando...")

else:
    print("Opção inválida!")
