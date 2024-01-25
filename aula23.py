try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'O erro encontrado foi o {erro.__cause__}, {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por 0')
except KeyboardInterrupt:
    print('\nO usuário decidiu não informar um número')
else:
    print(f'O resultado é {r}')
finally:
    print(f'MUITO OBRIGADO! VOLTE SEMPRE!')
