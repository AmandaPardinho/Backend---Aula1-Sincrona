# Este programa vai cadastrar um produto em dicionário
print("CADASTRO DE PRODUTO")

# Dicionário criado para guardar dados
produto = {}

produto["id"] = int(input("Insira o código do produto: "))
produto["nome"] = input("Insira o nome do produto: ")
produto["preco"] = float(input("Insira o preço do produto: "))

# Exibição do dicionário completo, com a mesma estrutura do código
print(produto)

# Exibição dos itens do dicionário, separando chave e valor
for chave, valor in produto.items():
    print(f"{chave} => {valor}")
