# A melhor opção para coletar dividendos das empresas brasileiras é através do repositório yfinance que pega dados do Yahoo
# Tags: histórico dividendos brasileiros; histórico dividendos bolsa de valores ; histórico dividendos b3; dividendos bolsa brasil
#
# O código abaixo extrai os dividendos históricos pra uma empresa facilmente, em um formato fácil de manusear

import pandas_datareader.data as web
#Para limpar possíveis bugs do data_reader para o yahoo
!pip install yfinance --upgrade --no-cache
import yfinance as yf
yf.pdr_override()

#Pegar dividendos históricos e de forma simples do Itaú
itsa4 = yf.Ticker('ITSA4.SA')
itsa4_dividendos = itsa4.dividends

# Muito simples, rápido e eficiente! A partir daqui é possível fazer várias análises relacionando dados
