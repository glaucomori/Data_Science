def checa_numero_escondido(numero,numero_oculto):
    num_int1 = numero
    num_str1 = str(num_int1)
    num_list_str1 = list(num_str1)
    num_int2 = numero_oculto
    num_str2 = str(num_int2)
    num_list_str2 = list(num_str2)
    while len(num_list_str1) > 0:
        if len(num_list_str2) == 0: 
            return True
        elif num_list_str1[-1] == num_list_str2[-1]:
            num_list_str1.pop()
            num_list_str2.pop()
        else:
            num_list_str1.pop()
    if len(num_list_str1) == 0 and len(num_list_str2) == 0:
        return True
    else:
        return False


# o código receberá dois números inteiros
# o código precisa verificar se com base no primeiro número e na ordem de seus algarismos
# se o valor do segundo número pode ser elaborado
# o código precisa decompor os números em seus algarismos (pode-se transformar em string e listas)
# o código pegará a primeira lista como base e fará a leitura dos elementos da segunda lista
# ele comparará o primeiro algarismo da primeira com o primeiro da segunda
# caso sejam o mesmo ele remove o algarismos das duas listas e repete o processo anterior
# caso sejam diferentes ele remove o item da primeira lista e repete o processo anterior
# o processo é repitido até a segunda lista ser totalmente percorrida ou até a primeira lista acabar
# se a primeira lista acabar o código deve retornar o resultado 'False'
# se a segunda lista acabar o código deve retornar o resultado 'True'

print(checa_numero_escondido(12345,235))
print('o resultado esperado é: True')

print(checa_numero_escondido(12345,154))
print('o resultado esperado é: False')
