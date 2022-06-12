from Funciones import * 


dolar_colombia= trm(date)[4]           
dolar_argentina=65
dolar_mexico=24

menu= """Bienvenido al conversor de monedas 

1- Peso Colombiano
2- Peso Argentino
3- Pesos Mexicanos

Elige una opcion:   """

opcion=int(input (menu))

if opcion==1:

    pesos=float (input ("Cuantos pesos colombiansos tienes: "))
    dolares=round(pesos/dolar_colombia,2)          #round redondea un numero al numro de decimales que le pongas, en este caso=2
    dolares=str(dolares)
    print("Tienes " + dolares + " USD")

elif opcion==2:

    pesos=float (input ("Cuantos pesos argentinos tienes: "))
    dolares=round(pesos/dolar_argentina,2)          #round redondea un numero al numro de decimales que le pongas, en este caso=2
    dolares=str(dolares)
    print("Tienes $" + dolares + " USD")
    
elif opcion==3:
    
    pesos=float (input ("Cuantos pesos mexicanos tienes: "))
    dolares=round(pesos/dolar_mexico,2)          #round redondea un numero al numro de decimales que le pongas, en este caso=2
    dolares=str(dolares)
    print("Tienes $" + dolares + " USD")

else:
    print("Ingregsa una opion correcta por favor")


