print("Convertidor de tiempo")
print("1 - Segundos a Minutos \n2 - Segundos a Horas")
opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
resultado = 0
 
if opcion == 1:
    print("Segundos a Minutos")
    entrada = float(input("Ingresa la cantidad en Segundos: "))
    resultado = round(entrada/60)
elif opcion == 2:
    print("Segundos a Horas")
    entrada = float(input("Ingresa la cantidad en Segundos: "))
    resultado = round(entrada/3600)
 
print("El resultado de la conversión es: {} ".format(resultado))