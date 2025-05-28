import time
import csv
from DataStructures.Graph import digraph as gr     
from DataStructures.Map import map_linear_probing as mp 
from DataStructures.List import array_list as ar
from DataStructures.Graph import bfs as bfs
from DataStructures.Graph import dfs as dfs
from DataStructures.Stack import stack as st
from DataStructures.Graph import dijsktra_structure as ds
from DataStructures.Graph import prim_structure as ps

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {"grafo" : gr.new_graph(False),
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
    suma_tiempos = 0

    with open(filename, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
                pedido_id = fila["ID"]
                domiciliario_id = fila["Delivery_person_ID"]
                tipo_vehiculo = fila["Type_of_vehicle"]
                tiempo = int(fila["Time_taken(min)"])

                lat_rest = round(float(fila["Restaurant_latitude"]), 4)
                lon_rest = round(float(fila["Restaurant_longitude"]), 4)
                lat_dest = round(float(fila["Delivery_location_latitude"]), 4)
                lon_dest = round(float(fila["Delivery_location_longitude"]), 4)

                origen = str(lat_rest) + "," + str(lon_rest)
                destino = str(lat_dest) + "," + str(lon_dest)

                # Crear vértices si no existen
                if not gr.contains_vertex(graph, origen):
                    tabla_origen = mp.new_map(10000, 0.5)
                    gr.insert_vertex(graph, origen, (tabla_origen, True))
                    mp.put(tabla_origen, pedido_id, {"domiciliario_id": domiciliario_id, "vehiculo": tipo_vehiculo})
                    
                else:
                    tabla_origen = gr.get_vertex_information(graph, origen)[0]
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
                    gr.add_edge(graph, origen, destino, tiempo)
                    mp.put(info_tiempo, clave_arista, [tiempo, 1])
                else:
                    v_origen = mp.get(graph["vertices"], origen)
                    v_destino = mp.get(graph["vertices"], destino)
                    mp.remove(v_origen["adjacents"], destino)
                    mp.remove(v_destino["adjacents"], origen)
                    suma, cuenta = mp.get(info_tiempo, clave_arista)
                    suma += tiempo
                    cuenta += 1
                    promedio = suma // cuenta
                    mp.put(info_tiempo, clave_arista, [suma, cuenta])
                total_domicilios += 1
                suma_tiempos += tiempo
                if domiciliario_id not in domiciliarios["elements"]:
                    ar.add_last(domiciliarios, domiciliario_id)
                if origen not in restaurantes["elements"]:
                    ar.add_last(restaurantes, origen)
                if destino not in destinos["elements"]:
                    ar.add_last(destinos, destino)
    # Número de arcos (no dirigidos, contar solo una vez)
    num_arcos = graph["num_edges"] // 2

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

    dfs_result = dfs.dfs(grafo, origen)

    if not dfs.has_path_to(dfs_result, destino):
        return 0

    camino = bfs.path_to(dfs_result, destino)  # lista de ubicaciones desde origen a destino
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

def req_6(catalog, origen):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    startf_time = get_time()
    graph = catalog["grafo"]
    dijkstra_structure = ds.dijkstra(graph, origen)
    num_ubicaciones = dijkstra_structure["visited"]["size"]
    if num_ubicaciones == 0:
        return None
    tiempo_max = 0
    key_max = None
    alcanzables = ar.new_list()
    for key in dijkstra_structure["visited"]["table"]["elements"]:
        if key is not None and key != "__EMPTY__":
            tiempo = ds.dist_to(key, dijkstra_structure)
            if tiempo > tiempo_max:
                tiempo_max = tiempo
                key_max = key
            ar.add_last(alcanzables, key)
    ordered_list = ar.merge_sort(alcanzables, sort_crit_6)
    path_max = ds.path_to(key_max, dijkstra_structure)
    end_time = get_time()
    tiempo = str(round(delta_time(startf_time, end_time), 2)) + "ms"
    return [tiempo, num_ubicaciones, ordered_list, path_max, tiempo_max]

def sort_crit_6(element1, element2):
    if element1 > element2:
        return True
    else:
        return False
def req_7(catalog, origen, domiciliario):
    graph = catalog["grafo"]
    start_time = get_time()
    if not gr.contains_vertex(graph, origen):
        return None
    else:
        prim = req_7_mask(graph, origen, domiciliario, ps.eager_prim(graph, origen))
        marked = prim["marked"]
        num_ubicaciones = mp.size(marked)
        if num_ubicaciones <= 1:
            return 0
        else:
            visited = ar.new_list()
            for i in range(num_ubicaciones):
                vertex = ar.get_element(marked["table"], i)["key"]
                if vertex is not None and vertex != "__EMPTY__":
                    ar.add_last(visited, vertex)
            ordered_list = ar.merge_sort(visited, sort_crit_6)
            tiempo_mst = 0
            dist_to = prim["dist_to"]["table"]["elements"]
            for z in dist_to:
                if z is not None and z != "__EMPTY__":
                    tiempo_mst += z
            end_time = get_time()
            tiempo = str(round(delta_time(start_time, end_time), 2)) + "ms"
            return [tiempo, num_ubicaciones, ordered_list, tiempo_mst]

def req_7_mask(grafo, origen, domiciliario, mst):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    if not gr.contains_vertex(grafo, origen):
        return None
    else:
        visited = mst["marked"]
        good_prim = True
        x = 0
        while x < mp.size(visited) and good_prim == True:
            vertex = ar.get_element(visited["table"], x)
            if vertex is not None and vertex != "__EMPTY__":
                tabla_info = gr.get_vertex_information(grafo, vertex)[0]
                pedidos = mp.key_set(tabla_info)
            
                i = 0
                while i < pedidos["size"] and good_prim == True:
                    ped_id = ar.get_element(pedidos["elements"],i)
                    pedido_info = mp.get(tabla_info, ped_id)
                    if pedido_info["domiciliario_id"] != domiciliario:
                        good_prim = False
        if good_prim == False:
            gr.remove_vertex(grafo, vertex)
            new_mst = ps.eager_prim(grafo, origen)
            return req_7_mask(grafo, origen, domiciliario, new_mst)
        else: 
            return mst


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
