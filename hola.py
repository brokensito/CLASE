class Hola():

    def __init__(self, buenas, tardes) -> None:
        self.buenas = buenas
        self.tardes = tardes

    def __str__(self) -> str:
        return "Maricon de mierda {}".format(self.tardes)


hola = Hola(1)

print(hola)

def quicksort(lista, primero, ultimo):
     
   
