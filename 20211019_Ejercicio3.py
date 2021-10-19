# Ejercicio 3 19/10/2021
from datetime import datetime
i = 1
while i < 100:
    print(str(i) + " " + datetime.now().time().strftime('%H:%M:%S'))
    i = i+1
