class Calculadora:
    
    operaciones = {'+':'suma', '-':'resta','*':'multiplicación', '/':'division', '**': 'potencia'}
    
    @staticmethod
    def bienvenida():
        """ Mensaje de bienvenida """
        mensaje_bienvenida = 'Bienvenido a la calculadora de python'
        print('*'*len(mensaje_bienvenida))
        print(mensaje_bienvenida)
        print('*'*len(mensaje_bienvenida) + '\n')

    def ingresar_numeros(self):
        """ Se ingresar numeros enteros por cosola """
        numero1 = input('\n Por favor ingrese el primer numero: ')
        numero2 = input('\n Por favor ingrese el segundo numero: ')
        return numero1, numero2

    def seleccionar_operacion(self):
        """ Seleccionar operacion a realizar 
        suma, resta, division, y multiplicacion
        las mismas estan definidas en el atributo
        de clase operaciones"""
        print('\n Operaciones disponibles \n')
        for key, value in self.operaciones.items():
            print(f'[{key}] {value}')
        operacion = input('\n Seleccione la operacion a realizar:')
        return operacion
    
    def realizar_operacion(self, numero1, numero2, operacion):
        """ Se realizar el calculo para retornar el resultado """ 
        resultado = str(eval(numero1 + operacion + numero2))
        return resultado

    def guardar_operacion(self, numero1, numero2, resultado, operacion):
        operacion_detalle = self.operaciones.get(operacion)
        with open('operaciones.txt', 'a') as log:
            log.writelines(f'\n La {operacion_detalle} de {numero1} y {numero2} es igual a {resultado}')
            log.close()
    
    def mostrar_operaciones_anteriores(self):
        log = open("operaciones.txt", "r") 
        return log.read()
    
    