import numpy as np
import matplotlib.pyplot as plt


def plot_patterns(patterns, network):

    plt.figure(figsize=(6, 4))
    plt.imshow(patterns, cmap="Oranges", interpolation="nearest")

    cbar = plt.colorbar()
    cbar.set_label("Pattern Count", fontsize=12)

    for i in range(patterns.shape[0]):
        for j in range(patterns.shape[1]):
            text = f"{int(patterns[i, j])}" if patterns[i, j] != 0 else "0"
            plt.text(j, i, text, ha="center", va="center",
                     color="white" if patterns[i, j] > np.max(patterns) / 2 else "black")

    # Add axis labels and title
    plt.xlabel("Column (j)", fontsize=12)
    plt.ylabel("Row (i)", fontsize=12)
    plt.title(f"Number of Patterns in {network} Network", fontsize=14)
    plt.xticks(range(patterns.shape[1]), [f"j={j + 1}" for j in range(patterns.shape[1])])
    plt.yticks(range(patterns.shape[0]), [f"i={i + 1}" for i in range(patterns.shape[0])])

    plt.tight_layout()
    plt.savefig(f"plots/patterns_heatmap_{network}.png")

if __name__ == "__main__":
    NETWORK = 'dblp'

    results_original_network = f"results/original_networks/{NETWORK}/results_{NETWORK}.txt"
    patterns_original_network = np.loadtxt(results_original_network)

    plot_patterns(patterns_original_network, network=NETWORK)