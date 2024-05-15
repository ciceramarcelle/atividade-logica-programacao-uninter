# Variável global para o ID dos livros - exigencia de id_global
id_global = 0 

# Lista para armazenar os livros e cada livro é um dicionário - exigencia de lista_livro
lista_livro = [] 

# Função para cadastrar um livro - exigencia 3 
def cadastrar_livro():
    global id_global 
    id_global += 1
    print(f'Id do livro: {id_global}')
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")
    #criação de dicionário q representa o livro e adiciona à lista de livros- exigencia 7
    livro = {'id': id_global,
             'nome': nome,
             'autor': autor,
             'editora': editora}
    lista_livro.append(livro) #adiciona o livro à lista de livros
    print("Livro adicionado com sucesso.")

# Função para consultar os livros - exigencia 4
def consultar_livro(): 
    while True: #loop pra continuar ate que o usuário queira sair
        print("\nEscolha a opção desejada:")
        print("1. Consultar Todos")
        print("2. Consultar por ID")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")

        opcao = input() #pra solicitar a opçao ao usuario

        if opcao == '1':
            consultar_todos()
        elif opcao == '2':
            consultar_por_id()
        elif opcao == '3':
            consultar_por_autor()
        elif opcao == '4':
            return
        else:
            print("Opção inválida")

#funçao pra consultar TODOS os livros e imprimir 

def consultar_todos():
    print("Lista de todos os livros:")
    for livro in lista_livro: 
        #pra imprimir os detalhes do livro - ID, NOME, AUTOR, EDITORA
        print(f"ID: {livro['id']}")
        print(f"Nome: {livro['nome']}")
        print(f"Autor: {livro['autor']}")
        print(f"Editora: {livro['editora']}")
        print()  # pra adicionar uma linha em branco entre os livros - sem isso tava dando erro

#funçao pra consultar livro por ID e imprimir

def consultar_por_id():
    id_livro = int(input("Digite o ID do livro: ")) # solicita o ID do livro ao usuário
    for livro in lista_livro:
        if livro['id'] == id_livro: # se o ID do livro corresponder ao ID fornecido pelo usuário
            print("Detalhes do livro:")
            print(f"ID: {livro['id']}")
            print(f"Nome: {livro['nome']}")
            print(f"Autor: {livro['autor']}")
            print(f"Editora: {livro['editora']}")
            return # Retorna após encontrar o livro desejado
    print("Livro não encontrado.")

#funçao pra consultar livros por autor e imprimir

def consultar_por_autor():
    autor = input("Digite o nome do autor: ") # solicita o nome do autor ao usuário
    print(f"Lista de livros do autor {autor}:")
    for livro in lista_livro:
        if livro['autor'] == autor:
            print("Detalhes do livro:")
            print(f"ID: {livro['id']}")
            print(f"Nome: {livro['nome']}")
            print(f"Autor: {livro['autor']}")
            print(f"Editora: {livro['editora']}")
            print()  

# Função para remover um livro - exigencia 5
def remover_livro():
    id_remover = int(input("Digite o ID do livro a ser removido: "))
    encontrado = False
    for livro in lista_livro:
        if livro['id'] == id_remover: # se o ID do livro for igual ao ID fornecido pelo usuário
            lista_livro.remove(livro) # remove o livro da lista de livros
            print("Livro removido com sucesso.")
            encontrado = True # livro como encontrado
            break # sai do loop APÓS remover o livro
    if not encontrado: 
        print("ID inválido.")

# Menu principal main - exigencia 6
def menu():
    print("Bem-vindo(a) a Livraria da Cicera!") #Exigencia 1 - boas vindas com meu nome
    while True:
        print("\nEscolha a opção desejada:")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Encerrar Programa")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            consultar_livro()
        elif opcao == '3':
            remover_livro()
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__": # executa o código
    menu() # chama a função MENU para iniciar o programa