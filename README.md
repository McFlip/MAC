# MAC
Simulation of various MAC protocols.
Authors: Shane Bennett and Grady Denton
For CNT5505 project 2.

Each folder has its own set of scripts. Run generator.py to create a traffic file.
Then pass that file into the aloha|slotted_aloha|csma.py
driver.bash is used for statistical analysis.  It iterates through a sequence of offered loads.
load_seq.py is used to generate load_seq.txt (The sequence of loads)
The bash script will save the generated traffic files in the traffic folder
and the Simulation output in the output folder.
It will also produce a file called catstat.csv, which is a comma seperated table of statistics.

This csv is then imported into a spreadsheet and used to compile graphs.

Prototypes of the scripts:

usage: generator [-h] [-n NUM_NODE] [-P PKT_SIZE] [-l OFFERED_LOAD]
[-p NUM_PKTS_PER_NODE] [-s SEED] [-o OUTFILE]

Generate simulated traffic and outputs to file.

optional arguments:
-h, --help            show this help message and exit
-n NUM_NODE, --num_node NUM_NODE
number of nodes that Tx & Rx
-P PKT_SIZE, --pkt_size PKT_SIZE
packet size
-l OFFERED_LOAD, --offered_load OFFERED_LOAD
offered load 0.01&to&10
-p NUM_PKTS_PER_NODE, --num_pkts_per_node NUM_PKTS_PER_NODE
number of packets per node
-s SEED, --seed SEED  seed for random function
-o OUTFILE, --outfile OUTFILE  traffic file

usage: aloha [-h] [-t TRAFFICFILE] [-o OUTFILE]

Simulates the aloha protocol for a given traffic file.

optional arguments:
-h, --help            show this help message and exit
-t TRAFFICFILE, --trafficfile TRAFFICFILE
traffic file
-o OUTFILE, --outfile OUTFILE  output file