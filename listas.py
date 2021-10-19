# Tipo de dato "listas"
#mutables y ordenadas, permite repeticion
#se define con "[" , "]" , pueden ser cualquier tipo
#ejemplo 
import random

lista_entero=[1,3,4,5,3,7,2,4]
lista_fruta=["manzana","platano","albaricoque"]

print(lista_entero)
print(lista_fruta)

i=0
for i in range(5):
    lista_entero.append(random.randrange(10,25))


print(lista_entero)
