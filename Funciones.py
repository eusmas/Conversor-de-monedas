#!/usr/bin/env python

from multiprocessing.sharedctypes import Value
from suds.client import Client
import time

WSDL_URL = 'https://www.superfinanciera.gov.co/SuperfinancieraWebServiceTRM/TCRMServicesWebService/TCRMServicesWebService?WSDL'
date = time.strftime('%Y-%m-%d')

def trm(date):
    try:
        client = Client(WSDL_URL, location=WSDL_URL, faults=True)
        trm =  client.service.queryTCRM(date)
    except Exception as e:
        return str(e)

    return trm

dolar_colombia= trm(date)[4] #trm(date) entrega una especie de vector con mucha info de la trm del dia (date), en la posicion 4 esta el valor en $pesos tipo float



print(trm(date))
print(dolar_colombia)