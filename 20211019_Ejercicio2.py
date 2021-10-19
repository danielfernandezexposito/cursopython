# Ejercicio  2 19/10/2021

# Modificar el ejercicio herencia.py a las clases Animal y Perro. De manera que Perro tiene un número de patas 

class Animal(object):
    def __init__(self, especie ):
        self.especie= especie



    def __str__(self):
        return "especie:"+self.especie

class Perro(Animal):
    def __init__(self, especie, patas ):
        super(Perro, self).__init__(especie)
        self.patas = patas

    def __str__(self):
        return "especie:" + self.especie + " patas: " + self.patas

a = Animal("perro")
print(a)
b = Perro("perro","4")
print(b) 
