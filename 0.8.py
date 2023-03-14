print("Comprobador de múltiplos")
num = int(input("Introduzca el número: "))
if num % 3 ==0 and num % 5 ==0:
    print (" Si es múltiplo de 3 y 5")
elif num% 3==0:
    print (" Si es múltiplo de 3 pero no de 5")

elif num% 5==0:
    print ("Si es múltiplo de 5 pero no de 3")

else:
    print("No es múltiplo de 3 ni de 5")