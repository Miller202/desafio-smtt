import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../viagens.csv')

data1 = data.empresa[data.duracao_prevista < data.duracao_realizada]
data2 = pd.DataFrame(data1) # check the dataframe.
table = pd.DataFrame(data1.value_counts()) # get the frequencies in the frequency table.

x = table.index #empresa
y = table.empresa #frequencia de atrasos

#visual
plt.figure(figsize=(16,8))
plt.title('Quantidade de atrasos por empresa', fontsize=20)
plt.xlabel('Empresa', fontsize=15)
plt.ylabel('Atrasos', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', color='#a3a3a3', linestyle="--")
plt.ylim((0, 2500))

#plot
plt.bar(x, y, color='#34daf7', edgecolor='#a3a3a3', width=0.8)
plt.show()

