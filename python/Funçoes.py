import json
import time

def linha():
    print("-="*30)

def cadastrar_livro(livros):
    dic = {}
    maior_id = 0
    titulo = input("Digite o titulo do livro que voce quer adicionar. ").capitalize().strip()
    dic["titulo"] = titulo
    while titulo == "":
        titulo = input("Digite o titulo do livro que voce quer adicionar. ").capitalize().strip()
    for livro in livros:
        if titulo == livro["titulo"]:
            print("livro já adicionado")
            return   
    autor = input("Digite o autor do livro ").capitalize().strip()
    dic["autor"] = autor
    for livro in livros:
        if maior_id < livro["id"]:
            maior_id = livro["id"]
    
    dic["id"] = maior_id + 1
        
    livros.append(dic)
    print("Livro Adicionado!")

    
def listar_livros(livros):
        encontrado = False
        lista_ordenada = sorted (livros, key = lambda livro: livro["id"]) # isso aqui (lambda) é uma função compacta que retorna o que está depois dos dois pontos quando voce chama o parametro
        for livro in lista_ordenada:
            print (f"Titulo:{livro['titulo']}")
            print(f"Autor:{livro['autor']}")
            print(f"ID:{livro['id']}")
            encontrado = True  
        if not encontrado:
            print("Nao existem livros na base de dados")
    
def remover_livro(livros):
    encontrado = False
    try:
        remoc= int(input("Digite o ID do livro a ser removido: "))
    except:
        print("Digite apenas numeros")
        return
    for livro in livros:
            if remoc == livro["id"]:
                conf = input(f"Tem certeza que deseja remover o livro {livro['titulo']}? (s/n) ").lower()
                if conf == "s":
                    livros.remove(livro)
                    print("Removendo livro...")
                    time.sleep(3)
                    print("Livro Removido")
                    encontrado = True
                else:
                    print("Operação cancelada")
                    return
    if not encontrado:
            print("livro nao encontrado")

def editar_livro(livros):
        try:
            edit = int(input("Digite o ID do livro que voce quer editar: "))
        except:
            print("Digite apenas numeros.")
            return
        encontrado = False
        for livro in livros:
            if edit == livro["id"]:
                print("Livro Encontrado")
                quest = input("qual o nome do novo livro? ").capitalize()
                livro["titulo"] = quest
                autor = input("Qual o nome do autor? ").capitalize()
                livro["autor"] = autor
                encontrado = True
            
        if not encontrado :
                print("Livro nao encontrado")

def salvar_livros(livros):
    with open("livros.json", "w") as arquivo:
        json.dump(livros, arquivo , indent=4, ensure_ascii=False)
        print("Banco Atualizado!")
        
def buscar_livro(livros):
    busca = input("Digite o nome do livro que voce deseja buscar: ").capitalize()
    encontrado = False
    for livro in livros :
        if busca == livro["titulo"]:
            print("Buscando livro...")
            time.sleep(2)
            print (f"Titulo:{livro['titulo']}")
            print(f"Autor:{livro['autor']}")
            encontrado = True
    if not encontrado:
        print("livro nao encontrado.")

def carregar_livros():
    try:
        with open ("livros.json", "r" ) as arquivo:
            return json.load(arquivo)
    except:
        return []

def menu(livros):
    linha()
    print("Bem Vindo a Biblioteca Virtual")
    print("Digite 1 para cadastrar um livro")
    print("Digite 2 para listar os livros")
    print("Digite 3 para sair do programa")
    print("Digite 4 para remover um livro")
    print("Digite 5 para editar um livro")
    print("Digite 6 para buscar um livro")
    linha()
    try:
        pergunta = int(input("Digite a opção desejada: "))
    except:
        print("Digite apenas números")
        return 
    return pergunta

livros = carregar_livros() 
while True:
    opçao = menu(livros)
    if opçao == 1:
            cadastrar_livro(livros)
            salvar_livros(livros)
    elif opçao == 2:
            listar_livros(livros)
    elif opçao  == 3:
            print("Saindo do programa...")
            time.sleep(2)
            exit()
    elif opçao == 4:
            remover_livro(livros)
            salvar_livros(livros)
    elif opçao == 5:
            editar_livro(livros)
            salvar_livros(livros)
    elif opçao == 6:
            buscar_livro(livros)
    else:
            print("Digite um numero valido")   


