# Mensagem de boas-vindas
print("Bem-vindo a copiadora da Cícera Marcelle de Melo Ferreira!")

# Função para perguntar e retornar o serviço desejado
def escolha_servico():
    while True:
        servicos = input('Entre com o serviço desejado:\n'
                         'DIG - Digitalização\n'
                         'ICO - Impressão colorida\n'
                         'IPB - Impressão Preto e Branco\n'
                         'FOT - Fotocópia\n')
        if servicos in ['DIG', 'ICO', 'IPB', 'FOT']:
            return servicos
        else:
            print("Escolha inválida. Entre com o tipo do serviço novamente.")

# Função para perguntar e retornar o número de páginas com desconto
def num_pagina():
    while True:
        try:
            num_paginas = int(input("Digite o número de páginas: "))
            if num_paginas < 20:
                return num_paginas #sem desconto
            elif 20 <= num_paginas < 200:
                return int(num_paginas * 0.85) #cálculo de desconto de 15%
            elif 200 <= num_paginas < 2000:
                return int(num_paginas * 0.80) #cálculo de desconto de 20%
            elif 2000 <= num_paginas < 20000:
                return int(num_paginas * 0.75) #cálculo de desconto de 25%
            else:
                print("Não aceitamos tantas páginas de uma vez.\n Entre com o número de páginas novamente.") #ultrapassou o limite de paginas, que é 20.000
        except ValueError:
            print("Por favor, digite um valor numérico.")

# Função para perguntar e retornar o valor do serviço adicional
def servico_extra():
    while True:
        servico_adicional = input("Deseja adicionar algum serviço? \n"
                         '1 - Encadernação Simples - R$15.00\n'
                         '2 - Encadernação Capa Dura - R$ 40.00\n'
                         '0 - Não desejo mais nada\n')
        if servico_adicional in ['1', '2', '0']:
            return int(servico_adicional)
        else:
            print("Opção inválida. Por favor, escolha entre 1, 2 ou 0.")



# para obter o serviço desejado
servico = escolha_servico()

# para obter o número de páginas com desconto
num_paginas = num_pagina()

# para obter o serviço adicional
servico_adicional = servico_extra()

# Calcula o custo do serviço selecionado
if servico == 'DIG':
    custo_servico = 1.10 #digitalizaçao é 1,10
elif servico == 'ICO':
    custo_servico = 1.00 #impressao colorida é 1,00
elif servico == 'IPB':
    custo_servico = 0.40 #impressao pb é 40 cents
else:  # servico == 'fot'
    custo_servico = 0.20 #custo por pag é 20 cents

# Para calcular o custo do serviço adicional
if servico_adicional == 0:
    custo_adicional = 0 #caso nao queira nada, é 0 reais
elif servico_adicional == 1:
    custo_adicional = 15 #encadernaçao simples = add 15 reais
else:  # servico_adicional == 2
    custo_adicional = 40 #encadernaçao capa dura = add 40 reais

# Para calcular o valor total a pagar (O valor final da conta é calculado da seguinte maneira: total = (servico * num_pagina) + extra)
total = (custo_servico * num_paginas) + custo_adicional

# Imprimir o valor total a pagar 
print(f"Total a pagar: R${total:.2f}")