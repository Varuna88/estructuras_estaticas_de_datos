"""Crear un programa que permita convertir una cantidad de segundos en horas, minutos segundos."""

total_seg = int(input("Ingresa una cantidad de Segundos: "))

horas = total_seg // 3600 

resto_seg = total_seg % 3600

minutos = resto_seg // 60
seg_finales = resto_seg % 60

print(f"{horas}h {minutos}m {seg_finales}s")
