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
    catalog = {"grafo" : gr.new_graph(dirigido=False),
               "info_tiempo": mp.new_map(10000, 0.5)}            
    
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    graph = catalog["grafo"]
    info_tiempo = catalog["info_tiempo"]

    total_domicilios = 0
    domiciliarios = []
    restaurantes = []
    destinos = []

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
                if not gr.contains_vertex(graph, origen):
                    tabla_origen = mp.new_map(10000, 0.5)
                    gr.insert_vertex(graph, origen, tabla_origen)
                    mp.put(tabla_origen, pedido_id, domiciliario_id)
                else:
                    tabla_origen = gr.get_vertex_information(graph, origen)
                    mp.put(tabla_origen, pedido_id, domiciliario_id)

                if not gr.contains_vertex(graph, destino):
                    tabla_destino = mp.new_map()
                    gr.insert_vertex(graph, destino, tabla_destino)
                    mp.put(tabla_destino, pedido_id, domiciliario_id)
                else:
                    tabla_destino = gr.get_vertex_information(graph, destino)
                    mp.put(tabla_destino, pedido_id, domiciliario_id)

                # Clave para guardar la acumulación de tiempos
                clave_arista = origen + "->" + destino

                # Agregar o actualizar la arista
                if gr.get_edge(graph, origen, destino) is None:
                    mp.put(info_tiempo, clave_arista, [tiempo, 1])
                else:
                    mp.remove(graph["vertices"][mp.get(graph["vertices"], origen)]["adjacents"], destino)
                    mp.remove(graph["vertices"][mp.get(graph["vertices"], destino)]["adjacents"], origen)
                    suma, cuenta = mp.get(info_tiempo, clave_arista)
                    suma += tiempo
                    cuenta += 1
                    promedio = suma // cuenta
                    mp.put(info_tiempo, clave_arista, [suma, cuenta])
                    gr.add_edge(catalog, origen, destino, promedio)

                total_domicilios += 1
                suma_tiempos += tiempo
                if domiciliario_id not in domiciliarios:
                    domiciliarios.append(domiciliario_id)
                if origen not in restaurantes:
                    restaurantes.append(origen)
                if destino not in destinos:
                    destinos.append(destino)

            except:
                # Por si hay filas con errores 
                continue
    # Número de arcos (no dirigidos, contar solo una vez)
    num_arcos = len(graph["edges"])//2 if hasattr(gr, 'num_edges') else len(set(
        tuple(sorted(edge)) for edge in graph["edges"]
    ))  

    return {
        "total_domicilios": total_domicilios,
        "total_domiciliarios": len(domiciliarios),
        "total_nodos": len(graph["vertices"]),
        "total_arcos": num_arcos,
        "total_restaurantes": len(restaurantes),
        "total_destinos": len(destinos),
        "promedio_tiempo": (suma_tiempos / total_domicilios) if total_domicilios > 0 else 0
    }

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
