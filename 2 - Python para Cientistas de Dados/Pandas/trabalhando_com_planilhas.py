import pandas as pd
#as pd foi incluido apenas para facilitar durante a programação para não precisar digitar
#pandas todas as vezes, assim digitamos pd no lugar de pandas
#pandas.read_excel("endereço da planilha") ou pd.read_excel("endereço da planilha") se tiver colocado as pd depois
#de import pandas
#pandas.concat([variáveis das planilhas]) >> concatena as planilhas. Importante terem a mesma estrutura.
df = pd.read_excel("templates/UF.xlsx")

print(df.head())

# método .head() >> nos mostra as 5 primeiras linhas da tabela, e dentro do parênteses podemos colocar a qtde de linhas
# método .tail() >> é o oposto do método .head(), mostrando as linhas ao final da tabela
# método .dtypes >> retorna os typos de dados em cada coluna da tabela
# método .astype("novo tipo") >> altera o tipo da coluna. Ex.: tabela[coluna] = tabela[coluna].astype("novo tipo")
# método .sample("qtde de linhas") >> retorna uma amostra com linhas randômicas
# método .mean() >> retorna a média dos valores
# método .sum() >> retorna a soma dos valores
# método .max() >> retorna o maior valor
# método .min() >> retorna o menor valor
# método .nlargest("qtde de linhas", "coluna") >> retorna as linas com os maiores valores de acordo com os argumentos
# método .nsmallest("qtde de linhas", "coluna") >> retorna as linas com os menores valores de acordo com os argumentos
# método .groupby("por qual coluna será agrupado")["quais valores serão agrupados"] >> agrupa linhas e valores
# método .sort_values("por qual coluna", ascending=False) >> ordena a tabela de acordo com os argumentos
# método .value_counts() >> retorna a contagem de valores respeitando os argumentos entre parênteses
# método .shape >> retorna a quantidade de linhas e colunas
# método .options.display.float_format = '{:20,.2f}'.format >> para configurar a exibição dos números do tipo float

######################## Valores Faltantes ########################

#tabela.isnull().sum() >> irá somar a quantidade de itens nulos em cada coliuna da tabela

# na linha de código >> df["UF"].fillna(df["UF"].mean(), inplace=True)
# .fillna() é o método que irá completar os valores em brancos pelo argumento desse método
# .mean() é o método que retorna a média
# inplace=True >> quer dizer que a alteração ocorrerá no arquivo em memória

# na linha de código >> df["UF"].fillna(0, inplace=True)
# foi feito o mesmo processo que o bloco superior, porém substituiu os valores por zero

# na linha de código >> df["UF"].dropna(inplace=True)
# .dropna() é o método que irá excluir a linha com algum dado nulo.
# caso queira especificar qual coluna deve ser condiderada devemos preencher da seguinte forma:
# df["UF"].dropna(subset=["coluna"], inplace=True)
# e caso queira remover linhas que tenham valores faltantes em todas as colunas devemos preencher assim:
# df["UF"].dropna(how="all", inplace=True)


######################## Criando colunas novas ########################
# tabela["nova coluna"] = "colocar como será calculada a nova coluna"
# tabela["nova coluna"] = tabela["coluna1"].mul(tabela["coluna2"]) >> nesse caso é o produto das colunas
# tabela["nova coluna"] = tabela["coluna1"] / tabela["coluna2"] >> nesse caso é a diferênça das colunas


######################## Trabalhando com datas ########################
# tabela["nome da coluna de data"] = pandas.to.datetime(tabela["nome da coluna de data"]) >> passar uma coluna
# para o formato de data.
# tabela.groupby(tabela["nome da coluna de data"].dt.year)["coluna com os valores que serão agrupados"].sum()
# tabela["nome da coluna de data"].dt.year >> extrai o ano do dado na coluna de data
# tabela["nome da coluna de data"].dt.quarter >> extrai o trimestre do dado na coluna de data
# tabela["nome da coluna de data"].dt.month >> extrai o mês do dado na coluna de data
# tabela["nome da coluna de data"].dt.day >> extrai o dia do dado na coluna de data
# para datas o método .min() retorna a data mais antiga e o método .max() a mauis recente


######################## Visualização de dados ########################
# método .plot() >> retorna um gráfico de linhas
# método .plot.barh() >> retorna um gráfico de barras horizontais
# método .plot.bar() >> retorna um gráfico de barras verticais
# exemplo:      tabela["coluna"].value_counts(ascending=True).plot.bar();
# método .plot.pie() >> retorna um gráfico de pizza
## para criar gráficos personalizando títulos e eixos precisamos importar uma biblioteca primeiro:
### import matplotlib.pyplot
### tabela["coluna"].value_counts(ascending=True).plot.bar(title="Nome do Título do Gráfico")
### matplotlib.pyplot.xlabel("nome do eixo x")
### matplotlib.pyplot.ylabel("nome do eixo y")
### matplotlib.pyplot.legend()
### alterar o estilo do gráfico >> primeiro consultar nas opções disponíveis na biblioteca matplotlib no site deles
### matplotlib.pyplot.style.use("nome do estilo")
### matplotlib.pyplot.hist() >> histograma
### matplotlib.pyplot.scatter(x = "", y = " ") >> gráfico de dispersão
### matplotlib.pyplot.title() >> título do gráfico
### matplotlib.pyplot.savefig("nome do arquivo.formato do arquivo") >> salvar imagem do gráfico.
### método .xticks(rotation="horizontal") >> mudar a rotação do eixo x no gráfico