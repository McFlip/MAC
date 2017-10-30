#!/usr/bin/python
'''
Grady Denton & Shane Bennet for proj2 in cnt5505 data comm
'''
import argparse
import os
from random import *

# Function definitions


# set up arguments
parser = argparse.ArgumentParser(prog='generator', description='Generate simulated traffic and outputs to file.')
parser.add_argument("-n","--num_node", help="number of nodes that Tx & Rx", default="1")
parser.add_argument("-P","--pkt_size", help="packet size", default="1")
parser.add_argument("-l","--offered_load", help="offered load 0.01&to&10", default="1")
parser.add_argument("-p","--num_pkts_per_node", help="number of packets per node", default="1")
parser.add_argument("-s","--seed", help="seed for random function", default="1")
parser.add_argument("-o","--outfile", help="traffic file", default=os.path.join(os.getcwd(), "traffic"))
args = parser.parse_args()

# check arguments

outfile = os.path.basename(os.path.expanduser(args.outfile))
outDir = os.path.dirname(os.path.expanduser(args.outfile))
if not outDir:
  outDir = os.getcwd()
if not os.path.exists(outDir):
    parser.error('The out dir does not exist!')
if not os.path.isdir(outDir):
    parser.error('The out dir is not a directory!')
if not os.access(outDir, os.W_OK):
    parser.error('The outDir dir is not writable!')

# MAIN FUNCTION

# Vars
num_node = int(args.num_node)
pkt_size = int(args.pkt_size)
offered_load = int(args.offered_load)
num_pkts_per_node = int(args.num_pkts_per_node)
seed = int(args.seed)
global tot_packets
tot_packets = 0
global gap
gap = (pkt_size * num_node / offered_load) - pkt_size

# do stuff


# finish
with open(outfile, 'w') as of:
  of.write("{}\n".format(tot_packets))
