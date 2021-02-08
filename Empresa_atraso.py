import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('viagens.csv')

data1 = data.empresa[data.duracao_prevista < data.duracao_realizada]
data2 = pd.DataFrame(data1) # check the dataframe.
table = pd.DataFrame(data1.value_counts()) # get the frequencies in the frequency table.

df = pd.DataFrame({'name': ['Empresa São Francisco', 'Viação Cidade de Maceió', 
                                  'Real Transportes Urbanos Ltda.	', 'Auto Viação Veleiro LTDA'],
                         'number': [2316, 1889, 1436, 728]})

x = df.name #empresa
y = df.number #frequencia de atrasos

#visual
plt.figure(figsize=(15,8))
plt.title('Quantidade de atrasos por empresa', fontsize=20)
plt.xlabel('Empresa', fontsize=15)
plt.ylabel('Atrasos', fontsize=15)
plt.grid(axis='y', color='#a3a3a3', linestyle="--")
plt.ylim((0, 2500))

#plot
plt.bar(x, y, color='#34daf7', edgecolor='#a3a3a3', width=0.9)
plt.show()

