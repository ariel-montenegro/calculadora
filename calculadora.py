class Calculadora:
    
    operaciones = {'+':'suma', '-':'resta','*':'multiplicación', '/':'division'}
    
    @staticmethod
    def bienvenida():
        """ Mensaje de bienvenida """
        mensaje_bienvenida = 'Bienvenido a la calculadora de python'
        print('*'*len(mensaje_bienvenida))
        print(mensaje_bienvenida)
        print('*'*len(mensaje_bienvenida) + '\n')

    def ingresar_numeros(self):
        """ Se ingresar numeros enteros por cosola """
        numero1 = input('Por favor ingrese el primer numero: ')
        numero2 = input('Por favor ingrese el segundo numero: ')
        return numero1, numero2

    def seleccionar_operacion(self):
        """ Seleccionar operacion a realizar 
        suma, resta, division, y multiplicacion
        las mismas estan definidas en el atributo
        de clase operaciones"""
        for key, value in self.operaciones.items():
            print(f'[{key}] {value}')
        operacion = input('\n Seleccione la operacion a realizar:')
        return operacion
    
    def realizar_operacion(self, numero1, numero2, operacion):
        """ Se realizar el calculo para retornar el resultado """
        resultado = str(eval(numero1 + operacion + numero2))
        return resultado

    #def guardar_operacion(self, resultado, operacion):
    #    log = open('operaciones.txt', 'a')
    
        
    
    