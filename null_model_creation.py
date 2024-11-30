import random

"""The null model is created by shuffling the timestamps of the edges"""

# To run the shuffling you need to choose one of the two available networks:
NETWORKS = [
    "dblp",
    "CollegeMsg"
]

def shuffle_timestamps(input_path, output_path):

    edges = []
    timestamps = []

    with open(input_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                node1 = parts[0]
                node2 = parts[1]
                timestamp = int(parts[2])
                edges.append((node1, node2, timestamp))
                timestamps.append(timestamp)

    random.shuffle(timestamps)

    null_model_edges = [
        (node1, node2, shuffled_timestamp)
        for (node1, node2, _), shuffled_timestamp in zip(edges, timestamps)
    ]

    with open(output_path, 'w') as out_file:
        for edge in null_model_edges:
            out_file.write(f"{edge[0]} {edge[1]} {edge[2]}\n")

if __name__ == '__main__':

    ORIGINAL_NETWORK = "CollegeMsg"
    no_runs = 10 # number of runs / number of null models to be created

    input_path = f"networks_preprocessed/{ORIGINAL_NETWORK}/{ORIGINAL_NETWORK}_network.txt"

    for idx in range(1, no_runs+1):
        output_path = f"null_models/{ORIGINAL_NETWORK}/{ORIGINAL_NETWORK}_null_model_{idx}.txt"
        shuffle_timestamps(input_path, output_path)
        print(f"Null model number {idx} for {ORIGINAL_NETWORK} network was created!")
