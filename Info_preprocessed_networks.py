import networkx as nx
from tqdm import tqdm
import json
from statistics import mean
import random

def extract_statistics(network, sample_size):
    no_nodes = network.number_of_nodes()
    no_edges = network.number_of_edges()

    connected_components = list(nx.connected_components(network))
    largest_connected_component = max(connected_components, key=len)
    largest_connected_subgraph = network.subgraph(largest_connected_component)

    no_connected_components = len(connected_components)
    no_nodes_largest_connected = largest_connected_subgraph.number_of_nodes()
    no_links_largest_connected = largest_connected_subgraph.number_of_edges()

    clustering_coeff_nodes = nx.clustering(network)
    avg_clustering_coeff = mean(clustering_coeff_nodes.values())

    sample_size_nodes = int(sample_size * len(largest_connected_subgraph .nodes()))
    sampled_nodes = random.sample(list(largest_connected_subgraph .nodes()), sample_size_nodes)
    sampled_subgraph_nodes = largest_connected_subgraph.subgraph(sampled_nodes)
    no_nodes_sampled = sampled_subgraph_nodes.number_of_nodes()

    distances = []
    for node, dist in tqdm(nx.all_pairs_shortest_path_length(sampled_subgraph_nodes),total= no_nodes_sampled, desc=
    " Calculating distances "):
        distances.extend(dist.values())

    avg_distance = average_distance(distances)

    return {
        'no_nodes': no_nodes,
        'no_edges': no_edges,
        'no_connected_components': no_connected_components,
        'no_nodes_largest_connected_component': no_nodes_largest_connected,
        'no_links_largest_connected_component': no_links_largest_connected,
        'avg_clustering': avg_clustering_coeff,
        'avg_distance': avg_distance
    }

def average_distance(distances):
    # We do not consider the distances = 0 ( between a node and itself )
    valid_distances = [ dist for dist in distances if dist > 0]
    valid_pairs = len(valid_distances)
    if len (valid_distances) == 0:
        avg_dist = 0
    else :
        avg_dist = sum( valid_distances ) / valid_pairs
    return avg_dist


def load_preprocessed_network(file_path):

    G = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                node_source = int(parts[0])
                node_destination = int(parts[1])
                timestamp = int(parts[2])

                G.add_edge(node_source, node_destination, timestamp=timestamp)
    return G


if __name__ == '__main__':

    NETWORK_NAME = "dblp" # "dblp" or "CollegeMsg"
    NETWORK_PATH = f"networks_preprocessed/{NETWORK_NAME}/{NETWORK_NAME}_network.txt"

    network = load_preprocessed_network(NETWORK_PATH)
    network_statistics = extract_statistics(network, sample_size=0.25)
    print(json.dumps(network_statistics, indent=2))
