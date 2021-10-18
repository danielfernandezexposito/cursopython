# Tipo de dato "date"
#Ejemplo de resta de fechas 
#Calculo de dias restantes para cumple

from datetime import date
from datetime import datetime

print("¿Cuando es tu cumpleanyos?")
print("Dia: ")
dia=int(input())
print("Mes: ")
mes=int(input())
anyocumple=2021

hoy=datetime.now()

if(hoy.month>mes):
    anyocumple=2022
elif (hoy.month==mes and hoy.dia>dia):
    anyocumple=2022
 
resta=abs(hoy - datetime(anyocumple,mes,dia))
print(f"quedan " + str(resta.days) + " dias para tu cumple")

