def calcula_top_ocorrencias_de_queries(texto,queries,k):
    string = texto
    matrixresult = []
    listresult = []
    for i in queries:
        n = (string.count(i),i)
        matrixresult.append(n)
    matrixresult_ordered = sorted(matrixresult, reverse = True)
    for j in range(k):
        partial = matrixresult_ordered[j][1]
        listresult.append(partial)
    return listresult

# o código receberá uma string que servirá de base para a contagem das queries.
# o código receberá uma lista com os termos que devem ser contabilizados.
# o código receberá um número inteiro positivo com a quantidade de posições a serem retornadas.
# o código deve atribuir uma variável para a string para poder contar os termos.


print(calcula_top_ocorrencias_de_queries("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",["a","em","i","el"],2))
print('o resultado esperado é: ["i","a"]')