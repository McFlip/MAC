#!/usr/bin/python
'''
Grady Denton & Shane Bennet for proj2 in cnt5505 data comm
'''
from __future__ import division
import argparse
import os
from random import *

# Function definitions



# set up arguments
parser = argparse.ArgumentParser(prog='aloha', description='Simulates the aloha protocol for a given traffic file.')
parser.add_argument("-t","--trafficfile", help="traffic file", default=os.path.join(os.getcwd(), "traffic"))
parser.add_argument("-o","--outfile", help="output file", default=os.path.join(os.getcwd(), "aloha.out"))
args = parser.parse_args()

# check arguments
trafficfile = os.path.expanduser(args.trafficfile)
if not os.path.exists(trafficfile):
  parser.error('The trafficfile file does not exist!')
if not os.path.isfile(trafficfile):
  parser.error('The trafficfile file is not a file!')
if not os.access(trafficfile, os.R_OK):
  parser.error('The trafficfile file is not readable!')

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

global packet_table
packet_table = []

# do stuff
seed(mySeed)


# finish
packet_table.sort(key=lambda x: int(x[4]))
with open(outfile, 'w') as of:
  of.write("{}\n".format(tot_packets))
  for row in packet_table:
    of.write("{} {} {} {} {}\n".format(row[0], row[1], row[2], row[3], row[4]))
