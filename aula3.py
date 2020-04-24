# -*- coding: utf-8 -*-
"""QuarentenaDados - Aula04

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_qlF7L09yfrYG_1kV10SQfqvbM-8CYKF

# Introdução


Olá, seja bem-vinda e bem-vindo ao notebook da **aula 04!** A partir desta aula iremos analisar e discutir um *sample* da base de dados do **ENEM 2018**. Nessa aula vamos falar sobre diversos temas importantes na área de IA, então **acompanhar esses explicações pela videoaula será importante para o seu desenvolvimento**.

#Aula 4

Aqui iremos explorar e conhecer uma pequena amostra da base de dados do **ENEM 2018**. Esse será o primeiro passo para construir os **modelos de machine learning da aula 05**. Se você quiser estudar o código utilizado para criar o dataset desta aula, pode acessar este [**link aqui**](https://github.com/guilhermesilveira/enem-2018).

Vamos iniciar setando a precisão de casas decimais que o pandas irá exibir os dados (`pd.options.display.float_format`), depois lendo e conhecendo as informações contidas na base de dados.
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd

# %precision %.2f
pd.options.display.float_format = '{:,.2f}'.format

uri = "https://raw.githubusercontent.com/GuilleAngulo/python-data-science/master/data/enem_sample_2018.csv"
dados = pd.read_csv(uri)
dados.head()

"""Conheça todas as colunas do nosso dataframe:"""

print(dados.columns.values)

"""Na videoaula tivemos uma discussão muito bacana sobre uma visão geral dos dados e sua organização, e sobre ética na IA. Se você não assistiu eu recomendo que veja, não cabe aqui no notebook reproduzir a conversa, então vamos seguir com o  desenvolvimento.


Conhecidas as informações, vamos chamar o **describe()** para analisá-las. Se atente ao detalhe que o **describe** só gera informação de dados numéricos!
"""

dados.describe()

"""A saída do `describe` traz várias estatísticas, de forma que algumas não fazem sentido ou não nos interessam neste momento.  Entretanto, se você analisou as últimas colunas, viu que lá temos alguns dados relevantes: notas das provas e redação. 

Desafio você a entrar nos detalhes das análises de notas e diversos outros campos! Como nosso tempo aqui é restrito, vamos analisar apenas as notas entre si, mas reflita: Será que existe uma correlação entre as notas? Quem tira notas maiores em redação também vai bem em linguagens?

Vamos analisar!
"""

colunas_de_notas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
dados_notas = dados[colunas_de_notas].dropna()
dados_notas.columns = ['ciencias_naturais', 'ciencias_humanas', 'linguagem_codigo', 'matematica', 'redacao']
dados_notas.head()

len(dados_notas)

"""Como queremos analisar as notas detalhadamente, no código acima separamos apenas os dados de interesse. Também removemos todos os valores vazios com o `.dropna()` e trocamos os nomes das colunas para ficar mais legível. 

Por fim, agora nosso DF tem 97270 linhas e 5 colunas.

Agora sim, vamos calcular a correlação usando o `.corr()`:
"""

corr = dados_notas.corr()
corr

"""Temos vários resultados interessantes por aqui: o primeiro é uma correlação considerável entre **linguagem_codigo e ciencias_humanas**, o que parece fazer sentido. Uma correlação que surpreende é entre **linguagem_codigo e redacao**. Embora haja uma correlação maior em relação às outras matérias e redação, eu esperava um valor ainda maior do que o existente. 

**Mais alguma correlação te chama a atenção? **

Eu tenho mais uma análise das correlações em geral! Repare que as correlações com linguagem_codigos sempre são as maiores e isso me faz pensar em várias hipóteses!

Será que se eu estudar mais português vou ter um desempenho melhor nas outras matérias? (lembre-se que o ENEM é uma prova que demanda interpretação de texto, então essa prerrogativa pode fazer sentido).
Será que se eu considerar provas de anos anteriores e comparar as correlações com linguagem_códigos elas serão maiores?

A verdade é que uma simples análise de correlação nos gera diversas hipóteses. **Se tiver curiosidade e quiser fazer essas análises fica como um desafio extra!**

Na videoaula você viu que tentamos plotar diversos gráficos para visualizar a correlação de uma melhor forma. Abaixo seguem os códigos usados:
"""

from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=np.bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

sns.heatmap(corr)

"""Depois de apanhar tentando criar boas imagens, resolvemos deixar esse desafio para você kkkkk... Resolva e dê aquela cornetada em nosso time uahuahha...

Ok, nós analisamos e conhecemos a base de dados, mas no final o que vou querer é construir um modelo de ML para fazer as predições de algumas notas. Para criar esse modelo de machine learning devemos analisar a distribuição dos nossos dados e verificar se existe alguma tendência entre eles, facilitando o processo preditivo. 

