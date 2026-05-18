import json
import os

def read_data(nombre_archivo):
    ruta_base = os.path.dirname(os.path.dirname(__file__))
    ruta_completa = os.path.join(ruta_base, 'data', nombre_archivo)

    with open(ruta_completa, encoding='utf-8') as f:
        return json.load(f)