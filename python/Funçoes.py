import json




def cadastrar_livro(livros):
    dic = {}
    titulo = input("Digite o titulo do livro que voce quer adicionar. ").capitalize()
    dic["titulo"] = titulo
    autor = input("Digite o autor do livro ").capitalize()
    dic["autor"] = autor
    livros.append(dic)
    print("Livro Adicionado!")

    
def listar_livros(livros):
        encontrado = False
        for livro in livros:
            print (f"Titulo:{livro['titulo']}")
            print(f"Autor:{livro['autor']}")
            encontrado = True
        if not encontrado:
            print("Nao existem livros na base de dados")
    
def remover_livro(livros):
    encontrado = False
    remoc = input("Digite o nome do livro a ser removido: ").capitalize()
    for livro in livros:
        if remoc == livro["titulo"]:
            livros.remove(livro)
            print("Livro Removido")
            encontrado = True
    if not encontrado:
            print("livro nao encontrado")

def editar_livro(livros):
    edit = (input("Qual livro voce quer editar?")).capitalize()
    encontrado = False
    for livro in livros:
        if edit == livro["titulo"]:
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
        print("Livro Salvo!")
        
def buscar_livro(livros):
    busca = input("Digite o nome do livro que voce deseja buscar: ").capitalize()
    encontrado = False
    for livro in livros :
        if busca == livro["titulo"]:
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

    

livros = carregar_livros()           

while True:
    try:
        perg = int(input("Digite 1 para cadastro, 2 para listar livros, 3 para sair, 4 para remover livro, 5 para editar o livro, 6 para buscar livro: "))
    except:
        print("Digite apenas números ")
        continue
    if perg == 1:
        print("-"*30)
        cadastrar_livro(livros)
        print("-"*30)
        salvar_livros(livros)
    elif perg == 2:
        print("-"*30)
        listar_livros(livros)
        print("-"*30)
    elif perg == 4:
        print("-"*30)
        remover_livro(livros)
        salvar_livros(livros)
        print("-"*30)
    elif perg == 5:
        print("-"*30)
        editar_livro(livros)
        salvar_livros(livros)
        print("-"*30)
    elif perg == 6:
        print("-"*30)
        buscar_livro(livros)    
        print("-"*30)
    elif perg == 3:
        break
    else:
        print("opçao inválida")
