import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('../viagens.csv')

data1 = data.duracao_realizada[data.duracao_realizada > 0]
data2 = pd.DataFrame(data1)

x = data2.duracao_realizada
y = data2.index

#visual
plt.figure(figsize=(13,7))
plt.title('Histograma do tempo de viagem dos transportes coletivos', 
          fontsize=20, bbox={'facecolor':'0.8', 'pad':2})
plt.xlabel('Tempo (minutos)', fontsize=14)
plt.ylabel('Frequência absoluta', fontsize=14)
plt.ylim((0, 6000))
plt.xlim((0, 160))
plt.yticks(np.arange(0, 6000, 800))
plt.xticks(np.arange(0, 160, 10))

#plot
plt.style.use('ggplot')
plt.hist(x, color='#ed4545', rwidth=0.97)
plt.show()
