import requests
import statistics
import math

URL = "https://abkiluminacion.com/api/random-array"

NOMBRE_ALUMNO = ""

try:
    print("Llamando al API...")

    respuesta = requests.get(URL, timeout=10)
    respuesta.raise_for_status()

    datos = respuesta.json()

    # Validación de estructura
    if not isinstance(datos, dict):
        raise ValueError("La respuesta no tiene formato JSON válido.")

    arreglo = datos.get("data")

    if arreglo is None:
        raise ValueError("No existe la llave 'data'.")

    if not isinstance(arreglo, list):
        raise ValueError("'data' debe ser un arreglo.")

    if len(arreglo) == 0:
        raise ValueError("El arreglo recibido está vacío.")

    # Validar que todos los elementos sean numéricos
    for valor in arreglo:
        if not isinstance(valor, (int, float)):
            raise ValueError(f"Valor no numérico encontrado: {valor}")

    print("\nArreglo recibido:")
    print(arreglo)

    # ==========================
    # Cálculos estadísticos
    # ==========================

    # Media
    media = sum(arreglo) / len(arreglo)

    # Mediana
    mediana = statistics.median(arreglo)

    # Moda
    frecuencias = {}
    for numero in arreglo:
        frecuencias[numero] = frecuencias.get(numero, 0) + 1

    max_frecuencia = max(frecuencias.values())

    modas = [
        numero
        for numero, frecuencia in frecuencias.items()
        if frecuencia == max_frecuencia
    ]

    # Si todos aparecen una sola vez no existe moda
    if max_frecuencia == 1:
        moda = None
    else:
        moda = modas

    # Varianza poblacional
    varianza = sum((x - media) ** 2 for x in arreglo) / len(arreglo)

    # Desviación estándar poblacional
    desviacion_estandar = math.sqrt(varianza)

    # ==========================
    # Resultados
    # ==========================

    print("\nRESULTADOS CALCULADOS")
    print(f"Media ................: {media}")
    print(f"Mediana ..............: {mediana}")

    if moda is None:
        print("Moda .................: No existe moda")
    else:
        print(f"Moda .................: {moda}")

    print(f"Varianza (poblacional): {varianza}")
    print(f"Desviación Estándar ..: {desviacion_estandar}")

    # Datos del oráculo (si existen)
    datos_oraculo = datos.get("result")

    if datos_oraculo:
        print("\nRESULTADOS ORÁCULO")
        print(f"Media ................: {datos_oraculo.get('media')}")
        print(f"Mediana ..............: {datos_oraculo.get('mediana')}")
        print(f"Moda .................: {datos_oraculo.get('moda')}")
        print(f"Varianza (poblacional): {datos_oraculo.get('varianza')}")
        print(
            f"Desviación Estándar ..: "
            f"{datos_oraculo.get('desviacion_estandar')}"
        )

except requests.exceptions.Timeout:
    print("ERROR: Tiempo de espera agotado.")

except requests.exceptions.ConnectionError:
    print("ERROR: No fue posible conectarse al API.")

except requests.exceptions.HTTPError as e:
    print(f"ERROR HTTP: {e}")

except ValueError as e:
    print(f"ERROR DE VALIDACIÓN: {e}")

except Exception as e:
    print(f"ERROR inesperado: {e}")

finally:
    print(f"\nAlumno: {NOMBRE_ALUMNO}")