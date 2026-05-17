import json
import time
def linha():
    print("-="*30)
def adicionar_receita(receitas):
    dic = {}
    maior_id = 0
    
    try:
            adicao = int(input("Digite o valor que foi adicionado:"))
            dic["receita"] = adicao
    except:
            print("Digite Apenas numeros")
            return
    
    descricao = input("Qual a descriçao da receita (de onde veio?)").capitalize().strip()
    dic["descricao"] = descricao
    for receita in receitas:
            if maior_id < receita["id"]:
                maior_id = receita["id"]
    dic["id"] = maior_id + 1
        
    receitas.append(dic)
    print("Valor Adicionado!")
    
def listar_receitas(receitas):
    encontrado = False
    lista_ordenada = sorted(receitas, key= lambda receita: receita["id"])
    for receita in lista_ordenada:
            print (f"Valor: {receita['receita']:.2f}")
            print(f"Descrição: {receita['descricao']}")
            print(f"ID: {receita['id']}")
            encontrado = True  
    if not encontrado :
            print("Dado nao encontrado na base de dados")
            
def carregar_receitas ():
    try:
        with open ("receitas.json", "r" ) as arquivo:
            return json.load(arquivo)
    except:
        return []
def salvar_receitas(receitas):
    with open("receitas.json", "w") as arquivo:
        json.dump(receitas, arquivo , indent=4, ensure_ascii=False)
        print("Banco Atualizado!")
def remover_receitas(receitas):
    encontrado = False
    
    try:
            remoc = int(input("Digite o ID da receita que voce quer fazer a retirada: "))
    except:
            print("Digite apenas numeros")
            return
    for receita in receitas:
            if remoc == receita["id"]:
                conf = input(f"Tem certeza que deseja remover o livro {receita['descricao']}? (s/n) ").lower().strip()
                if conf == "s":
                    receitas.remove(receita)
                    print("Removendo receita...")
                    time.sleep(3)
                    print("Receita Removida")
                    encontrado = True
                else:
                    print("Operação cancelada")
                    return
    if not encontrado:
            print("receita nao encontrada")
def editar_receita(receitas):
    try:
        edit = int(input("Digite o ID da receita que voce deseja editar: "))
    except:
        print("Digite apenas numeros ")
        return
    encontrado = False
    for receita in receitas:
        if edit == receita["id"]:
            print("Receita encontrada!")
            quest = int(input("Qual o novo valor? "))
            receita["receita"] = quest
            quest2 = input("Digite a descriçao: ").strip()
            receita["descricao"] = quest2
            encontrado = True
    if not encontrado:
            print("Receita nao encontrada. ")
    
        

def menu(receitas):
    linha()
    print("Bem Vindo ao seu relatorio de receitas")
    print("Digite 1 para Adicionar uma receita nova")
    print("Digite 2 para listar as receitas")
    print("Digite 3 para sair do programa")
    print("Digite 4 para remover uma receita")
    print("Digite 5 para editar uma receita")
    linha()
    
    try:
        pergunta = int(input("Digite a opção desejada: "))
    except:
        print("Digite apenas números")
        return 
    return pergunta
            
    
receitas = carregar_receitas()

while True:
    opçao = menu(receitas)
    
    if opçao == 1:
        adicionar_receita(receitas)
        salvar_receitas(receitas)
    elif opçao == 2:
        listar_receitas(receitas)
        linha()
    elif opçao == 3:
        break
    elif opçao == 4:
        remover_receitas(receitas)
        salvar_receitas(receitas)
    elif opçao == 5:
        editar_receita(receitas)
        salvar_receitas(receitas)