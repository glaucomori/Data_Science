def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# os parâmetros somente por posição são os que vêm antes da barra "/" na lista de parâmetros de uma função.
# os parâmetros que ficam após a barra "/" não são influenciados por essa obrigação de passar por posição.

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # válido
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido