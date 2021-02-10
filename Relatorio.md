![alt](https://img.icons8.com/plasticine/2x/business-report.png) 
# Relatório do tempo de viagem dos transportes coletivos de Maceió

* Autor: Michael Miller Rodrigues Cardoso.
* Relatório referente aos dados das viagens feitas entre os dias 04/10/2020 e 10/10/2020.

***Devido ao fato de servir como base para tomada de decisão, foi elaborado um resumo
sobre o tempo de viagem no Sistema de Transporte Coletivo de Maceió. Foram desenvolvidas 
quatro visualizações que permitem avaliar os principais indicadores de qualidade do sistema, 
com relação ao atraso, adiantamento, pontualidade e tempo médio das viagens.***

***As visualizações foram desenvolvidas em python com auxílio das seguintes ferramentas:***
* Pandas - biblioteca para para manipulação e análise dos dados;
* Matplotlib - biblioteca para criação de gráficos e visualizações de dados;
* NumPy - pacote python para realizar cálculos em arrays multidimensionais.

---

### Gráfico de Barra da quantidade de viagens atrasadas por empresa

* Este gráfico de barra exibe a quantidade absoluta de viagens **atrasadas** no eixo **X** e o nome das empresas no eixo **Y**. Para obter estas informações, foi necessário criar um dataframe que considere somente as colunas em que a duração realizada de uma viagem foi **maior** que a duração prevista.
* img
* conclusão

---

### Gráfico de Barra da quantidade de viagens adiantadas por empresa

* Este gráfico de barra exibe a quantidade absoluta de viagens com **adiantamento** no eixo **X** e o nome das empresas no eixo **Y**. Para obter estas informações, foi necessário criar um dataframe que considere somente as colunas em que a duração realizada de uma viagem foi **menor** que a duração prevista.
* img
* conclusão

---

### Gráfico de Pizza do percentual de viagens pontuais por empresa

* Este gráfico de pizza exibe o percentual de viagens realizadas com **pontualidade** por empresa. Para obter uma quantidade considerável de dados, foi considerada uma tolerância de **2 minutos** para uma viagem ser marcada como pontual, ou seja, uma viagem com previsão de 45 minutos é pontual se estiver no intervalo **43 <= x <= 47**.
* img
* conclusão

---

### Histograma do tempo de viagem dos transportes coletivos de Maceió

* Este histograma apresenta o tempo das viagens (em minutos) no eixo **X** e a frequência absoluta no eixo **Y**. Para obter os dados, foi montada uma tabela de frequências da **duração realizada** das viagens do transporte coletivo.
* img
* conclusão

---

### Conclusões e considerações finais

* veredito
