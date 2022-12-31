def calcula_porcentagem_sorteio(assinante,minutos_assistidos):
    fator_de_assinatura = []
    horas = []
    resultado = []
    for i in assinante:
        if i == True:
            fator_de_assinatura.append(2)
        else:
            fator_de_assinatura.append(1)
    for i in minutos_assistidos:
        if i % 60 == 0:
            n = int(i/60)
            horas.append(n)
        else:
            n = int(i/60 + 1)
            horas.append(n)
    produto = [x*y for x,y in zip(fator_de_assinatura,horas)]
    soma = sum(produto)
    for i in produto:
        x = round(( i / soma ) * 100)
        resultado.append(x)
    return resultado
    

# o código receberá duas listas distintas com os dados necessários
# a primeira lista terá valores booleanos para assinantes da plataforma em questão
# a segunda lista trará os tempos de cada indivíduo, respeitando a ordem da lista anterior
# o código precisa identificar os valores 'True' na primeira lista para dobrar as chances no sorteio.
# o código precisa encontrar o valor inteiro arredondado para cima para o tempo assistido pelos indivíduos.
# o código precisa dobrar os valores da segunda lista de acordo com a primeira.
# o código precisa calcular a probabilidade de cada indivíduo ganhar o sorteio em percentual.
# o código precisa retornar a probabilidade ao final do código.


print(calcula_porcentagem_sorteio([True,False],[60,120]))
print(' o resultado esperado é: [50,50]')

print(calcula_porcentagem_sorteio([True, False, False],[51,60,60]))
print(' o resultado esperado é: [50,25,25]')