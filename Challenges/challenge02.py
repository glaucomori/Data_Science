def retorna_menor_e_maior_valor_de_vendas(tickets):
    final_list = []
    for l in tickets:
            for i in l:
                if i < 20:
                    continue
                elif i > 500:
                    continue
                else:
                    final_list.append(i)
    final_list = [min(final_list),max(final_list)]
    return final_list

# A função precisa receber uma lista com os valores de cada funcionário.
# para cada funcionário presente na lista a função receberá uma outra lista com os valores.
# o programa precisa extrair cada um dos valores para poder compara-los.
# precisa criar uma lista com os novos valores extraidos, para que possam ser comparados.
# precisa determinar qual o menor valor e o maior dentro do limite informado pelo problema.
# limite inferior >> 20
# limite superior >> 500
# adicionar os valores dos limites na nova lista seguindo a orientação do problema >> [menor, maior].
# retornar a lista ao final da execução da função.
# elaborar situações de teste para avaliar o código.

print(retorna_menor_e_maior_valor_de_vendas([[200,100],[300]]))
print('o resultado esperado é: [100,300]')

print(retorna_menor_e_maior_valor_de_vendas([[200,100],[300], [], [45,42]]))
print('o resultado esperado é: [42,300]')

print(retorna_menor_e_maior_valor_de_vendas([[200,100],[300], [0], [1000,1200]]))
print('o resultado esperado é: [100,300]')

print(retorna_menor_e_maior_valor_de_vendas([[200,100],[300], [500,20]]))
print('o resultado esperado é: [20,500]')