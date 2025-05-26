import time
import csv
from DataStructures.Graph import digraph as gr     
from DataStructures.List import single_linked_list as lt
from DataStructures.Map import map_linear_probing as mp  
from DataStructures import list as lt
from DataStructures import array as arr

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {
        "grafo": gr.new_graph(dirigido=False),  
        "info_nodos": mp.new_map()              
    }
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    grafo = catalog["grafo"]
    info_nodos = catalog["info_nodos"]

    with open(filename, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                pedido_id = fila["ID"]
                domiciliario_id = fila["Delivery_person_ID"]
                tiempo = int(fila["Time_taken(min)"])

                lat_rest = fila["Restaurant_latitude"]
                lon_rest = fila["Restaurant_longitude"]
                lat_dest = fila["Delivery_location_latitude"]
                lon_dest = fila["Delivery_location_longitude"]

                origen = str(lat_rest) + "," + str(lon_rest)
                destino = str(lat_dest) + "," + str(lon_dest)

                # Crear vértices si no existen
                if not gr.contains_vertex(grafo, origen):
                    gr.insert_vertex(grafo, origen)
                    tabla_origen = mp.new_map()
                    mp.put(tabla_origen, pedido_id, domiciliario_id)
                    mp.put(info_nodos, origen, tabla_origen)
                else:
                    tabla_origen = mp.get(info_nodos, origen)
                    mp.put(tabla_origen, pedido_id, domiciliario_id)

                if not gr.contains_vertex(grafo, destino):
                    gr.insert_vertex(grafo, destino)
                    tabla_destino = mp.new_map()
                    mp.put(tabla_destino, pedido_id, domiciliario_id)
                    mp.put(info_nodos, destino, tabla_destino)
                else:
                    tabla_destino = mp.get(info_nodos, destino)
                    mp.put(tabla_destino, pedido_id, domiciliario_id)

                # Clave para guardar la acumulación de tiempos
                clave_arista = origen + "->" + destino

                # Agregar o actualizar la arista
                if gr.get_edge(grafo, origen, destino) is None:
                    mp.put(info_nodos, clave_arista, [tiempo, 1])
                    gr.add_edge(grafo, origen, destino, tiempo)
                else:
                    suma, cuenta = mp.get(info_nodos, clave_arista)
                    suma += tiempo
                    cuenta += 1
                    promedio = suma // cuenta
                    mp.put(info_nodos, clave_arista, [suma, cuenta])
                    gr.add_edge(grafo, origen, destino, promedio)

            except:
                # Por si hay filas con errores 
                continue

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
