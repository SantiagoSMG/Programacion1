# Calculadora de viajes hecho en Pseint
total_km_recorridos = 0
litros_consumidos = 0
viajes = 0
viajes1 = 0
dias = 0
gas1 = 0
terminar = False
viajes = int(input("Ingrese los viajes realizados durante el mes: "))
while not terminar:
    dias = int(input("Ingrese el número de días que trabajó durante el mes: "))
    litros_consumidos = float(input("Ingrese los litros consumidos de gasolina en el mes: "))
    viajes1 = int(input("Ingrese el día que hizo más viajes recorridos: "))
    gas1 = float(input("Ingrese cuánta gasolina gastó en ese día: "))
    total_km_recorridos = float(input("Ingrese los kilómetros recorridos en el mes: "))
    if not terminar:
        promedio_km_recorridos = total_km_recorridos * viajes / dias
        rendimiento_del_vehiculo = total_km_recorridos / litros_consumidos
        print(f"Su promedio de kilómetros recorridos es {promedio_km_recorridos:.2f} km")
        print(f"El rendimiento de su vehículo durante el mes es de {rendimiento_del_vehiculo:.2f} km/l")
    opcion = input("¿Desea realizar otro cálculo? (si/no): ").lower()
    if opcion != 'si':
        print("Hasta luego ¡vuelva pronto!")
        terminar = True
