import random
import csv
from statistics import geometric_mean

trabajadores =["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanzhez","Isabel Gomez","Francisco Diaz","Elena Fernandez" ]
sueldo=[]

def Asignar_sueldos():
    for al in range(0,10) :
        sue=random.randrange(300000,2500000)
        sueldo.append(sue)
    print("Sueldos Creados")
        
def clasificar_sueldos():
    if not sueldo:
        print("No hay sueldos registrados, por favor registre sueldos")
    else:
        sueldo1 = 0
        sueldo2 = 0
        sueldo3 = 0
        print("Nombre Empleado     Sueldo")
        for num in range(0,10):
            if sueldo[num] < 800000:
                print(f"{trabajadores[num]}     {sueldo[num]} ")
                sueldo1= sueldo1+1
        print(f"Sueldos menores a $800.000 TOTAL:{sueldo1}\n")

        print("Nombre Empleado     Sueldo")
        for num in range(0,10):
            if (sueldo[num] >= 800000) and (sueldo[num] <= 2000000):
                print(f"{trabajadores[num]}        {sueldo[num]}")
                sueldo2= sueldo2+1
        print(f"Sueldos entre $800.000 y $2.000.000 TOTAL:{sueldo2}\n")

        print("Nombre Empleado     Sueldo")
        for num in range(0,10):
            if sueldo[num] > 2000000:
                print(f"{trabajadores[num]}        {sueldo[num]}")
                sueldo3= sueldo3+1
        print(f"Sueldos superiores $2.000.000 TOTAL:{sueldo3}\n")

def ver_estadistica():
    if not sueldo:
        print("No hay sueldos registrados, por favor registre sueldos")
    else:
        mayor = sueldo[1]
        for num in range(0,9):
            if sueldo[num] < sueldo[num+1]:
                mayor = sueldo[num]+1
        print(f"sueldo mas alto:{mayor}")

        menor = sueldo[1]
        for num in range(0,9):
            if sueldo[num] > sueldo[num+1]:
                menor = sueldo[num]+1
        print(f"Sueldo mas bajo:{menor}")
        promedio = 0
        for num in range(0,10):
            promedio = promedio + sueldo[num] 
            promedio=promedio/10
        print(f"El promedio es:{promedio}")
        media_geometrica = 0
    
            

def reporte_sueldos():
    if not sueldo:
        print("No hay sueldos registrados, por favor registre sueldos")
    else:
        print("Nombre Empleado     Sueldo Base     Descuento Salud       Descuento AFP       Sueldo Liquido")

        for num in range(0,10):
                descuento_salud=sueldo[num]*0.07
                descuento_afp=sueldo[num]*0.12
                sueldo_liquido = sueldo[num] - descuento_salud - descuento_afp
                print(f"{trabajadores[num]}          {sueldo[num]}           {descuento_salud}           {descuento_afp}        {sueldo_liquido}")

    
def main():
    while True:

        opcion = (input("Escriba el numero que desea ejecutar:\n(1)Asignar Sueldos\n(2)Clasificar Sueldo\n(3)Ver Estadistica\n(4)Reporte Sueldos\n(5)Salir\n"))
        if opcion == "1":
            Asignar_sueldos()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadistica()
        elif opcion == "4":
            reporte_sueldos()
        elif opcion == "5":
            print("Finalizando programa...")
            print("Desarrolado por Bastian Gutierrez")
            print("RUT 21.306.320-0")
            break
        else:
            print("Error, Numero invalido")

if 1== 1:
    main()