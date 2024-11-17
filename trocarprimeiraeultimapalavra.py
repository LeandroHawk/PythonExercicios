# Solicitar ao usuário que digite uma palavra
palavra = input("Digite uma palavra: ")

# Pegar a primeira e a última letra
primeira_letra = palavra[0]
ultima_letra = palavra[-1]

# Formar a nova palavra com as letras trocadas
nova_palavra = ultima_letra + palavra[1:-1] + primeira_letra

# Exibir a palavra modificada
print(f"Palavra modificada: {nova_palavra}")