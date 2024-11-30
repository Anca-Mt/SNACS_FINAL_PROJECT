# Pattern Extraction in Temporal Networks

## Requirements
1. install networkx

## Supported Networks
dblp: https://www-kdd.isti.cnr.it/GERM/ (This is the original source I downloaded the file two months ago, but I think meanwhile the site has been deactivated)
CollegeMsg: https://snap.stanford.edu/data/CollegeMsg.html

## Directories explanations
1. networks_raw contains two folders: one for dblp original network and one for CollegeMsg network
2. networks_preprocess: contains the preprocessed original networks ready to be fed to the SNAP algorithm
3. null_models: for each original network 10 null models were created to be fed to the SNAP algorithm 

## Running 
In order to replicate the files in the directories you need to run: 
1. preprocessing_{network_name}_network.py 
2. null_model_creation.py -> in this one you will need to select for which network to create the null models (set variable ORIGINAL_NETWORK) and how many null models to create (set variable no_runs)

*auxiliary*
For each network there is an info_{network_name}_network.py file which shows you statistics related to the network: numer of nodes and number of edges

## Important things to know about the networks
- The dblp network is un undirected one.
- CollegeMsg network was originally a directed network, but in the processing step I transformed it into an undirected one (in order to facilitate the analysis and to align our study with the one in the paper).


