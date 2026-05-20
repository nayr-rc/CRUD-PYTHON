import json

def linha():
    print("-="*30)
    
    
def carregar_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            return json.load(arquivo)
    except:
        return []

def salvar_json(nome_arquivo, dados):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print("Banco Atualizado!")