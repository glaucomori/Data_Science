def calcula_total_leds(altura,largura):
    if altura == 0 or largura == 0:
        return 0
    else:
        quantidade_leds = (altura + 1) * (largura + 1)
        return quantidade_leds

# o programa recebe dois valores inteiros
# esse valores se referem ao tamanho, em cm, de um painel de led montado em quadrados de 1cm de lado
# esse painel recebe um led em cada vertice de quadrado
# num quadrado de 1 x 1 = tem-se 4 leds (4 = 2 x 2)
# num quadrado de 2 x 4 = tem-se 15 leds (15 = 3 x 5)
# então devemos incrementar cada uma das dimensês em 1
# e depois multiplicar o valor das duas dimensões incrementadas
# e retornar o valor ao final da função

print(calcula_total_leds(2,3))
print('o resultado esperado é: 12')

print(calcula_total_leds(1,1))
print('o resultado esperado é: 4')

print(calcula_total_leds(2,4))
print('o resultado esperado é: 15')