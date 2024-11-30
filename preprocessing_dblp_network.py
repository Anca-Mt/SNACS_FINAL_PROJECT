
def extract_edges(input_path, output_path):
    edges = []

    with open(input_path, 'r') as f:
        for line in f:
            if line.startswith('e'):
                parts = line.strip().split()
                if len(parts) == 4:
                    node1 = int(parts[1])
                    node2 = int(parts[2])
                    timestamp = int(parts[3])
                    edges.append(f"{node1} {node2} {timestamp}")
                else: print(f"The edge {parts} is invalid and cannot be used.")

    with open(output_path, 'w') as out:
        out.write("\n".join(edges) + "\n")

if __name__ == '__main__':

    input_gs_path = 'networks_raw/dblp/dblp.years_1992_2002.gs'
    output_txt_path = 'networks_preprocessed/dblp/dblp_network.txt'

    extract_edges(input_gs_path, output_txt_path)
    print(f"The preprocessed dblp network has been saved to {output_txt_path}")