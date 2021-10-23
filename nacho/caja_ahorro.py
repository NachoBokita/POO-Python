"""
    Ejercicio 1:
        Modelar el objeto caja de ahorro:
            - un titular
            - un saldo
        
        y debera poder:
            - depositar un monto
            - puedeExtraer un monto
            - extraer un monto
            - en el caso de querer extraer un monto superior 
              al monto disponible arrojara una 
              excepcion ValueError("Imposible realizar extracción.")

        Realizar los test necesarios que validen 
        el comportamiento.  
"""


class CajaAhorro(object):
    
    __titular = "Carlos"  # propiedad privada
    __saldo = 0

    @property
    def titular(self): return self.__titular  # Guetter

    @titular.setter
    def titular(self, valor): self.__titular = valor  # Setter
    
    @property
    def saldo(self): return self.__saldo  # Guetter

    @saldo.setter
    def saldo(self, valor): self.__saldo = valor  # Setter
    
    # ------ Metodos de la clase ------- #
    def depositar(self, monto: int):
        """ Metodo que realiza un deposito al saldo base de la caja de ahorro. """
        self.saldo += monto
        
    def puedeExtraer (self,un_monto):
        return un_monto <= self.saldo
              
    def extraer(self, un_monto): 
        if self.puedeExtraer(un_monto): 
            self.__saldo -= un_monto
        else: 
            raise ValueError("Imposible realizar extracción.")

if __name__ == "__main__":
    cajaAhorro1 = CajaAhorro()

    print(cajaAhorro1.titular)
    print(cajaAhorro1.saldo)

    cajaAhorro1.depositar(300)
    print(cajaAhorro1.saldo)
    
    cajaAhorro1.puedeExtraer(300)
    
    cajaAhorro1.extraer(500)
    print(cajaAhorro1.saldo)