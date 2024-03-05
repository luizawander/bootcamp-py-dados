capacidade_atual, aumento_percentual = map(int, input().split())


capacidade_nova = capacidade_atual + capacidade_atual*aumento_percentual/100

print(f'{capacidade_nova:.0f}')