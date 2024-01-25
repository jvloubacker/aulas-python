lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita'
print(sorted(lanche))

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")
print('')

for pos, comida in enumerate(lanche):
    print(f"Eu comi {comida} na posição {pos}")
print("COMI PRA CARAMBA!")