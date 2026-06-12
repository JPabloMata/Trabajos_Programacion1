pcion=0
print("CALCULADORA")
while opcion!="5":
    print("Escribe el numero para acceder a la opcion")
    print("1: SUMAR")
    print("2: RESTAR")
    print("3: MULTIPLICAR")
    print("4: DIVIDIR")
    print("5: SALIR")
    opcion=input()

    match opcion:

        case "1":
            print("HA ELEGIDO SUMAR")
            num1=(input("Escriba el primer numero-- ")).lower()
            if num1=="ans":
                resultado=resultado
            else:
                resultado=float(num1)
            respuesta="s"
            while respuesta in ("si", "s"):
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
            num1=(input("Escriba el primer numero-- ")).lower()
            if num1=="ans":
                resultado=resultado
            else:
                resultado=float(num1)
            respuesta="s"
            while respuesta in ("si", "s"):
                num2=float(input("Escriba el numero a restar-- "))
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
            num1=(input("Escriba el primer numero-- ")).lower()
            if num1=="ans":
                resultado=resultado
            else:
                resultado=float(num1)
            respuesta="s"
            while respuesta in ("si", "s"):
                num2=float(input("Escriba el numero a multiplicar-- "))
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
            num1=(input("Escriba el primer numero-- ")).lower()
            if num1=="ans":
                resultado=resultado
            else:
                resultado=float(num1)
            respuesta="s"
            while respuesta in ("si", "s"):
                num2=float(input("Escriba el numero a dividir-- "))
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