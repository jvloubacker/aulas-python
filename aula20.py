def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1


#programa principal
valores=[6,10,2,0,4]
dobra(valores)
print(valores)