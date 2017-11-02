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

# do stuff
with open(trafficfile, 'r') as tf:
  tf.readline()

  for line in tf:
    packet = line.split()
    time = int(packet[4])
    packet.append("")

    #print finished packets
    while(packet_queu):
      if packet_queu[0][5] == ": collision":
        finish = "finish sending: failed"
      else:
        finish = "finish sending: successfully transmitted"
      if int(packet_queu[0][4]) + int(packet_queu[0][3]) < time:
        print "Time: {} Packet: {}: {} {} {} {} {}".format(int(packet_queu[0][4]) + int(packet_queu[0][3]), packet_queu[0][0], packet_queu[0][1], packet_queu[0][2], packet_queu[0][3], packet_queu[0][4], finish)
        packet_queu.pop(0)
      else:
        break

    #check for collisions
    if packet_queu:
      packet[5] = ": collision"
      if len(packet_queu) == 1:
        packet_queu[0][5] = ": collision"

    #print packet sending message
    print "Time: {} Packet: {}: {} {} {} {} start sending{}".format(packet[4], packet[0], packet[1], packet[2], packet[3], packet[4], packet[5])

    packet_queu.append(packet)


  #make sure you check for failed
  #while packet_queu:
    #print packet_queu