dic = {
  #nome_plano  #dados
    "plano1" : [100, 80],
    "plano2" : [200, 90],
    "plano3" : [300, 100],
    "plano4" : [500, 130],
    "plano5" : [1000, 160]
}

def planos_disponiveis(usado):
    
    for nome_plano, dados in dic.items():
        limite = dados[0]
        preco_base = dados[1]
        
        print(f"{nome_plano.upper()}")
        print(f"Capacidade: {limite} MB | Valor Base: R${preco_base}")

        if usado > limite:
            excedente = usado - limite
            taxa_extra = excedente * 0.15
            total = preco_base + taxa_extra
            print(f"Status: Excedeu {excedente} MB.")
            print(f"Valor extra: R${taxa_extra:.2f} | Total: R${total:.2f}")
        else:
            print(f"Status: Dentro do limite. Total: R${preco_base:.2f}")
        print("-" * 20)
    
final = planos_disponiveis(500)
print(final)