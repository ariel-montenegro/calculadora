 
from calculadora import Calculadora


calculadora = Calculadora()
calculadora.bienvenida()

salir = ''

while salir != 'si':

    numero1, numero2 = calculadora.ingresar_numeros()
    try:
        int_numero1 = int(numero1)
        int_numero2 = int(numero2)
        int_numero1 / int_numero2
    except ValueError:
        print('\n Ambos números deben ser validos \n')
        continue
    
    operacion = calculadora.seleccionar_operacion()
    
    if operacion not in list(calculadora.operaciones.keys()):
        print('\n Operacion no permitida \n')
        continue
    if operacion == '/' and numero2 == '0':
        print('\n El divisor no puede ser cero \n')
        continue
    
    resultado = calculadora.realizar_operacion(numero1, numero2, operacion) 
    calculadora.guardar_operacion(numero1, numero2, resultado, operacion)
    print(f'\n El resultado es: {resultado} \n')
    respuesta_operaciones = input("\n ¿Desea ver las operaciones anteriores? [si] [no]:  ")
    if respuesta_operaciones == 'si':
        operaciones_anteriores = calculadora.mostrar_operaciones_anteriores()
        print(operaciones_anteriores)
    respuesta_salir = input("\n ¿Desea salir? [si] [no]: ")
    salir = respuesta_salir

print('Hasta luego')