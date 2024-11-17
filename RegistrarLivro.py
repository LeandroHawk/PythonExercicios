# Solicitar informações do livro ao usuário
titulo = input("Digite o título do livro: ")
autor = input("Digite o nome do autor: ")
preco = float(input("Digite o preço (R$) do livro: "))

# Armazenar as informações em um dicionário
livro = {
    "Título": titulo,
    "Autor": autor,
    "Preço": preco
}

# Salvando a informação no arquivo
with open("livros.txt", "a") as arquivo:
    arquivo.write(f"{livro}\n")

print("Livro registrado com sucesso!")