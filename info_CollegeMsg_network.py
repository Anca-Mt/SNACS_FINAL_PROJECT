import networkx as nx

def load_temporal_graph(network_path):
    graph = nx.DiGraph()

    with open(network_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            info_per_line = line.strip().split()
            if len(info_per_line) == 3:
                node1 = int(info_per_line[0])
                node2 = int(info_per_line[1])
                timestamp = int(info_per_line[2])
                graph.add_edge(node1, node2, label=timestamp)
            else:
                continue

    return graph

if __name__ == '__main__':
    network_path = 'networks_raw/CollegeMsg/CollegeMsg.txt'
    network_graph = load_temporal_graph(network_path)

    print("Number of nodes: ", network_graph.number_of_nodes())
    print("Number of edges: ", network_graph.number_of_edges())
