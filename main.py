 
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
        print('Ambos números deben ser validos')
    else:
        operacion = calculadora.seleccionar_operacion()
        if operacion == '/' and numero2 == '0':
            print('El divisor no puede ser cero')
            break
        resultado = calculadora.realizar_operacion(numero1, numero2, operacion) 
        calculadora.guardar_operacion(resultado, operacion)
    print(f'El resultado es: {resultado} \n')
    respuesta = input("¿Desea continuar? [si] [no]:  ")
    salir = respuesta

print('Hasta luego')

    
    