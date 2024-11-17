# Inicializando o estoque como um dicionário
estoque = {
    "maçã": 10,
    "banana": 5,
    "cereja": 8
}

# Lista para produtos fora de estoque
lista_espera = []

def verificar_estoque(produto, quantidade):
    if produto in estoque:
        if estoque[produto] > 0:
            if quantidade <= estoque[produto]:
                return "Disponível"
            else:
                return "Quantidade indisponível"
        else:
            return "Fora de estoque"
    else:
        return "Não encontrado"

def atualizar_estoque(produto, quantidade):
    estoque[produto] -= quantidade
    print(f"{produto} atualizado. Quantidade restante: {estoque[produto]}")

def adicionar_produto_estoque():
    while True:
        produto = input("Digite o nome do novo produto (ou 'sair' para encerrar): ")
        if produto.lower() == 'sair':
            break
        quantidade = int(input(f"Digite a quantidade de {produto}: "))
        estoque[produto] = quantidade
        print(f"{produto} adicionado ao estoque com {quantidade} unidades.")

def processar_venda(produto, quantidade):
    status = verificar_estoque(produto, quantidade)
    if status == "Disponível":
        atualizar_estoque(produto, quantidade)
        print(f"Venda de {quantidade} {produto}(s) concluída com sucesso!")
    elif status == "Quantidade indisponível":
        print(f"Quantidade indisponível. Apenas {estoque[produto]} unidades em estoque.")
    elif status == "Fora de estoque":
        print("Produto fora de estoque. Deseja ser notificado quando estiver disponível?")
        adicionar_lista = input("Deseja adicionar seu nome à lista de espera? (s/n): ")
        if adicionar_lista.lower() == 's':
            nome_cliente = input("Digite seu nome: ")
            lista_espera.append(nome_cliente)
            print(f"{nome_cliente}, você foi adicionado à lista de espera.")
        print("Produtos alternativos disponíveis:")
        produtos_alternativos = [p for p in estoque if estoque[p] > 0]
        print(", ".join(produtos_alternativos))
    elif status == "Não encontrado":
        print("Produto não encontrado.")

# Função principal para interagir com o usuário
def sistema_controle_estoque():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar novo produto ao estoque")
        print("2. Processar venda de produto")
        print("3. Sair")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            adicionar_produto_estoque()
        elif opcao == '2':
            produto = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade desejada: "))
            processar_venda(produto, quantidade)
        elif opcao == '3':
            print("Encerrando o sistema de controle de estoque. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o sistema de controle de estoque
sistema_controle_estoque()
