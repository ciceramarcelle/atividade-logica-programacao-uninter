# exigencia - Boas-vindas com meu nome
print("Bem-vindo a Loja da Cícera Marcelle de Melo Ferreira!")

# exigencia - Input do valor unitário e quantidade do produto
valor_unitario = float(input("Valor unitário do produto: "))
quantidade = int(input("Quantidade do produto: "))

# Valor SEM desconto
valor_total_sem_desconto = valor_unitario * quantidade

# Descontos conforme solicitado com as condições if, elif e else
if valor_total_sem_desconto < 2500:
    desconto = 0 #se valor for menor que 2500 o desconto será de 0%;
elif valor_total_sem_desconto < 6000:
    desconto = 0.04  # se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%;
elif valor_total_sem_desconto < 10000:
    desconto = 0.07  # se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%;
else:
    desconto = 0.11  # se valor for igual ou maior que 10000 o desconto será de 11%;

# Cálculo valor COM desconto
valor_total_com_desconto = valor_total_sem_desconto - (valor_total_sem_desconto * desconto)

# Saída do console
print(f"Valor total SEM desconto é: R$ {valor_total_sem_desconto}")
print(f"Valor total COM desconto é: R$ {valor_total_com_desconto}")