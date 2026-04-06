# Solicita a velocidade do carro
velocidade = float(input("Digite a velocidade em Km/h: "))

limite = 80

# Estrutura de decisão para verificar se ultrapassou o limite
if velocidade > limite:
    excedente = velocidade - limite
    multa = excedente * 50
    print(f"Excedeu {excedente} Km/h")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Velocidade dentro do limite")
