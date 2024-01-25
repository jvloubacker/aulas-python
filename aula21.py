def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False

n = int(input('digite um número: '))
print(par(n))