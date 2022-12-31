valores = input().split() 

total_hotdogs = int(valores[0])
total_participantes = int(valores[1])
media = total_hotdogs / total_participantes
print(f'{media:.2f}')