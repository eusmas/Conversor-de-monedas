# from Funciones import trm
# from Funciones import Conversor_moneda

from Funciones import *

dolar_colombia= trm(date)[4]           
dolar_argentina=65
dolar_mexico=24

menu= """Bienvenido al conversor de monedas 

1- Peso Colombiano
2- Peso Argentino
3- Pesos Mexicanos

Elige una opcion:   """

opcion=int(input(menu))

#print("Tienes " + dolares + " USD")


if opcion==1:
    dolares=Conversor_moneda("Colombianos", dolar_colombia)

elif opcion==2:
    dolares=Conversor_moneda("Argentinos", dolar_argentina)
    
elif opcion==3:
    dolares=Conversor_moneda("Mexicanos", dolar_mexico)
else:
    print("Ingregsa una opion correcta por favor")


print("Tienes $" + dolares + " USD")

