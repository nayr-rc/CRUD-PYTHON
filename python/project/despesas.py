def adicionar_despesas(receitas ,  despesas):
    desp={}
    
    maior_id = 0
    try:
        despesa = int(input("Digite o valor da Despesa: "))
        desp["despesa"] = despesa
    except:
        print("Digite apenas numeros.")
        return
    descricao = input("Qual a descriçao da despesa (de onde veio?)").capitalize().strip()
    desp["descricao"] = descricao
    for despesa in despesas:
            if maior_id < despesa["id"]:
                maior_id = despesa["id"]
    desp["id"] = maior_id + 1
        
    despesas.append(desp)
    print("Valor Adicionado!")


def listar_despesas(despesas):
    encontrado = False
    lista_ordenada = sorted(despesas, key= lambda despesa: despesa["id"])
    for despesa in lista_ordenada:
            print (f"Valor: {despesa['despesa']:.2f}")
            print(f"Descrição: {despesa['descricao']}")
            print(f"ID: {despesa['id']}")
            encontrado = True  
    if not encontrado :
            print("Dado nao encontrado na base de dados")



def remover_despesas(despesas):
    encontrado = False
    
    try:
            remoc = int(input("Digite o ID da despesa que voce quer fazer a retirada: "))
    except:
            print("Digite apenas numeros")
            return
    for despesa in despesas:
            if remoc == despesa["id"]:
                conf = input(f"Tem certeza que deseja remover {despesa['descricao']}? (s/n) ").lower().strip()
                if conf == "s":
                    despesas.remove(despesa)
                    print("Removendo despesa...")
                    time.sleep(3)
                    print("Despesa Removida")
                    encontrado = True
                else:
                    print("Operação cancelada")
                    return
    if not encontrado:
            print("Despesa nao encontrada")



def editar_despesa(despesas):
    try:
        edit = int(input("Digite o ID da despesa que voce deseja editar: "))
    except:
        print("Digite apenas numeros ")
        return
    encontrado = False
    for despesa in despesas:
        if edit == despesa["id"]:
            print("Despesa encontrada!")
            quest = int(input("Qual o novo valor? "))
            despesa["despesa"] = quest
            quest2 = input("Digite a descriçao: ").strip()
            despesa["descricao"] = quest2
            encontrado = True
    if not encontrado:
            print("Despesa nao encontrada. ")



def soma_das_despesas(despesas):
    total = 0 
    for despesa in despesas :
        total  += despesa["despesa"]
    return total


