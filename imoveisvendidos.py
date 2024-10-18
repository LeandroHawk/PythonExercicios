# Solicitar informações do corretor
nome = input("Digite o nome do corretor: ")
quantidade_imoveis_vendidos = int(input("Digite a quantidade de imóveis vendidos: "))
valor_total_vendas = float(input("Digite o valor total das vendas: R$ "))

# Definir variáveis
salario_base = 1500.00
comissao_por_imovel = 200.00
percentual_comissao_vendas = 0.05

# Calcular o salário final
comissao_total = quantidade_imoveis_vendidos * comissao_por_imovel
comissao_sobre_vendas = valor_total_vendas * percentual_comissao_vendas
salario_final = salario_base + comissao_total + comissao_sobre_vendas

# Exibir o resultado
print(f"Salário final do corretor {nome}: R$ {salario_final:.2f}")
