import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('../viagens.csv')

data1 = data.empresa[(data.duracao_prevista == data.duracao_realizada) 
  | (data.duracao_realizada == (data.duracao_prevista + 1.0)) 
  | (data.duracao_realizada == (data.duracao_prevista - 1.0))
  | (data.duracao_realizada == (data.duracao_prevista + 2.0)) 
  | (data.duracao_realizada == (data.duracao_prevista - 2.0))]

data2 = pd.DataFrame(data1) # check the dataframe.
table = pd.DataFrame(data1.value_counts()) # get the frequencies in the frequency table.

x = table.index #empresa
y = table.empresa #frequencia de adiantamentos
explode = (0.1, 0, 0, 0)

# plot chart
plt.rcParams['font.size'] = 14.0
fig1, ax1 = plt.subplots(figsize=(16,8))
ax1.pie(y, explode=explode, labels=x, autopct='%1.1f%%',
        shadow=True, startangle=75)
ax1.axis('equal')
plt.title("Percentual de pontualidade das viagens por empresa", 
		fontsize=20, bbox={'facecolor':'0.8', 'pad':5})
plt.show()

#plt.savefig("Empresa_pontualidade.png", dpi=300)