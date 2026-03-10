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

#FII - SIMUlACOES




