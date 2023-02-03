import networkx as nx
import data

def build_struct_from_array(city_list=data.get_from_file()):
    graph = {}
    for row in city_list:
        if row[0] not in graph:
            graph[row[0]] = []
        graph[row[0]].append(row[1])
    return graph

def create_from_struct(graph, city_list=data.get_from_file()):
    g = nx.Graph(graph)
    for row in city_list:
        g[row[0]][row[1]]['distance'] = row[2]
    return g

def create_from_array(city_list=data.get_from_file()):
    g = nx.Graph()
    for row in city_list:
        g.add_edge(row[0], row[1], distance=row[2])
    return g

def draw_networkx(g):
    return nx.draw_networkx(g)

def shortest_path(source, target, city_list=data.get_from_file()):
    g = create_from_array(city_list)
    return nx.shortest_path(g, source, target)

def shortest_path_and_length(source, target, city_list=data.get_from_file()):
    g = create_from_array(city_list)
    path = nx.shortest_path(g, source, target)
    distance = 0
    i = 1
    while len(path) > i:
        distance += int(g[path[i-1]][path[i]]['distance'])
        i += 1

    return path, distance
