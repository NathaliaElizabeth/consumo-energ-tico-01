# Cálculo del tiempo de llenado de un tanque en horas
#Nathalia Elizabeth Guano Pillajo
#09 de Junio de 2026
#Versión Github: https://github.com/NathaliaElizabeth/consumo-energ-tico-01.git
zona = input("ingrese la zona (rural,urbano o industrial):").strip().lower()
kw = float(input("Ingrese la potencia en kw:"))
h = float(input("Ingrese las horas de uso:"))
#calcular consumo energético
kwh = kw * h
#decisión según la zona
if zona == "rural":
    C = 0.8
elif zona == "urbano":
    C = 1.0
elif zona == "industrial":
    C = 1.2
else:
    print("Zona no encontrada")
    C = None
#tasa según el consumo
if C is not None:
    if kwh < 0:
        print("Error: la energía no puede ser negativa.")
        tasa = None
    elif kwh >= 150:
        tasa = 0.15
        print("Se aplica tarifa alta.")
    elif 101 <= kwh < 150:
        tasa = 0.11
        print("Se aplica tarifa intermedia.")
    elif 51 <= kwh < 101:
        tasa = 0.09
        print("se aplica tarifa intermedia.")
    else:
        tasa = 0.05
        print("Se aplica tarifa básica.")

    #se calcula el pago
    if C is not None and kwh >= 0:
        pago = kwh * tasa * C
        #se muestran los resultados
        print("consumo:", kwh, "kwh")
        print("cargo por zona:", C)
        print("tasa:", tasa)
        print("pago total:", round(pago, 3), "dólares")
else:
    print("No se puede realizar los cálculos.")
