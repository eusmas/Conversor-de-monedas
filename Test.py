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

valor_dolar= trm(date)
print(type(valor_dolar))

#print (trm(date))
#print (valor_dolar)