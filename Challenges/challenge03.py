from itertools import count

def calcula_senha(senha):
    code = []
    for i in senha:
        countzero = i.count('0')
        countone = i.count('1')
        if countone < countzero:
            code.append(0)
        else:
            code.append(1)
    finalstring = str(code[0]) + str(code[1]) + str(code[2]) + str(code[3]) + str(code[4]) + str(code[5]) + str(code[6]) + str(code[7]) + str(code[8]) + str(code[9])
    finalnumber = int(finalstring, base=2)
    return finalnumber


def calcula_numero_da_senha(senha):
    valor = ['0','0','0','0','0','0','0','0','0','0']
    for i in range(10):
        no0 = senha[0][i]
        no1 = senha[1][i]
        no2 = senha[2][i]
        no3 = senha[3][i]
        no4 = senha[4][i]
        no5 = senha[5][i]
        no6 = senha[6][i]
        no7 = senha[7][i]
        no8 = senha[8][i]
        no9 = senha[9][i]
        valor[i] = str(no0) + str(no1) + str(no2) + str(no3) + str(no4) + str(no5) + str(no6) + str(no7) + str(no8) + str(no9)
    final = [valor[0],valor[1],valor[2],valor[3],valor[4],valor[5],valor[6],valor[7],valor[8],valor[9]]
    return calcula_senha(final)



print(calcula_numero_da_senha(["0110100000","1001011111","1110001010","0111010101","0011100110","1010011001","1101100100","1011010100","1001100111","1000011000"]))
print('o resultado esperado é 724')