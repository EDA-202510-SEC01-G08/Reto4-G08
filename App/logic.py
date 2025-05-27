import time
import csv
from DataStructures.Graph import digraph as gr     
from DataStructures.List import single_linked_list as lt
from DataStructures.Map import map_linear_probing as mp  
from DataStructures import list as lt
from DataStructures.List import array_list as ar
from DataStructures.Graph import bfs as bfs
from DataStructures.Graph import dfs as dfs
from DataStructures.Stack import stack as st

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
    domiciliarios = ar.new_list()
    restaurantes = ar.new_list()
    destinos = ar.new_list()

    with open(filename, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                pedido_id = fila["ID"]
                domiciliario_id = fila["Delivery_person_ID"]
                tipo_vehiculo = fila["Vehicle_type"]
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
                    gr.insert_vertex(graph, origen, (tabla_origen, True))
                    mp.put(tabla_origen, pedido_id, {"domiciliario_id": domiciliario_id, "vehiculo": tipo_vehiculo})
                else:
                    tabla_origen = gr.get_vertex_information(graph, origen)
                    mp.put(tabla_origen, pedido_id, {"domiciliario_id": domiciliario_id, "vehiculo": tipo_vehiculo})

                if not gr.contains_vertex(graph, destino):
                    tabla_destino = mp.new_map(10000, 0.5)
                    gr.insert_vertex(graph, destino, (tabla_destino, False))
                    mp.put(tabla_origen, pedido_id, {"domiciliario_id": domiciliario_id, "vehiculo": tipo_vehiculo})
                   
                else:
                    tabla_destino = gr.get_vertex_information(graph, destino)
                    mp.put(tabla_origen, pedido_id, {"domiciliario_id": domiciliario_id, "vehiculo": tipo_vehiculo})

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
                if domiciliario_id not in domiciliarios["elements"]:
                    ar.add_last(domiciliarios, domiciliario_id)
                if origen not in restaurantes["elements"]:
                    ar.add_last(restaurantes, origen)
                if destino not in destinos["elements"]:
                    ar.add_last(destinos, destino)

            except:
                # Por si hay filas con errores 
                continue
    # Número de arcos (no dirigidos, contar solo una vez)
    num_arcos = len(graph["edges"])//2 if hasattr(gr, 'num_edges') else len(set(
        tuple(sorted(edge)) for edge in graph["edges"]
    ))  

    return {
        "total_domicilios": total_domicilios,
        "total_domiciliarios": domiciliarios["size"],
        "total_nodos": graph["vertices"]["table"]["size"],
        "total_arcos": num_arcos,
        "total_restaurantes": restaurantes["size"],
        "total_destinos": destinos["size"],
        "promedio_tiempo": (suma_tiempos / total_domicilios) if total_domicilios > 0 else 0
    }

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog,origen,destino):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    grafo = catalog["grafo"]
    start_time = get_time()


    if not gr.contains_vertex(grafo, origen) or not gr.contains_vertex(grafo, destino):
        return None

    bfs_result = bfs.bfs(grafo, origen)

    if not bfs.has_path_to(bfs_result, destino):
        return 0

    camino = bfs.path_to(bfs_result, destino)  # lista de ubicaciones desde origen a destino
    cantidad_puntos = st.size(camino)

    domiciliarios = ar.new_list()
    restaurantes = ar.new_list()

    for i in range(cantidad_puntos):
        punto = ar.get_element(camino,i)
        tabla_info = gr.get_vertex_information(grafo, punto)[0]
        rest = gr.get_vertex_information(grafo, punto)[1]
        if rest:
            ar.add_last(restaurantes, punto)
        info_pedidos = mp.value_set(tabla_info)
        for domicilio in info_pedidos["elements"]:
            domiciliario = domicilio["domiciliario_id"]
            if domiciliario not in domiciliarios["elements"]:
                ar.add_last(domiciliarios, domiciliario)

    end_time = get_time()
    time = str(round(delta_time(start_time, end_time),2)) + "ms"

    return {
        "tiempo": time,
        "cantidad_puntos": cantidad_puntos,
        "domiciliarios": domiciliarios,
        "secuencia_ubicaciones": camino,
        "restaurantes": restaurantes
    }


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog, punto):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = get_time()
    grafo = catalog["grafo"]

    if not gr.contains_vertex(grafo, punto):
        return None

    tabla_pedidos = gr.get_vertex_information(grafo, punto)[0]
    conteo = {}     # clave: domiciliario_id, valor: cantidad de pedidos
    vehiculos = {}  # clave: domiciliario_id, valor: dict con tipos de vehículo y conteo
    pedidos = mp.key_set(tabla_pedidos)
    for pedido_id in pedidos:
        datos = mp.get(tabla_pedidos, pedido_id)
        dom_id = datos["domiciliario_id"]
        vehiculo = datos["vehiculo"]

        if dom_id not in conteo:
            conteo[dom_id] = 1
            vehiculos[dom_id] = {}
        else:
            conteo[dom_id] += 1

        if vehiculo not in vehiculos[dom_id]:
            vehiculos[dom_id][vehiculo] = 1
        else:
            vehiculos[dom_id][vehiculo] += 1

    # Encontrar domiciliario con más pedidos
    max_dom = None
    max_pedidos = 0
    for domi in conteo:
        if conteo[domi] > max_pedidos:
            max_dom = domi
            max_pedidos = conteo[domi]

    # Tipo de vehículo más usado por ese domiciliario
    tipo_vehiculo = None
    max_veces = 0
    for veh in vehiculos[max_dom]:
        veces = vehiculos[max_dom][veh]
        if veces > max_veces:
            tipo_vehiculo = veh
            max_veces = veces

    end_time = get_time()
    time = str(round(delta_time(start_time, end_time), 2)) + "ms"

    return {
        "domiciliario_mas_popular": max_dom,
        "pedidos_totales": max_pedidos,
        "vehiculo_mas_usado": tipo_vehiculo,
        "tiempo": time
    }


def req_4(catalog, punto_a, punto_b):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start_time = get_time()
    grafo = catalog["grafo"]

    if not gr.contains_vertex(grafo, punto_a) or not gr.contains_vertex(grafo, punto_b):
        return None

    # Obtener recorrido desde punto_a usando BFS
    bfs_result = bfs.bfs(grafo, punto_a)

    if not bfs.has_path_to(bfs_result, punto_b):
        return 0

    camino = bfs.path_to(bfs_result, punto_b)
    listas_domiciliarios = ar.new_list()

    for punto in camino["elements"]:
        pedidos = gr.get_vertex_information(grafo, punto)[0]
        lista = ar.new_list()
        info_ped = mp.value_set(pedidos)
        for pedido in info_ped:
            dom_id = pedido["domiciliario_id"]
            if dom_id not in lista["elements"]:
                ar.add_last(lista, dom_id)
        ar.add_last(listas_domiciliarios, lista)

    # Intersección de todas las listas sin usar set

    comunes = ar.new_list()
    primera = listas_domiciliarios[0]
    for dom in primera:
        esta_en_todas = True
        for lista in listas_domiciliarios[1:]:
            if dom not in lista:
                esta_en_todas = False
                break
        if esta_en_todas and dom not in comunes:
            ar.add_last(comunes, dom)

    end_time = get_time()
    tiempo = str(round(delta_time(start_time, end_time), 2)) + "ms"

    return {
        "camino_simple": list(camino),
        "domiciliarios_comunes": comunes,
        "tiempo": tiempo
    }



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
