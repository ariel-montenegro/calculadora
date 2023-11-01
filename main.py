
from calculadora import Calculadora


calculadora = Calculadora()


salir = ''

while salir != 'si':
    calculadora.bienvenida()
    numero1, numero2 = calculadora.ingresar_numeros()
    operacion = calculadora.seleccionar_operacion()
    resultado = calculadora.realizar_operacion(numero1, numero2, operacion)
    
    salir= 'si'
