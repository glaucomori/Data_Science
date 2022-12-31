def menor_string_maior(name):
    name_list_str = list(name)
    name_list_number = []
    name_list = []
    for i in range(len(name_list_str)):
        number = name_list_str[i]
        number = ord(number)
        name_list_number.append(number) # até aqui está tudo bem
    
    limite_contador = (-1)*(len(name_list_str))
    contador = -1
    while contador >= limite_contador:
        count = -1
        antecessor = contador -1
        if name_list_number[count] > name_list_number[antecessor]:
            temp = name_list_number[count]
            name_list_number[count] = name_list_number[antecessor]
            name_list_number[antecessor] = temp
            for i in range(len(name_list_number)):
                number = name_list_number[i]
                number = chr(number)
                name_list.append(number)
                result = ''.join(name_list)            
            return result
        else:
            return 'sem resposta'


# o código receberá uma string e precisará retornar a primeira string maior do que a recebida
# como a ordem é a alfabética, pode-se usar a função ord(letra) para retornar o valor na tabel ASCII
# o codigo precisa separar a string nas suas letras para poder usar como número
# ele irá comparar o último algarismo(posição -1) com o seu antecessor(posição -2), 
# e se for maior, deverá trocar. Mas se não for maior, devera comparar esse ultimo número
# com o numero antecessor ao antecessor (posição -3). Nesse caso onde a comparação não foi verdadeira
# o contador de posicão reduziu em 1. Deve-se realizar comparações recursivamente até o final da sequencia,
# caso a comparação seja verdadeira os algarismos comparados devem trocar de lugar e após isso
# os algarismos nas posições posteriores devem ser ordenados crescentemente e a função retornará esse valor
# se após percorrer toda a sequencia e não conseguir achar uma comparação verdadeira, todo o processo
# deverá reiniciar, porém agora comparando o segundo algarismo (posição -2) com o seu antecessor 
# (posição -3) e remoçar a recursividade novamente. Caso os algarismos se esgotem e não tenham chegado a
# uma comparação verdadeira, a função retornará 'sem resposta'.

print(menor_string_maior('ab'))
print('o resultado esperado é: "ba"')

print(menor_string_maior("abcde"))
print('o resultado esperado é: "abced"')

print(menor_string_maior('ba'))
print('o resultado esperado é: “sem resposta"')