nome_produto = input("digite o nome do produto: ")
preco = float(input("digite o preco do produto: "))
desconto = float(input("digite o percentual de desconto: "))
valor_desconto = preco * desconto / 100
preco_final = preco = valor_desconto
print(f"produto: {nome_produto} - preco final: R$ {preco_final}")