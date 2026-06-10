opcion=0
while opcion!=6:
    print("CALCULADORA")
    print("Escribe el numero para acceder a la opcion")
    print("1: SUMAR")
    print("2: RESTAR")
    print("3: MULTIPLICAR")
    print("4: DIVIDIR")
    print("5: OPERACION MIXTA")
    print("6: SALIR")
    opcion=input()

    match opcion:

        case "1":
            print("HA ELEGIDO SUMAR")
            resultado=float(input("Escriba el primer numero-- "))
            respuesta="s"
            while respuesta in ("si", "s"):
                num1=resultado
                num2=float(input("Escriba el numero a sumar-- "))
                resultado=resultado+num2
                print(f"{num1}+{num2}={resultado}")
                repetir=True
                while repetir==True:
                    respuesta=input(f"¿Desea continuar sumando con {resultado}?-- ").lower()
                    if respuesta== "si" or respuesta=="s":
                        repetir=False
                    elif respuesta=="no" or respuesta=="n":
                        repetir=False
                    else:
                        print("opcion incorrecta. reintentar")
        
        case "2":

            print("HA ELEGIDO RESTAR")
            resultado=float(input("Escriba el primer numero-- "))
            respuesta="s"
            while respuesta in ("si", "s"):
                num1=resultado
                num2=float(input("Escriba el numero a sumar-- "))
                resultado=resultado-num2
                print(f"{num1}-{num2}={resultado}")
                repetir=True
                while repetir==True:
                    respuesta=input(f"¿Desea continuar restando con {resultado}?-- ").lower()
                    if respuesta== "si" or respuesta=="s":
                        repetir=False
                    elif respuesta=="no" or respuesta=="n":
                        repetir=False
                    else:
                        print("opcion incorrecta. reintentar")
        case "3":

            print("HA ELEGIDO MULTIPLICAR")
            resultado=float(input("Escriba el primer numero-- "))
            respuesta="s"
            while respuesta in ("si", "s"):
                num1=resultado
                num2=float(input("Escriba el numero a sumar-- "))
                resultado=resultado*num2
                print(f"{num1}x{num2}={resultado}")
                repetir=True
                while repetir==True:
                    respuesta=input(f"¿Desea continuar multiplicando con {resultado}?-- ").lower()
                    if respuesta== "si" or respuesta=="s":
                        repetir=False
                    elif respuesta=="no" or respuesta=="n":
                        repetir=False
                    else:
                        print("opcion incorrecta. reintentar")
        case "4":

            print("HA ELEGIDO DIVIDIR")
            resultado=float(input("Escriba el primer numero-- "))
            respuesta="s"
            while respuesta in ("si", "s"):
                num1=resultado
                num2=float(input("Escriba el numero a sumar-- "))
                resultado=resultado/num2
                print(f"{num1}/{num2}={resultado}")
                repetir=True
                while repetir==True:
                    respuesta=input(f"¿Desea continuar dividiendo con {resultado}?-- ").lower()
                    if respuesta== "si" or respuesta=="s":
                        repetir=False
                    elif respuesta=="no" or respuesta=="n":
                        repetir=False
                    else:
                        print("opcion incorrecta. reintentar")
        case "5":
            