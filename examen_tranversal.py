import random
import csv
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos=[]

def sueldos_aleatorios(sueldos_random):
    
    for trabajador in trabajadores:    
        sueldos_random=random.randint(300000,2500000)
        print(f"el sueldo de {trabajador} es de :{sueldos_random}")
        sueldos.append(sueldos_random)
def clasificar_sueldos(sueldos):
    total_sueldo_bajo=0
    total_sueldo_medio=0
    total_sueldo_alto=0
    for  s in sueldos:
        if s <800000:
            total_sueldo_bajo+=1 
        elif s >=800000 and s <2000000:
            total_sueldo_medio+=1
        elif s > 2000000:
            total_sueldo_alto+=1 
    
    print(f"sueldos menores a 800.000 total:{total_sueldo_bajo}")
    
    print(f"sueldos mayores o igual a 800.000 total:{total_sueldo_medio}")
    print(f"sueldos mayores a 2.000.000 total:{total_sueldo_alto}")
def ver_estadisticas(sueldos):
    pass
def reporte_de_sueldos():
    for sueldo_calculado in sueldos:
        salud = sueldo_calculado/100*7 
        afp=sueldo_calculado/100*12
        sueldo_liquido=sueldo_calculado-salud-afp
    with open('reporte_sueldos.csv','w',newline="") as archivo:
        escritor_csv=csv.writer(archivo)
        escritor_csv.writerow(['Nombre empleado', 'sueldo base', 'descuento salud', 'descuento afp', 'sueldo liquido'])
        for t in trabajadores:
            escritor_csv.writerow(["nombre empleado:",t, "sueldo base:",sueldo_calculado,"descuento salud:", salud,"descuento afp:", afp ,"sueldo liquido:", sueldo_liquido])
    
    
    
while True:
    print("1.-asignar sueldos aleatorios ")
    print("2.-Clasificar sueldos")
    print("3.-Ver estadísticas.")
    print("4.-reporte de sueldos")
    print("5.-salir")
    opcion=int(input("ingrese la opcion que desea:"))
    match opcion:
        case 1:
            sueldos_aleatorios(trabajadores)
        case 2:
            clasificar_sueldos(sueldos)
        case 3:
            ver_estadisticas(sueldos)
        case 4:
            reporte_de_sueldos()
        case 5:
            print("programa finalizado")
            print("desarrollado por Gabriel Cuevas")
            print("rut 21.827.124-3")
    
