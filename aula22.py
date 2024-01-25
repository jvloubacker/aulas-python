#AULA 22   MODULOS E PACOTES
# * aumentar a legibilidade , dividir os programas grandes, foco: facil manutenção

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f*=c
    return f

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
