import helpers as graph

# # First
# graph_struct = graph.build_struct_from_array()
# G = graph.create_from_struct(graph_struct)

# # Second
G = graph.create_from_array()

graph.draw_networkx(G)