
def preprocess_to_undirected(input_path, output_path):
    seen_edges = set()
    undirected_edges = []

    with open(input_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                node1 = int(parts[0])
                node2 = int(parts[1])
                timestamp = int(parts[2])

                edge = tuple(sorted([node1, node2]))
                if edge not in seen_edges:
                    seen_edges.add(edge)
                    undirected_edges.append(f"{edge[0]} {edge[1]} {timestamp}")
            else:
                continue

    with open(output_path, 'w') as out:
        out.write("\n".join(undirected_edges) + "\n")


if __name__ == '__main__':
    input_txt_path = 'networks_raw/CollegeMsg/CollegeMsg.txt'
    output_txt_path = 'networks_preprocessed/CollegeMsg/CollegeMsg_network.txt'

    preprocess_to_undirected(input_txt_path, output_txt_path)
    print(f"Undirected CollegeMsg network saved to {output_txt_path}")