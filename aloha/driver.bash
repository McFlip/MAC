#!/bin/bash
# Driver program that will run generator and simulator scripts
# stats files will concat to a csv file for import into spreadsheet
# graphs will be generated from spreadsheet

NUM_NODE="-n 10" #number of nodes that Tx & Rx
PKT_SIZE="-P 100" #packet size
# -l offered load 0.01 to 10
load_seq=$(< load_seq.txt)
NUM_PKTS_PER_NODE="-p 10" #number of packets per node
SEED="-s 1" #seed for random function
OUTFILE="-o traffic/traffic" #OUTFILE
Atraffic="-t ./traffic/traffic"
Aout="-o ./output/aloha.out"
catFile="catstat.csv" #compiled stats
i=0

for OFFERED_LOAD in $load_seq
do
  $( python generator.py $NUM_NODE $PKT_SIZE -l $OFFERED_LOAD $OUTFILE$i && python aloha.py $Atraffic$i $Aout$i ) &
  let "i++"
done

wait
echo "offered load,throughput" > $catFile
cat ./output/*.stats >> $catFile
