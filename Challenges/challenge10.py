def shuffle_musicas(musicas_tocadas):
    lista_de_musicas = []
    lista_ordenada = sorted(musicas_tocadas)
    for i in range(len(lista_ordenada)):
        u = lista_ordenada[-1]
        lista_de_musicas.append(u)
        lista_ordenada.pop()
        lista_ordenada.reverse()
    
    return lista_de_musicas

# o código receberá uma lista com valores aleatório
# o retorno deve ser uma lista com os mesmos valores, porém ordenados de forma diferente
# a lista deve começar com o maior dos valores e depois o menor dos valores
# a seguir virá o segundo maior valor e depois o segundo menor
# seguindo assim até o fim da lista
# o código irá ordenar a lista de forma crescente, retornar o último valor (que seria o maior)
# e remove-lo da lista. Depois irá reverter a ordem da lista resultante e retornar o último valor
# que agora é o primeiro, já que foi invertida e o valor é removido da lista.
# Esse processo continua até o fim da lista.
# Os valores removidos serão adicionados na lista que será retornada ao final da função
# 
# pop
# reverse
#  

print(shuffle_musicas([2,10,5,3]))
print('o resultado esperado é: [10,2,5,3]')

print(shuffle_musicas([2,10,5,30]))
print('o resultado esperado é: [30,2,10,5]')

print(shuffle_musicas([1,2,3,4]))
print('o resultado esperado é: [4,1,3,2]')

print(shuffle_musicas([1,2,3,4,5,6,7,8,9]))
print('o resultado esperado é: [9,1,8,2,7,3,6,4,5]')

print(shuffle_musicas([1,2,3,7,8,9,0,4,5,6]))
print('o resultado esperado é: [9,0,8,1,7,2,6,3,5,4]')