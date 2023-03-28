print("Convertidor de monedas")
print("1 - USD a Euro\n2 - USD a Libra esterlina\n3 - USD a Yen japonés\n4 - USD a Peso argentino\n5 - USD a Real brasileño\n6 - USD a Peso colombiano\n7 - USD a Quetzal guatemalteco\n8 - USD a Won surcoreano\n9 -USD a Lira turca \n10 - USD a Rupia india")
opcion = float(input("Ingrese la opción de conversión que desea utilizar: "))
resultado = float(0)
 
if opcion == 1:
    print("USD a Euro")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*0.93348)
elif opcion == 2:
    print("USD a Libra esterlina")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*0.82452)
elif opcion == 3:
    print("USD a Yen japonés")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*133.584)
elif opcion == 4:
    print("USD a Peso argentino")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*199.985)
elif opcion == 5:
    print("USD a Real brasileño")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*5.2305)
elif opcion == 6:
    print("USD a Peso colombiano")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*4728.77)
elif opcion == 7:
    print("USD a Quetzal guatemalteco")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*7.60357)
elif opcion == 8:
    print("USD a Won surcoreano")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*1302.2)
elif opcion == 9:
    print("USD a Lira turca")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*18.9655)
elif opcion == 10:
    print("USD a Rupia india")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*82.1366)

 
print("El resultado de la conversión es: {0:.2f} ".format(resultado))

while True:
    print("Convertidor de Hectareas")
    print("""
1 - Hectarea a metro cuadrado
    \n2 - Hectarea a centimetro cubico
    \n3 - apagar convertidor
    """)

    opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
    resultado = 0

    if opcion == 1:
        print("Hectarea a metro cuadrado")
        entrada = float(input("Ingresa la cantidad en Hectareas: "))
        resultado = round(entrada*10000)
    elif opcion == 2:
        print("Hectarea a centimetro cubico")
        entrada = float(input("Ingresa la cantidad en Hectareas: "))
        resultado = round(entrada/100000000)
    elif opcion == 3:
        break
    print("El resultado de la conversión es: {} ".format(resultado))

    while True:
     print("""
1 - Kilómetro cúbico a Metro Cubico
    \n2 - Hectómetro cúbico a Metro Cubico
    \n3 - Decametro cubico a Metro Cubico
    \n4 - Metro Cubico a Kilometro cubico
    \n5 - Metro Cubico a Hectometro cubico
    \n6 - Metro Cubico a Decametro cubico
    \n7 - Decimetro cubico a Metro Cubico
    \n8 - Centimetro cubico a Metro Cubico
    \n9 - Milimetro cubico a Metro Cubico
    \n11 - apagar convertidor
    """)

    opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
    resultado = 0

    if opcion == 1:
        print("Kilómetro cúbico a Metro Cubico")
        entrada = float(input("Ingresa la cantidad en Kilometros cubicos: "))
        resultado = round(entrada*1000000000)
    elif opcion == 2:
        print("Hectómetro cúbico a Metro Cubico")
        entrada = float(input("Ingresa la cantidad en Hectometro cubico: "))
        resultado = round(entrada*1000000)
    elif opcion == 3:
        print("Decametro cubico a Metro Cubico")
        entrada = float(input("Ingresa la cantidad en Decametros cubicos: "))
        resultado = round(entrada*1000)
    elif opcion == 4:
        print("Metro Cubico a Kilometro cubico")
        entrada = float(input("Ingresa la cantidad en Metro cubico: "))
        resultado = round(entrada/1000000000)
    elif opcion == 5:
        print("Metro Cubico a Hectometro cubico")
        entrada = float(input("Ingresa la cantidad en Metros Cubicos: "))
        resultado = round(entrada/1000000)
    elif opcion == 6:
        print("Metro Cubico a Decametro cubico")
        entrada = float(input("Ingresa la cantidad en Metros cubicos: "))
        resultado = round(entrada/1000)
    elif opcion == 7:
        print("Decimetro cubico a Metro Cubico")
        entrada = float(input("Ingresa la cantidad en Decimetros cubicos: "))
        resultado = round(entrada*0.001)
    elif opcion == 8:
        print("Centimetro cubico a Metro Cubico")
        entrada = float(input("Ingresa la cantidad en Centimetros cubicos: "))
        resultado = round(entrada*0.000001)
    elif opcion == 9:
        print("Milimetro cubico a Metro Cubico")
        entrada = float(input("Ingresa la cantidad en Milimetros cubicos: "))
        resultado = round(entrada*0.000000001)
    elif opcion == 11:
        break
    print("El resultado de la conversión es: {} ".format(resultado))

