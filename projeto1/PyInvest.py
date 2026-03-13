import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
#entradas
capital=float(input('capital inicial'))
aporte= float(input('aporte inicial'))
meses= int(input('prazo(meses)'))
cdi_anual= float(input('CDI anual(%)'))/100
perc_cdb= float(input('percentual do CDI(%)'))/100
perc_lci=float(input('percentualdoLCI(%)'))/100
taxa_fii= float(input('rentabilidade mensal FII(%)'))/100
meta= float(input('meta financeira(R$)'))
#conversao_CDI
cdi_mensal = math.pow((cdi_anual),1/12) -1


#TOTAL investido
total_ivestido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb =(capital * math.pow(1 + taxa_cdb),meses) + (aporte * meses)
lucro_cdb= montante_cdb - total_ivestido
montante_cdb_liquido = total_ivestido + (lucro_cdb *0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow ( 1 + taxa_lci), meses) + (aporte+ meses)

#poupanca
taxa_poupanca= 0.005
montante_poupanCa = (capital * math.pow(1 + taxa_poupanca), meses) + (aporte * meses)
montante = (capital * math.pow((1 + taxa_fii), meses) + (aporte * meses))
variacao = random.uniform(-0.03, 0.03) 
valor_final = montante * (1 + variacao)


variacao_1= random.uniform(-0.03,0.03)
variacao_2= random.uniform(-0.03,0.03)
variacao_3= random.uniform(-0.03,0.03)
variacao_4= random.uniform(-0.03,0.03)
variacao_5= random.uniform(-0.03,0.03)

FII1= (capital * math.pow(1 + taxa_fii, meses) + (aporte * meses)) *(1 + variacao_1)
FII2= (capital * math.pow(1 + taxa_fii, meses) + (aporte * meses)) *(1 + variacao_2)
FII3= (capital * math.pow(1 + taxa_fii, meses) + (aporte * meses)) *(1 + variacao_3)
FII4= (capital * math.pow(1 + taxa_fii, meses) + (aporte * meses)) *(1 + variacao_4)
FII5= (capital * math.pow(1 + taxa_fii, meses) + (aporte * meses)) *(1 + variacao_5)

taxa_fii= (FII1,FII2,FII3,FII4,FII5)

media_FII = statistics.mean(taxa_fii)
mediana_FII = statistics.median(taxa_fii)
desvio_FII = statistics.stdev(taxa_fii)

#datas

data_simulacao= datetime.datetime.now()
dias= meses * 30
data_resgate= data_simulacao + datetime.timedelta(days= dias)

#meta 
meta_atingida= media_FII>= meta

#formatação moeda
total_format= locale.currency(total_investido, grouping= True)
cdb_format= locale.currency(montante_cdb_liquido, grouping= True)
lci_format= locale.currency(montante_lci, grouping= True)
poup_format= locale.currency(montante_poupanca, grouping= True)

media_format= locale.currency(media_FII, grouping= True)
mediana_format= locale.currency(mediana_FII, grouping= True)
desvio_format= locale.currency(desvio_FII, grouping= True)

#grafico ASCII
graf_cdb= "█" * int(montante_cdb_liquido / 1000)
graf_lci= "█" * int(montante_lci / 1000)
graf_poup= "█" * int(montante_poupanca / 1000)
graf_FII= "█" * int(media_FII / 1000)

#relatório

print("relatório de investimento")

print("data de simulação: " ,data_simulacao.strftime("%d/%m/%y"))
print("data estimada de resgate: " ,data_resgate.strftime("%d/%m/%y"))

print("total investido: ", total_format)

print("resultados")

print("cdb:", cdb_format)
print("lci:", lci_format)
print("poupança", poup_format)
print("FII (media): ", media_format)

print ("estatisticas FII")

print("media: ", media_format)
print("mediana:", mediana_format)
print("desvio padrão: ", desvio_format)

print("meta financeira atingida: ", meta_atingida)

print("grafico comparativo")
print("cdb", graf_cdb)
print("lci", graf_lci)
print("poupança: ", graf_poup)
print("FII", graf_FII)
#FII - SIMUlACOES




