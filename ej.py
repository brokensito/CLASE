


class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)


class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} kg".format(self.carga)

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return Vehiculo.__str__() + ", {} es su tipo".format(self.tipo)

class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        Bicicleta.__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Bicicleta.__str__() + ", {} km/h, {} cc".format(self.velocidad,self.cilindrada)



c = Motocicleta("azul", 4, 150, 1200, 80)
print(c)



    

