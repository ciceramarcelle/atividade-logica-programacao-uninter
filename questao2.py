# Boas-vindas com meu nome
print("Bem-vindo a Loja de Açaí e Cupuaçu da Cícera Marcelle de Melo Ferreira")
# dados da tabela
tabela = [
    ["Tamanho", "Cupuaçu (CP)", "Açaí (AC)"],
    ["P", "R$9,00", "R$ 11,00"],
    ["M", "R$14,00", "R$ 16,00"],
    ["G", "R$18,00", "R$ 20,00"],
]

# imprimindo a tabela
for linha in tabela:
    print("{: <10} {: <10} {: <10}".format(*linha))

# Total
total_pedido = 0

# para receber pedidos
while True:
    # input de sabor
    sabor = input("Digite o sabor desejado: \n(CP para Cupuaçu / AC para Açaí): ")

    # verificar se o sabor é válido
    if sabor != 'CP' and sabor != 'AC':
        print("Sabor inválido. Tente novamente.")
        continue  # para voltar ao início

    # input de tamanho
    tamanho = input("Digite o tamanho desejado: \nTamanho (P para Pequeno / M para Médio / G para Grande): ")

    # verificar se o tamanho é válido
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print("Tamanho inválido. Tente novamente")
        continue  # para voltar ao início do loop

    # Implementar if, elif e/ou else com cada uma das combinações de sabor e tamanho
    if sabor == 'CP':
        if tamanho == 'P':
            valor_pedido = 9
            produto = 'Cupuaçu'
            tamanho_descricao = 'Pequeno'
        elif tamanho == 'M':
            valor_pedido = 14
            produto = 'Cupuaçu'
            tamanho_descricao = 'Médio'
        else:
            valor_pedido = 18
            produto = 'Cupuaçu'
            tamanho_descricao = 'Grande'
    elif sabor == 'AC':
        if tamanho == 'P':
            valor_pedido = 11
            produto = 'Açaí'
            tamanho_descricao = 'Pequeno'
        elif tamanho == 'M':
            valor_pedido = 16
            produto = 'Açaí'
            tamanho_descricao = 'Médio'
        else:
            valor_pedido = 20
            produto = 'Açaí'
            tamanho_descricao = 'Grande'

    # para somar valores dos pedidos
    total_pedido += valor_pedido

    # mensagem do pedido
    print(f"Você pediu um {produto} no tamanho {tamanho_descricao} e isso custa R$ {valor_pedido:.2f}")

    # deseja pedir mais alguma coisa?
    mais_pedidos = input("Deseja mais alguma coisa? (S para Sim / N para Não): ")
    if mais_pedidos == 'N':
        break #pra parar 
    elif mais_pedidos == 'S':
        continue  # para voltar ao início

# saída do valor total 
print(f"\nTotal do pedido: R$ {total_pedido:.2f}")