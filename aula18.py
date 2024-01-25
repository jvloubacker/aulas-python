galera = list()
dados = list()
totmaior = totmenor = 0
for var in range(0,4):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] > 21:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade.')
        totmaior+=1
    else:
        print(f'{p[0]} é de menor.')
        totmenor+=1
print(f'Maior de idade tem {totmaior}.')
print(f'Mneor de idade tem {totmenor}.')