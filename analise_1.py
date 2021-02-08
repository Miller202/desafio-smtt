import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('viagens.csv')

data2 = data.empresa[data.duracao_prevista < data.duracao_realizada]
data3 = pd.DataFrame(data2)

x = data3.empresa

plt.title('Quantidade de atrasos por empresa')
plt.xlabel('Empresa')
plt.ylabel('Atrasos')

plt.hist(x, color='orange')
plt.show()
