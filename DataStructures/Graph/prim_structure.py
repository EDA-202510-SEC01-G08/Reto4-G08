from DataStructures.Map import map_linear_probing as map
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Queue import queue as q
from DataStructures.Graph import digraph as dg


def new_prim_structure(source, g_order):
    """
    Crea una estructura de busqueda usada en el algoritmo **prim**.

    Se crea una estructura de busqueda con los siguientes atributos:

    - **source**: Vertice de inicio del MST.
    - **edge_from**: Mapa con los vertices visitados. Se inicializa en ``None``
    - **dist_to**: Mapa con las distancias a los vertices. Se inicializa en ``None``
    - **marked**: Mapa con los vertices visitados. Se inicializa en ``None``
    - **pq**: Cola de prioridad indexada (index_priority_queue). Se inicializa en ``None``

    :returns: Estructura de busqueda
    :rtype: prim_search
    """

    structure = {
        "source": source,
        "edge_from": map.new_map(g_order, 0.5),
        "dist_to": map.new_map(g_order, 0.5),
        "marked": map.new_map(g_order, 0.5),
        "pq":  pq.new_heap(),
    }

    return structure

def eager_prim(my_graph, source):
    prim_structure = new_prim_structure(source, dg.order(my_graph))
    for v in dg.vertices(my_graph):
        map.put(prim_structure["dist_to"], v, float("inf"))
        map.put(prim_structure["marked"], v, False)
    map.put(prim_structure["dist_to"], source, 0)
    map.put(prim_structure["edge_from"], source, None)
    pq.insert(prim_structure["pq"], (source, 0))

    while not pq.is_empty(prim_structure["pq"]):
        vertex = pq.get_first_priority(prim_structure["pq"])[0]
        map.put(prim_structure["marked"], vertex, True)
        adjacents = dg.adjacents(my_graph, vertex)
        for adj in adjacents:
            if not map.contains(prim_structure["marked"], adj):
                edge = dg.get_edge(my_graph, vertex, adj)
                weight = edge["weight"]
                if weight < map.get(prim_structure["dist_to"], adj):
                    map.put(prim_structure["dist_to"], adj, weight)
                    map.put(prim_structure["edge_from"], adj, vertex)
                    pq.insert(prim_structure["pq"], (adj, weight))
    return prim_structure
                    