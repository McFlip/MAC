#!/usr/bin/python
'''
Grady Denton & Shane Bennett for proj2 in cnt5505 data comm
'''
from __future__ import division
import argparse
import os
from collections import deque
from copy import deepcopy

# Function definitions
def processQue(packet_queu, time, numSuccess):
  while(packet_queu and (int(packet_queu[0][4]) + int(packet_queu[0][3]) <= time or time == -1)):
    if packet_queu[0][5] == ": collision":
      finish = "finish sending: failed"
    else:
      finish = "finish sending: successfully transmitted"
      numSuccess = numSuccess + 1
    of.write("Time: {} Packet: {}: {} {} {} {} {}\n".format(int(packet_queu[0][4]) + int(packet_queu[0][3]), packet_queu[0][0], packet_queu[0][1], packet_queu[0][2], packet_queu[0][3], packet_queu[0][4], finish))
    packet_queu.popleft()
  return numSuccess


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
packet_queu = deque()
waiting_queu = deque()
numSuccess = 0
outPath = outDir + "/" + outfile

# do stuff
with open(outPath, 'w') as of:
  with open(trafficfile, 'r') as tf:
    stats = tf.readline()
    stats = stats.split()
    numPackets = int(stats[0])
    offerdLoad = float(stats[1])
    # get packet size
    pos = tf.tell()
    line = tf.readline()
    packet = line.split()
    packetSize = int(packet[3])
    tf.seek(pos)

    for line in tf:
      packet = line.split()
      time = int(packet[4])
      packet.append("")

      #print finished packets
      numSuccess = processQue(packet_queu, time, numSuccess)

      # ***** Changed for csma
      # copy waiting queu to sending queu
      if not packet_queu and waiting_queu:
        packet_queu = deepcopy(waiting_queu)
        waiting_queu.clear()
        if len(packet_queu) > 1:
          for p in packet_queu:
            #print packet sending message
            of.write("Time: {} Packet: {}: {} {} {} {} start sending{}\n".format(p[4], p[0], p[1], p[2], p[3], p[4], p[5]))
            p[5] = ": collision"
        elif len(packet_queu) == 1:
          for p in packet_queu:
            #print packet sending message
            of.write("Time: {} Packet: {}: {} {} {} {} start sending{}\n".format(p[4], p[0], p[1], p[2], p[3], p[4], p[5]))
        numSuccess = processQue(packet_queu, time, numSuccess)

      # processing current packet
      if packet_queu:
        packet[4] = int(packet_queu[0][4]) + packetSize
        waiting_queu.append(packet)
      else:
        packet_queu.append(packet)
      # ***** end changed for csma

    #finish off the queu
    if waiting_queu:
        timeLastPacketFinished = int(waiting_queu[-1][4]) + packetSize
    else:
        timeLastPacketFinished = int(packet_queu[-1][4]) + packetSize
    numSuccess = processQue(packet_queu, -1, numSuccess)
    if len(waiting_queu) > 1:
        for p in waiting_queu:
          #print packet sending message
          of.write("Time: {} Packet: {}: {} {} {} {} start sending{}\n".format(p[4], p[0], p[1], p[2], p[3], p[4], p[5]))
          p[5] = ": collision"
    numSuccess = processQue(waiting_queu, -1, numSuccess)

    of.write("Packet Size: {}  NumSuccess: {}  TimeLastPacketFinished: {} \n".format(packetSize, numSuccess, timeLastPacketFinished))

statfile = outDir + "/" + outfile + ".stats"
throughput = (numSuccess * packetSize) / timeLastPacketFinished
with open(statfile, 'w') as sf:
  sf.write("{},{}\n".format(offerdLoad,throughput))