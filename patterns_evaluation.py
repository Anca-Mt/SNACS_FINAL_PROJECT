import numpy as np
import os
import matplotlib.pyplot as plt

def compute_z_scores(original_network, null_models):

    mean = np.mean(null_models, axis=0)
    std = np.std(null_models, axis=0)
    # print(mean)
    # print(std)

    z_scores_dict = {}

    for i in range(original_network.shape[0]):
        for j in range(original_network.shape[1]):
            if original_network[i][j] != 0: # undirected patterns
                if std[i][j] != 0:
                    z_score = (original_network[i][j] - mean[i][j]) / std[i][j]
                else:
                    z_score = np.nan

                pattern = f"M({i + 1},{j + 1})"
                z_scores_dict[pattern] = z_score
                print(f"{pattern}: {z_score:.4f}")

    return z_scores_dict

def plot_z_scores(z_scores_dict, network):
    patterns = list(z_scores_dict.keys())
    z_scores = list(z_scores_dict.values())

    plt.figure(figsize=(6, 4))
    plt.bar(patterns, z_scores, color='blue', edgecolor='black')

    plt.xlabel("Patterns (M(i,j))", fontsize=12)
    plt.ylabel("Z-score", fontsize=12)
    plt.title(f"Z-scores for the Patterns in {network} Network", fontsize=14)
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axhline(1.96, color='red', linewidth=0.8, linestyle='--')
    plt.axhline(-1.96, color='red', linewidth=0.8, linestyle='--')
    plt.tight_layout()
    plt.savefig(f"plots/z_scores_{network}.png")

    print(f"The visualization plot for the z-scores of the {network} network was saved")

def combine_null_models(null_models_dir_path):
    null_models = []
    for file in sorted(os.listdir(null_models_dir_path)):
        if file.endswith(".txt"):
            null_models.append(np.loadtxt(os.path.join(null_models_dir_path, file)))

    null_models = np.array(null_models)

    return null_models

if __name__ == '__main__':
    NETWORK = 'CollegeMsg'

    results_original_network = f"results/original_networks/{NETWORK}/results_{NETWORK}.txt"
    null_models_dir = f"results/null_models/{NETWORK}"

    patterns_original_network = np.loadtxt(results_original_network)
    patterns_null_models = combine_null_models(null_models_dir)

    z_scores = compute_z_scores(patterns_original_network, patterns_null_models)

    plot_z_scores(z_scores, network=NETWORK)
