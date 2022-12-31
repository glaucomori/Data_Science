valores = input().split()

tempo = int(valores[0])
velocidade = int(valores[1])
consumo = (tempo * velocidade)/12
print(f'{consumo:.3f}')