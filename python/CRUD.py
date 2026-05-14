pessoas = []
encontrado = False
for _ in range(3):
    pessoa = {}
    nome = (input("Digite o Nome :")).lower()
    pessoa["nome"] = nome
    idade = int(input("Digite a Idade : "))
    pessoa["idade"] = idade
    cidade = input("Digite a cidade : ").lower()
    pessoa["cidade"] = cidade
    pessoas.append(pessoa)

while True:
    encontrado = False
    
  
    decider = int(input("Você quer consultar alguem da lista ou remover?( 1. para consulta 2, para remoçao, 3 para sair, 4 para listar) "))

    if decider == 1:
            quest = (input("Quem voce quer consultar?")).lower()
            for pessoa in pessoas:
                if quest == pessoa["nome"]:
                    print(pessoa["nome"])
                    print(pessoa["idade"])
                    print(pessoa["cidade"])
                    encontrado = True
    elif decider == 3:
        break

    elif decider == 2:
            remoc = input("Digite o nome de quem voce quer remover os dados.").lower()
            for pessoa in pessoas:
                if remoc == pessoa["nome"]:
                    pessoas.remove(pessoa)
                    encontrado = True
                    print("Dados removidos com sucesso.")
    elif decider == 4:
        for pessoa in pessoas:
            print("Nome:",pessoa["nome"])
            print("Idade:",pessoa["idade"])
            print("Cidade:",pessoa["cidade"])
            
    else:
        print("opçao invalida")
        
    
        if not encontrado:
            print("Essa pessoa nao consta em nosso banco de dados")
                    
