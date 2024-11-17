# Solicitar a string do usuário
texto = input("Digite uma string: ")

# Criar um dicionário para armazenar a contagem de caracteres
contagem_caracteres = {}

# Usar um loop for para iterar sobre cada caractere na string
for caractere in texto:
    if caractere in contagem_caracteres:
        contagem_caracteres[caractere] += 1
    else:
        contagem_caracteres[caractere] = 1

# Exibir a contagem de cada caractere
for caractere, contagem in contagem_caracteres.items():
    print(f"{caractere}: {contagem}")
