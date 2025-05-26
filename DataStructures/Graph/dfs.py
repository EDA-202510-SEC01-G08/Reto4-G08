import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from DataStructures.Stack import stack as st
from DataStructures.Map import map_linear_probing as lp
from DataStructures.List import array_list as ar
from DataStructures.Graph import digraph as dg
from DataStructures.Graph import vertex as ve

def dfs(my_graph, source):
    order = dg.order(my_graph)
    visited_map = lp.new_map(order, 0.5)
    value = {"marked": True, "edge_to": True}
    lp.put(visited_map, source, value)
    visited_map = dfs_vertex(my_graph, source, visited_map)
    return visited_map

def dfs_vertex(my_graph, vertex, visited_map):
    list_of_adjacents = dg.adjacents(my_graph, vertex)
    tamanio = ar.size(list_of_adjacents)
    for i in range(tamanio):
        visited_key = ar.remove_last(list_of_adjacents)
        visited = lp.get(visited_map, visited_key)
        if visited is None:
            lp.put(visited_map, visited_key, {"marked": True, "edge_to": vertex})
            dfs_vertex(my_graph, visited_key, visited_map)
    return visited_map
    
def has_path_to(key_v, visited_map):
    if key_v in visited_map["elements"]:
        return True
    else:
        return False
    
def path_to(key_v, visited_map):
    element = lp.get(visited_map, key_v)
    stack_retorno = st.new_stack()
    if has_path_to(visited_map, key_v) is False:
        return None
    else:
        st.push(stack_retorno, key_v)
        while element and element['marked'] is True and element["edge_to"] != True:
            st.push(stack_retorno, element["edge_to"])
            element = lp.get(visited_map, element["edge_to"])
        return stack_retorno