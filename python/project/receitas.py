import time
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


def soma_das_receitas(receitas):
    total = 0
    for receita in receitas:  
        total+= receita["receita"]
    return total 