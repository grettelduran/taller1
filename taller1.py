import math
# actual example (we are using a decorator @ )
class Piedra:
    """This class is going to be the model of a
    regular Device with serialNumber & manufacture
    use ->property fullName to review details
    """
    def __init__(self, masa, potasio, argon):
        self.masa = masa
        self.potasio = potasio
        self.argon =argon

    @property
    def edad(self):
        return (1.248*(10**9)/math.log(2))*((self.potasio+self.argon/0.109)/self.potasio)
    @property
    def categoria(self):
        if self.edad<65500000:
            return "cenozoica"
        if self.edad < 251000000:
            return "mesozoica"
        if self.edad <542000000:
            return "paleozoica"
        else:
            return "pre-paleozoica" 
    @property
    def descripcion(self):
        return 'La masa: {}g\nLa cantidad de potasio: {}mg\nLa cantidad de argon: {}mg\nLa edad: {}\nLa categoria: {}'.format(self.masa,self.potasio, self.argon, self.edad,self.categoria)

# capturando datos del usuario

cant_muestras =  int(input( "Ingrese la cantidad de muestras:  =>  "))
print("cantidad de muestras solicitadas:", cant_muestras)
for x in range (0,cant_muestras):
    masa =  float(input( "Ingrese la masa de la piedra:  =>  "))
    potasio =  float(input( "Ingrese la cantidad de potasio de la piedra:  =>  "))
    argon =  float(input( "Ingrese la cantidad de argon de la piedra:  =>  "))
    piedra = Piedra(masa, potasio, argon)
    print(piedra.descripcion)
