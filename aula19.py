nome = dict()
dados = list()
for c in range(0,2):
    nome['nome'] = str(input("Digite seu nome: "))
    nome['idade'] = int(input("Digite sua idade: "))
    dados.append(nome.copy())
for n in dados:
    for k, v in n.items():
        print(f'{k} tem valor {v}')