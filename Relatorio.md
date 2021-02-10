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
![alt](https://github.com/Miller202/desafio-smtt/blob/main/img/Empresa_atraso.png) 
* Observando o gráfico, podemos concluir que a empresa São Francisco tem o maior número de viagens com atraso, aproximadamente 2400, enquanto a empresa Auto Viação Veleiro possuir o menor índice de atrasos, aproximadamente 750, porém, vale ressaltar que a Veleiro possui a menor frota de ônibus em Maceió, fato que pesou na quantidade inferior de viagens atrasadas. A empresa Real Transportes Urbanos Ltda também teve um bom desempenho, tendo menos atrasos que as empresas São Francisco e Viação Cidade de Maceió.

---

### Gráfico de Barra da quantidade de viagens adiantadas por empresa

* Este gráfico de barra exibe a quantidade absoluta de viagens com **adiantamento** no eixo **X** e o nome das empresas no eixo **Y**. Para obter estas informações, foi necessário criar um dataframe que considere somente as colunas em que a duração realizada de uma viagem foi **menor** que a duração prevista.
![alt](https://github.com/Miller202/desafio-smtt/blob/main/img/Empresa_adiantamento.png)
* Observando o gráfico, podemos concluir que a empresa Viação Cidade de Maceió possui o maior índice de viagens realizadas com adiantamento, vindo em seguida a empresa Real Transportes LTDA, ambas com eficiência no tempo de viagem. Além disso, a Auto Viação Veleiro LTDA possui uma quantidade inferior de viagens adiantadas, sendo a pior nesse critério.

---

### Gráfico de Pizza do percentual de viagens pontuais por empresa

* Este gráfico de pizza exibe o percentual de viagens realizadas com **pontualidade** por empresa. Para obter uma quantidade considerável de dados, foi considerada uma tolerância de **2 minutos** para uma viagem ser marcada como pontual, ou seja, uma viagem com previsão de 45 minutos é pontual se estiver no intervalo **43 <= x <= 47**.
![alt](https://github.com/Miller202/desafio-smtt/blob/main/img/Empresa_pontualidade.png)
* Observando o gráfico de pizza, temos que a empresa Real Transportes Urbanos Ltda tem a maior pontualidade nas suas viagens, cumprindo o tempo de viagem prevista com superioridade em relação às outras empresas, apesar da Viação Cidade de Maceió também possuir um bom percentual. A empresa Auto Viação Veleiro LTDA também foi a empresa menos pontual, provando o que foi dito nos resultados do gráfico de atrasos, que a Veleiro possui a menor frota de transportes coletivos.

---

### Histograma do tempo de viagem dos transportes coletivos de Maceió

* Este histograma apresenta o tempo das viagens (em minutos) no eixo **X** e a frequência absoluta no eixo **Y**. Para obter os dados, foi montada uma tabela de frequências da **duração realizada** das viagens do transporte coletivo.
![alt](https://github.com/Miller202/desafio-smtt/blob/main/img/Tempo_viagem.png)
* Observando o histograma, podemos concluir que a maior parte das viagens dos transportes coletivos de Maceió possuem um tempo médio de 40-60 minutos, e a minoria está fora do intervalo de 20-80 minutos.

---

### Conclusões e considerações finais

* veredito
