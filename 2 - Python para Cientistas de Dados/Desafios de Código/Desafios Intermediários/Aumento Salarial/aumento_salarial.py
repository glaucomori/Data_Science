salario = float(input()) 

if ( 0 < salario <= 600 ):
    percentual = 0.17

elif ( 600 < salario <= 900 ):
    percentual = 0.13

elif ( 900 < salario <= 1500 ):
    percentual = 0.12

elif ( 1500 < salario <= 2000 ):
    percentual = 0.10

else: 
    percentual = 0.05

percentual_reajuste = int(percentual * 100)
reajuste = salario * percentual
novo_salario = salario + reajuste
print(f"Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual_reajuste} %")
