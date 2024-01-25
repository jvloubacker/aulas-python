nome = str(input('Escreva o seu nome: '))

if nome == 'João Vitor':
    print("Que nome lindo!")

elif nome == 'José' or nome == 'Maria' or nome == 'Pedro':
    print(f"O seu nome é normal no Brasil!")

else:
    print("Seu nome é bem comum!")
print(f"Tenha um ótimo dia, {nome}!")