import random
entrada = input('Faça uma pergunta, que a resposta seja sim ou não: ')
respostas = ['Sim', 'Óbvio', 'Não', 'Talvez', 'Não tenho certeza']
ale = random.choices(respostas)
print(f'A resposta é: {ale}')