Então, vamos ao **pairplot**:
"""

sns.pairplot(dados_notas)

"""Embora existam alguns dados com maior dispersão, outros parecem obedecer uma certa tendência. Dessa forma, desenvolver um modelo de ML com resultados razoáveis será complexo, porém possível (para detalhes das análises, acompanhe a discussão na videoaula).

Com isso chegamos ao final de mais uma aula da #quarentenadados. E aí, o que está achando?

Agora iremos entrar em uma área totalmente nova: o desenvolvimento de modelos de machine learning! Espero que você esteja empolgado(a) para conhecer um pouquinho mais sobre esse assunto!

Crie seu próprio notebook, reproduza nossa aula e resolva os desafios que deixamos para você.

Até a próxima aula!


P.S: A partir de agora você irá colocar a mão na massa, nossos desafios serão mais analítcos. Queremos que você vivencie o dia-a-dia de um ciêntista de dados, discutindo suas conclusões no Slack e estudando as análises de outros colegas, por isso não haverá gabarito.

## Desafio 1 da [Thais André](https://twitter.com/thais_tandre)

Se a pessoa não teve presença, preencha a nota dela com algum número. A nota 0? A nota média? A mediana?
"""

# 'TP_PRESENCA' indica -> (0 - FALTOU / 1 - PRESENTE / 2 - ELIMINADO)
dados_novos = dados.copy()

for sufix in ["CN","CH","LC","MT"]:
  dados_novos.loc[dados_novos.eval(f"TP_PRESENCA_{sufix} == 0 | TP_PRESENCA_{sufix} == 2"), f"NU_NOTA_{sufix}"] = 0

dados_novos.loc[dados_novos.eval(f"TP_PRESENCA_LC == 0 | TP_PRESENCA_LC == 2"), "NU_NOTA_REDACAO"] = 0

dados_novos[colunas_de_notas].head()

"""## Desafio 2 do [Thiago Gonçalves](https://twitter.com/tgcsantos)

A matriz de correlação está feiosa, vamos deixar mais bonita? :) Não se esqueça de manter os valores dentro delas.
"""

from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=np.bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(12, 15))

# Generate a custom diverging colormap
cmap = sns.cubehelix_palette(8, start=2, rot=0, dark=0, light=3, as_cmap=True)


x_axis_labels = ['Ciencias Naturais', 'Ciencias Humanas', 'Linguagem/Codigo', 'Matematica', ''] # labels for x-axis
y_axis_labels = ['', 'Ciencias Humanas', 'Linguagem/Codigo', 'Matematica', 'Redação'] # labels for y-axis

# Draw the heatmap with the mask and correct aspect ratio
graf = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.7, vmin=0.5 ,
            center=0, square=True, linewidths=.3, 
            cbar_kws={"shrink": .5}, annot=True, 
            xticklabels=x_axis_labels, yticklabels=y_axis_labels,
            )


graf.set_title("Correlação entre calificaçoes")
graf.set_yticklabels(graf.get_yticklabels(), rotation=45)

plt.show()

"""## Desafio 3 do [Paulo Silveira](https://twitter.com/paulo_caelum)


Pairplot dos acertos de cada categoria (CN, CH, MT, LC, nota pura da redação). Usar o gabarito e as respostas
"""

materias = ['CN', 'CH', 'MT', 'LC']
respostas_prefix = 'TX_RESPOSTAS_'
gabarito_prefix = 'TX_GABARITO_'
acertos_prefix = 'ACERTOS_'

dados_limpos = dados.copy().dropna()

def calc_acertos(respostas, gabarito):
  return [sum(c==d for c, d in zip(a,b)) if (type(a) == str and type(b) == str) else 0 for a, b in zip(respostas, gabarito)]

for sufix in materias:
  dados_limpos[f"{acertos_prefix}{sufix}"] = calc_acertos(dados_limpos[f"{respostas_prefix}{sufix}"], dados_limpos[f"{gabarito_prefix}{sufix}"])


dados_acertos = dados_limpos[["ACERTOS_CN", "ACERTOS_CH", "ACERTOS_LC", "ACERTOS_MT", "NU_NOTA_REDACAO"]]

sns.pairplot(dados_acertos)
plt.show()

dados_acertos.corr()

"""## Desafio 4 do [Guilherme Silveira](https://twitter.com/guilhermecaelum)

