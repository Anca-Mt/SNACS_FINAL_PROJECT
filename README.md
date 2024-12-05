## Extracting Patterns in Temporal Networks

### Requirements
1. pip install -r requirements.txt

### Supported Networks
dblp: https://www-kdd.isti.cnr.it/GERM/ (This is the original source we downloaded the file two months ago, but we think that meanwhile the site has been deactivated)

CollegeMsg: https://snap.stanford.edu/data/CollegeMsg.html

*auxiliary:*

- The dblp network is an undirected one.
- CollegeMsg network was originally a directed network, but in the preprocessing step it was transformed into an undirected one (in order to facilitate the analysis and to align our study with the one in the paper).

### Directories explanations
1. networks_raw contains two folders: one for dblp original network and one for CollegeMsg network
2. networks_preprocess: contains the preprocessed original networks ready to be fed to the SNAP algorithm
3. null_models: for each original network 10 null models were created to be fed to the SNAP algorithm 
4. snap: contains the necessary files for creating an executable for running SNAP algorithm (temporal-motifs). The SNAP algorithm is an open source git repository. More information on how to use the algorithm can be found here: https://snap.stanford.edu/temporal-motifs/
5. results: contains the results obtained by running the SNAP algorithm for both networks (original and null models)
6. plot: contains the patterns heatmaps and z-scores bar plots

### Running 
In order to replicate the files in the directories you need to run: 
1. preprocessing_{network_name}_network.py 
2. null_model_creation.py -> select for which network to create the null models (set variable ORIGINAL_NETWORK) and how many null models to create (set variable no_runs)
3. the results were obtained by a running the SNAP algorithm on a separate machine with Linux support. For errorless execution, the networks_preprocessed and null_models directories have to be copied in snap/examples/temporalmotifs directory

**Example of command:** 

*./temporalmotifsmain -i:networks_preprocessed/dblp/dblp_network.txt -delta:1000 -o:results/original_networks/dblp/results_dblp.txt*

4. patterns_visualization.py -> select for which network to visualize the patterns heatmap (set variable NETWORK)
5. patterns_evaluation.py -> select for which network to compute and visualize the z-scores (set variable NETWORK)

*auxiliary:*

For each network there is an info_{network_name}_network.py file which computes some statistics related to the raw network: number of nodes and number of edges
