def ultima_parada(combustivel,consumo,postos_de_gasolina):
    postos_de_gasolina_ordenados = sorted(postos_de_gasolina)
    autonomia = combustivel * consumo
    if autonomia < postos_de_gasolina_ordenados[0]:
        return -1
    elif autonomia > postos_de_gasolina_ordenados[-1]:
        return postos_de_gasolina_ordenados[-1]
    else:
        for i in range(len(postos_de_gasolina)):
            if autonomia >= postos_de_gasolina_ordenados[i]:
                continue
            else:
                return postos_de_gasolina_ordenados[i-1]



print(ultima_parada(2,8,[2,15,22,11]))
print('o resultado esperado é: 15')