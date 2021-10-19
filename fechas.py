# Tipo de dato "date"
# Ejemplo de resta de fechas
# Calculo de dias restantes para cumple

from datetime import date
from datetime import datetime

print("¿Cuando es tu cumpleanyos?")
print("Dia: ")
dia = int(input())
print("Mes: ")
mes = int(input())


hoy = datetime.now()
anyocumple = hoy.year

if(hoy.month > mes):
    anyocumple = anyocumple + 1
elif (hoy.month == mes and hoy.dia > dia):
    anyocumple = anyocumple + 1

resta = abs(hoy - datetime(anyocumple, mes, dia))
print(f"quedan " + str(resta.days) + " dias para tu cumple")
