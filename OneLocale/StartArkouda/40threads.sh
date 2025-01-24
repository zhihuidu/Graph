#!/bin/bash


if [ "$#" -le 1 ];
then
    echo "usage: ./StartServer   <#locales> <PortNum> "
    exit
fi

#we first use MAX_LOGICAL threads to run it
numNodes=$1
PortNum=$2
d=`date +%F-%H-%M-%S`
hostname=`hostname`
export CHPL_RT_NUM_THREADS_PER_LOCALE=40
output="$d-$hostname-Server-$1-Locales-$PortNum$3-Threads$CHPL_RT_NUM_THREADS_PER_LOCALE"


mkdir -p AKOutPut
echo "./arkouda_server -nl $1 --ServerConfig.ServerPort=$PortNum 2>&1|tee -a AKOutPut/$output"
echo "./arkouda_server -nl $1 --ServerConfig.ServerPort=$PortNum "|tee -a AKOutPut/$output
echo "CHPL_RT_NUM_THREADS_PER_LOCALE=40 " |tee -a AKOutPut/$output
./arkouda_server -nl $1 --ServerConfig.ServerPort=$PortNum 2>&1|tee -a AKOutPut/$output

