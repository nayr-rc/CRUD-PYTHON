
from receitas import *
from despesas import *
from utils import *

def mostrar_saldo(receitas, despesas):
    total_receitas = soma_das_receitas(receitas)
    total_despesas = soma_das_despesas(despesas)
    saldo = total_receitas - total_despesas

    print(f"Saldo atual: R${saldo:.2f}")

def relatorio_financeiro(receitas, despesas):
    total_receitas = soma_das_receitas(receitas)
    total_despesas = soma_das_despesas(despesas)
    saldo = total_receitas - total_despesas

    linha()
    print(f"Receitas totais: R${total_receitas:.2f}")
    print(f"Despesas totais: R${total_despesas:.2f}")
    print(f"Saldo atual: R${saldo:.2f}")
    linha()

def menu():
    linha()

    print("Bem Vindo ao seu relatorio financeiro")
    print("1 - Adicionar receita")
    print("2 - Listar receitas")
    print("3 - Sair")
    print("4 - Remover receita")
    print("5 - Editar receita")
    print("6 - Adicionar despesa")
    print("7 - Mostrar saldo")
    print("8 - Listar despesas")
    print("9 - Remover despesas")
    print("10 - Editar despesas")
    print("11 - Relatorio financeiro")

    linha()

    try:
        return int(input("Digite a opção desejada: "))
    except:
        print("Digite apenas numeros")
        return

receitas = carregar_json("receitas.json")
despesas = carregar_json("despesas.json")

while True:

    opcao = menu()

    if opcao == 1:
        adicionar_receita(receitas)
        salvar_json("receitas.json", receitas)

    elif opcao == 2:
        listar_receitas(receitas)

    elif opcao == 3:
        print("Saindo...")
        break

    elif opcao == 4:
        remover_receitas(receitas)
        salvar_json("receitas.json", receitas)

    elif opcao == 5:
        editar_receita(receitas)
        salvar_json("receitas.json", receitas)

    elif opcao == 6:
        adicionar_despesas(receitas, despesas)
        salvar_json("despesas.json", despesas)

    elif opcao == 7:
        mostrar_saldo(receitas, despesas)

    elif opcao == 8:
        listar_despesas(despesas)

    elif opcao == 9:
        remover_despesas(despesas)
        salvar_json("despesas.json", despesas)

    elif opcao == 10:
        editar_despesa(despesas)
        salvar_json("despesas.json", despesas)

    elif opcao == 11:
        relatorio_financeiro(receitas, despesas)

    else:
        print("Opção inválida")