while True:
     print("Convertidor de almacenamiento")
     print("""
1 - Kilobyte a Bytes
    \n2 - Megabyte a Kilobyte
    \n3 - Gigabyte a Megabyte
    \n4 - Terabyte a Gigabyte
    \n5 - Petabyte a Terabyte
    \n6 - Exabyte a Petabyte
    \n7 - Zettabyte a Exabyte
    \n8 - Yottabyte a Zetabyte
    """)

opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
resultado = 0

if opcion == 1:
        print("Kilobyte a Bytes")
        entrada = float(input("Ingresa la cantidad en kilobyte: "))
        resultado = round(entrada*1024)
elif opcion == 2:
        print("Megabyte a Kilobyte")
        entrada = float(input("Ingresa la cantidad en Megabytes: "))
        resultado = round(entrada*1024)
elif opcion == 3:
        print("Gigabyte a Megabyte")
        entrada = float(input("Ingresa la cantidad en Gigabytes: "))
        resultado = round(entrada*1024)
elif opcion == 4:
        print("Terabyte a Gigabyte")
        entrada = float(input("Ingresa la cantidad en Terabytes: "))
        resultado = round(entrada*1024)
elif opcion == 5:
        print("Petabyte a Terabyte")
        entrada = float(input("Ingresa la cantidad en Petabytes: "))
        resultado = round(entrada*1024)
elif opcion == 6:
        print("Exabyte a Petabyte")
        entrada = float(input("Ingresa la cantidad en Exabytes: "))
        resultado = round(entrada*1024)
elif opcion == 7:
        print("Yottabyte a Zetabyte")
        entrada = float(input("Ingresa la cantidad en Yottabytes: "))
        resultado = round(entrada*1024)
elif opcion == 8:
    break
print("El resultado de la conversión es: {} ".format(resultado))

while True:
    print("Convertidor de masas")
    print("""
    1 - Kilogramos a Gramos
    \n2 - Gramos a Kilogramos
    \n3 - libras a gramos
    \n4 - gramos a libras
    \n5 - libras a kilogramos
    \n6 - kilogramos a libras
    \n7 - kilogramos a hectogramos
    \n8 - hectogramos a kilogramos
    \n9 - decagramo a gramo
    \n10 - gramo a decagramo
    \n11 - apagar convertidor
    """)

    opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
    resultado = 0

    if opcion == 1:
        print("Kilogramos a Gramos")
        entrada = float(input("Ingresa la cantidad en kilogramos: "))
        resultado = round(entrada*1000)
    elif opcion == 2:
        print("Gramos a Kilogramos")
        entrada = float(input("Ingresa la cantidad en Gramos: "))
        resultado = round(entrada/1000)
    elif opcion == 3:
        print("libras a gramos")
        entrada = float(input("Ingresa la cantidad en libras: "))
        resultado = round(entrada*453.6)
    elif opcion == 4:
        print("gramos a libras")
        entrada = float(input("Ingresa la cantidad en gramos: "))
        resultado = round(entrada/453.6)
    elif opcion == 5:
        print("libras a kilogramos")
        entrada = float(input("Ingresa la cantidad en libras: "))
        resultado = round(entrada/2.205)
    elif opcion == 6:
        print("kilogramos a libras")
        entrada = float(input("Ingresa la cantidad en Kilogramos: "))
        resultado = round(entrada*2.205)
    elif opcion == 7:
        print("kilogramos a hectogramos")
        entrada = float(input("Ingresa la cantidad en Kilogramos: "))
        resultado = round(entrada*10)
    elif opcion == 8:
        print("Hectogramos a kilogramos")
        entrada = float(input("Ingresa la cantidad en hectogramos: "))
        resultado = round(entrada/10)
    elif opcion == 9:
        print("decagramo a gramo")
        entrada = float(input("Ingresa la cantidad en decagramo: "))
        resultado = round(entrada*10)
    elif opcion == 10:
        print("gramo a decagramo")
        entrada = float(input("Ingresa la cantidad en gramo: "))
        resultado = round(entrada/10)
    elif opcion == 11:
        break
    print("El resultado de la conversión es: {} ".format(resultado))

    while True:
    print("Convertidor de tiempo")
    print("""
    1 - Minuto a Segundos
    \n2 - Segundos a Minutos
    \n3 - Horas a Minutos
    \n4 - Horas a Segundos
    \n5 - Minutos a Horas
    \n6 - Segundos a Horas
    \n7 - Horas a Dias
    \n8 - Dias a Meses
    \n9 - Meses a Dias
    \n10 - Años a Dias
    \n11 - apagar convertidor
    """)

    opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
    resultado = 0

    if opcion == 1:
        print("Minuto a Segundos")
        entrada = float(input("Ingresa la cantidad en Minutos: "))
        resultado = round(entrada*60)
    elif opcion == 2:
        print("Segundos a Minutos")
        entrada = float(input("Ingresa la cantidad en Segundos: "))
        resultado = round(entrada/60)
    elif opcion == 3:
        print("Horas a Minutos")
        entrada = float(input("Ingresa la cantidad en Horas: "))
        resultado = round(entrada*60)
    elif opcion == 4:
        print("Horas a Segundos")
        entrada = float(input("Ingresa la cantidad en Horas: "))
        resultado = round(entrada/3600)
    elif opcion == 5:
        print("Minutos a Horas")
        entrada = float(input("Ingresa la cantidad en Minutos: "))
        resultado = round(entrada/60)
    elif opcion == 6:
        print("Segundos a Horas")
        entrada = float(input("Ingresa la cantidad en Segundos: "))
        resultado = round(entrada/3600)
    elif opcion == 7:
        print("Horas a Dias")
        entrada = float(input("Ingresa la cantidad en Horas: "))
        resultado = round(entrada/24)
    elif opcion == 8:
        print("Dias a Meses")
        entrada = float(input("Ingresa la cantidad en Dias: "))
        resultado = round(entrada/30.417)
    elif opcion == 9:
        print("Meses a Dias")
        entrada = float(input("Ingresa la cantidad en Meses: "))
        resultado = round(entrada*30.417)
    elif opcion == 10:
        print("Años a Dias")
        entrada = float(input("Ingresa la cantidad en Años: "))
        resultado = round(entrada*365)
    elif opcion == 11:
        break
    print("El resultado de la conversión es: {} ".format(resultado))

    print("Convertidor de Manzanas")
