itens = []

print("Digite até 3 itens para a lista (pressione Enter após cada item).")

for i in range(3):
    item = input(f"Item {i+1}: ")
    itens.append(item)
    

print("Itens da lista:", itens)