Remover todos os zeros. Tomar o cuidado que no desafio 1 já tomamos decisões ligadas a limpeza dos dados também. Você também pode exportar para outro CSV se quiser.
"""

dados_sem_zero = dados_limpos.copy()

dados_sem_zero[["NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT","NU_NOTA_REDACAO"]] = dados_sem_zero[["NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT","NU_NOTA_REDACAO"]][~(dados_sem_zero[["NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT","NU_NOTA_REDACAO"]] == 0).any(axis=1)]

dados_sem_zero.head()

"""## Desafio 5 do [Thiago Gonçalves](https://twitter.com/tgcsantos)

Quais questões tiveram mais erros (análise sobre o gabarito x acertos x erros)
"""

# Inspirado no collab do Higor Eurípedes (PS: Não conhecia o método apply):
# Referência:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.idxmax.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html

dados_sem_zero = dados_sem_zero.dropna(subset=['CO_PROVA_CN', 'CO_PROVA_CH','CO_PROVA_LC','CO_PROVA_MT'])

def processa_linha(linha, tipo):
  resp = linha["TX_RESPOSTAS_"+tipo]
  gab = linha["TX_GABARITO_"+tipo]
  res = dict()

  for i in range(len(resp)):
    if resp[i] == 9:  # Despreza a comparação caso inglês/espanhol 
      continue
    res[i+1] = (resp[i] != gab[i]) * 1 # CHECANDO POR ERROS (i+1 pois range(len()) começa de 0 )
  
  return pd.Series(res)

maior_indice = 0
maior_valor = 0
maior_cor = "Nenhum"
maior_tipo = "CH"  # Para evitar erro na execução da exibição final


for tipo in ["CN", "CH", "MT", "LC"]:
  cores = dados_sem_zero[f"CO_PROVA_{tipo}"].unique()  # Obtem lista de cores
  print("Analisando provas: " + tipo)
  for cor in cores:  # Percorre para cada cor
    print("Analisando cor: " + str(cor))
    tmp = dados_sem_zero.query(f"CO_PROVA_{tipo} == {cor}")[[f"TX_RESPOSTAS_{tipo}", f"TX_GABARITO_{tipo}"]].apply(processa_linha, args=[tipo], axis=1).sum()
    
    idxmax = tmp.idxmax()  # Retorna o índice do valor máximo 

    if maior_valor < tmp[idxmax]:
      maior_indice = idxmax
      maior_valor = tmp[idxmax]
      maior_cor = cor
      maior_tipo = tipo

# Preparação das informações para exibição

desc_cores = {"CN": {
    447: "Azul",
    448: "Amarela",
    449: "Cinza",
    450: "Rosa",
    463: "Laranja - Adaptada Ledor",
    467: "Verde - Videoprova - Libras",
    487: "Amarela (Reaplicação)",
    488: "Cinza (Reaplicação)",
    489: "Azul (Reaplicação)",
    490: "Rosa (Reaplicação)"},
  "CH": {
    451: "Azul",
    452: "Amarela",
    453: "Branca",
    454: "Rosa",
    464: "Laranja - Adaptada Ledor",
    468: "Verde - Videoprova - Libras",
    491: "Azul (Reaplicação)",
    492: "Amarelo (Reaplicação)",
    493: "Branco (Reaplicação)",
    494: "Rosa (Reaplicação)"},
  "LC": {
    455: "Azul",
    456: "Amarela",
    457: "Rosa",
    458: "Branca",
    465: "Laranja - Adaptada Ledor",
    469: "Verde - Videoprova - Libras",
    495: "Azul (Reaplicação)",
    496: "Amarelo (Reaplicação)",
    497: "Branca (Reaplicação)",
    498: "Rosa (Reaplicação)"},
  "MT": {
    459: "Azul",
    460: "Amarela",
    461: "Rosa",
    462: "Cinza",
    466: "Laranja - Adaptada Ledor",
    470: "Verde - Videoprova - Libras",
    499: "Amarela (Reaplicação)",
    500: "Cinza (Reaplicação)",
    501: "Azul (Reaplicação)",
    502: "Rosa (Reaplicação)"}}

desc_tipos = {"CN": "Ciências da Natureza", "CH": "Ciências Humanas", "LC": "Linguagens e Códigos","MT": "Matemática"}

print("Questão com mais erros: ")
print(f"Prova  : {desc_tipos[maior_tipo]} - {desc_cores[maior_tipo][int(maior_cor)]}")
print(f"Questão: {maior_indice} (1-45)")
print(f"Erros  : {maior_valor}")

"""## Desafio 6 do [Allan Spadini](https://twitter.com/allanspadini)

Estudar o que as pessoas que estudam o assunto estão discutindo e conclusões que já chegaram sobre a utilização de informações (principalmente sensíveis) para machine learning e data science. Podcast do datahackers também sobre o assunto.

#Não esqueça de compartilhar a solução dos seus desafios com nossos instrutores, seja no Twitter, seja LinkedIn. Boa sorte!
"""