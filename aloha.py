#!/usr/bin/python
'''
Grady Denton & Shane Bennet for proj2 in cnt5505 data comm
'''
from __future__ import division
import argparse
import os

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
packet_queu = []
howManySending = 0

# do stuff
with open(trafficfile, 'r') as tf:
  for line in tf:
    packet = line.split()
    if len(packet) > 1:
      packet.append("")
      if packet_queu:
        time = int(packet[4])
        for p in packet_queu:
          if int(p[4]) + int(p[3]) < time:
            if p[5] == ": collision":
              finish = "finish sending: failed"
            else:
              finish = "finish sending: successfully transmitted"
            print "Time: {} Packet: {}: {} {} {} {} {}".format(int(p[4]) + int(p[3]), p[0], p[1], p[2], p[3], p[4], finish)
            packet_queu.remove(p)
          else:
            p[5] = ": collision"
            packet[5] = ": collision"
      print "Time: {} Packet: {}: {} {} {} {} start sending{}".format(packet[4], packet[0], packet[1], packet[2], packet[3], packet[4], packet[5])
      packet_queu.append(packet)
  if packet_queu:
    print "STUFF LEFT IN QUE"
    print packet_queu