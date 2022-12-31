def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# os parâmetros somente por nome são os que vêm após o asterisco "*" na lista de parâmetros de uma função.
# os parâmetros que ficam antes do asterisco "*" não são influenciados por essa obrigação de passar por nome.

# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido