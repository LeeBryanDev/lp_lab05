# modulo_ingreso.py

from datetime import datetime
class Usuario:
    def __init__(self, clave):
        self._clave = clave
        self._fecha = None

    # get y set de la clave
    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, valor):
        self._clave = valor

    # get y set de la fecha
    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

class Persona(Usuario):
    def __init__(self, dni, clave):
        Usuario.__init__(self, clave)
        self._dni = dni

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        self._dni = valor

    # La persona ingresa con DNI (un solo intento)
    def ingreso(self):
        dni = input("Ingrese su DNI: ")
        clave = input("Ingrese su contraseña: ")

        if dni == self.dni and clave == self.clave:
            self.fecha = datetime.now()
            print("Ingreso correcto:", self.fecha)
            return True

        if dni != self.dni:
            print("DNI incorrecto")
        if clave != self.clave:
            print("Contraseña incorrecta")
        return False
class Empresa(Usuario):
    def __init__(self, ruc, clave):
        Usuario.__init__(self, clave)
        self._ruc = ruc

    @property
    def ruc(self):
        return self._ruc

    @ruc.setter
    def ruc(self, valor):
        self._ruc = valor

    # La empresa ingresa con RUC (un solo intento)
    def ingreso(self):
        ruc = input("Ingrese su RUC: ")
        clave = input("Ingrese su contraseña: ")

        if ruc == self.ruc and clave == self.clave:
            self.fecha = datetime.now()
            print("Ingreso correcto:", self.fecha)
            return True

        if ruc != self.ruc:
            print("RUC incorrecto")
        if clave != self.clave:
            print("Contraseña incorrecta")
        return False
# ----- PRUEBA -----
# Para probar la empresa, cambia la línea de abajo por:
# usuario = Empresa("20123456789", "empresa99")
usuario = Persona("12345678", "clave123")

intentos = 0
entro = False

while entro == False:
    entro = usuario.ingreso()      # misma función, pero cada clase pide lo suyo

    if entro == False:
        intentos = intentos + 1
        if intentos > 3:
            print("Pista: empieza con", usuario.clave[0], "y termina con", usuario.clave[-1])
