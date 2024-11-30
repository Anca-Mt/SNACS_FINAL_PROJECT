import networkx as nx

def load_temporal_graph(network_path):
    graph = nx.Graph()

    with open(network_path, 'r') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            info_per_line = line.strip().split()
            if info_per_line[0] == 'v':  # Node: v ID LAB
                node_id = int(info_per_line[1])
                node_label = int(info_per_line[2])
                graph.add_node(node_id, label=node_label)
            elif info_per_line[0] == 'e':
                node1 = int(info_per_line[1])
                node2 = int(info_per_line[2])
                edge_label = int(info_per_line[3])
                graph.add_edge(node1, node2, label=edge_label)
            elif info_per_line[0] == 't':
                count +=1

    return graph

if __name__ == '__main__':

    network_path = 'networks_raw/dblp/dblp.years_1992_2002.gs'
    network_dblp = load_temporal_graph(network_path)

    print("Number of nodes: ", network_dblp.number_of_nodes())
    print("Number of edges: ", network_dblp.number_of_edges())