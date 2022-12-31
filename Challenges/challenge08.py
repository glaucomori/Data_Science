def escolhe_taxi(tf1,vqr1,tf2,vqr2):
    a = float(tf1)
    b = float(vqr1)
    c = float(tf2)
    d = float(vqr2)
    if a == c and b == d:
        return 'Tanto faz'
    elif a == c and b < d:
        return 'Empresa 1'
    elif a == c and b > d:
        return 'Empresa 2'
    elif a < c and b == d:
        return 'Empresa 1'
    elif a > c and b == d:
        return 'Empresa 2'
    elif a < c and b < d:
        return 'Empresa 1'
    elif a > c and b > d:
        return 'Empresa 2'
    else:
        N = ( c - a ) / (b - d)
        N = float(N)
        if N < 0:
            N = N * (-1)
        else:
            N = N
        if a < c:
            Xpto = '1'
            Ypto = '2'
        else:
            Xpto = '2'
            Ypto = '1'
        resultado = f'Empresa {Xpto} quando a distância < {N:.1f}, Tanto faz quando a distância = {N:.1f}, Empresa {Ypto} quando a distância > {N:.1f}'
        return resultado

# o programa receberá quatro valores em string e se referem respectivamente a:
# tarifa fixa da empresa 1 (TF1), valor por quilômetro rodado da empresa 1 (VQR1),
# tarifa fixa da empresa 2 (TF2), valor por quilômetro rodado da empresa 2 (VQR2).
# o programa deve calcular qual empresa é mais barata para viajar
# se os valores da empresa 1 foram iguais aos respectivos valores da empresa 2 = 'Tanto faz'
# se os valores fixos forem iguais, mas os valores por quilômetro rodado diferirem = 'Empresa X'
# onde o X é a empresa com menor valor por quilômetro rodado
# se os valores por quilômetro rodado forem iguais e os valores fixos diferirem = "Empresa Y"
# onde o Y é a empresa com menor valor fixo
# se todos os valores diferirem >> então é necessário fazer mais outras considerações:
# 1- se ambos os valores da empresa 1 forem respectivamente menores que os da empresa 2 = 'Empresa 1'
# 2- se ambos os valores da empresa 2 forem respectivamente menores que os da empresa 1 = 'Empresa 2'
# 3- calcular a raiz da equação >> TF1 + VQR1 * x = TF2 + VQR2 * x; e a partir dai:
# o valor da raiz comporá o segundo trecho da resposta: 'Tanto faz quando a distância = N,'
# a empresa com menor valor fixo estará presente no primeiro trecho da resposta:
# 'Empresa Xpto quando a distância < N,' e a empresa com maior valor fixo comporá o último trecho:
# 'Empresa Ypto quando a distância > N'
#  retornar o resultado ao final da função


print(escolhe_taxi("2.5","1.0","5.0","0.75"))
print('o resultado esperado é: "Empresa 1 quando a distância < 10.0, Tanto faz quando a distância = 10.0, Empresa 2 quando a distância > 10.0"')

print(escolhe_taxi("2","2","2","2"))
print('o resultado esperado é: "Tanto faz"')

print(escolhe_taxi("5","1","5","1"))
print('o resultado esperado é: "Tanto faz"')

print(escolhe_taxi("2","1","2","2"))
print('o resultado esperado é: "Empresa 1"')

print(escolhe_taxi("5","2","5","1"))
print('o resultado esperado é: "Empresa 2"')

print(escolhe_taxi("4","1","5","1"))
print('o resultado esperado é: "Empresa 1"')

print(escolhe_taxi("5","1","4","1"))
print('o resultado esperado é: "Empresa 2"')

print(escolhe_taxi("5.0","1.5","2.5","0.5"))
print('o resultado esperado é: "Empresa 2 quando a distância < 2.5, Tanto faz quando a distância = 2.5, Empresa 1 quando a distância > 2.5"')

# x = ( c - a ) / (b - d)