nome = input("Digite o nome: ")
salario_bruto = float(input("Digite o salário bruto (R$): "))

inss = salario_bruto * 0.11

base_irrf = salario_bruto - inss
irrf = base_irrf * 0.075


salario_liquido = salario_bruto - inss - irrf

print(f"\nFuncionário: {nome}")
print(f"Desconto INSS: R$ {inss:.2f}")
print(f"Desconto IRRF: R$ {irrf:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
