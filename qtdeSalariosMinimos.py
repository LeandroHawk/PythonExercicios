#ENTRADA DE DADOS = Solicitar ao usuário
nome = input("nome do trabalhador: ")
salario_do_trabalhador = float(
    input("Digite o valor do salario do trabalhador em R$:  "))

#variáveis
salario_minimo = 1412

#calcular quantos salários mínimos eu recebo
quantidade_de_salarios_minimos = salario_do_trabalhador / salario_minimo

# Exibir o resultado
print(f" A quantidade de salarios minimos que {nome} recebe é: {quantidade_de_salarios_minimos:.2f}")