print("1 - Manzanas a Varas Cuadradas\n2 - Manzanas a Metros Cuadrados \n3 - Manzanas a Pies\n4 - Manzanas a  Acres\n5 - Manzanas a Hectarea\n6 - Varas cuadradas a Manzanas\n7 - Metros Cuadrados a Manzanas\n8 - Pies a Manzanas\n9 - Acres a Manzanas\n10 - Hectarea a Manzanas")
opcion = float(input("Ingrese la opción de conversión que desea utilizar: "))
resultado = float(0)
 
if opcion == 1:
    print("Manzanas a Varas Cuadradas")
    entrada = float(input("Ingresa la cantidad en Manzanas: "))
    resultado = float(entrada*10000)
elif opcion == 2:
    print("Manzanas a Metros Cuadrados")
    entrada = float(input("Ingresa la cantidad en Manzanas: "))
    resultado = float(entrada*6988)
elif opcion == 3:
    print("Manzanas a Pies")
    entrada = float(input("Ingresa la cantidad en Manzanas: "))
    resultado = float(entrada*75220.68)
elif opcion == 4:
    print("Manzanas a  Acres")
    entrada = float(input("Ingresa la cantidad en Manzanas: "))
    resultado = float(entrada*1.72677)
elif opcion == 5:
    print("Manzanas a Hectarea")
    entrada = float(input("Ingresa la cantidad en Manzanas: "))
    resultado = float(entrada*0.6988)
elif opcion == 6:
    print("Varas cuadradas a Manzanas")
    entrada = float(input("Ingresa la cantidad en Varas cuadradas: "))
    resultado = float(entrada/10000)
elif opcion == 7:
    print("Metros Cuadrados a Manzanas")
    entrada = float(input("Ingresa la cantidad en Metros Cuadrados: "))
    resultado = float(entrada/6988)
elif opcion == 8:
    print("Pies a Manzanas")
    entrada = float(input("Ingresa la cantidad en Pies: "))
    resultado = float(entrada/75220.68)
elif opcion == 9:
    print("Acres a Manzanas")
    entrada = float(input("Ingresa la cantidad en Acres: "))
    resultado = float(entrada/1.72677)
elif opcion == 10:
    print("Hectarea a Manzanas")
    entrada = float(input("Ingresa la cantidad en Hectarea: "))
    resultado = float(entrada/0.6988)


 
print("El resultado de la conversión es: {0:.4f} ".format(resultado))