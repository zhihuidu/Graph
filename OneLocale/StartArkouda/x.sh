#!/bin/bash

PortNum=$2
d=`date +%F-%H-%M-%S`
hostname=`hostname`
output="$d-$hostname-Server-$1-Locales-$PortNum$3"
# Only argument is number of locales/nodes
if [ "$#" -le 1 ];
then
    echo "usage: ./StartServer   <#locales> <PortNum> "
    exit
fi
numNodes=$1

echo "./arkouda_server -nl $1 --ServerConfig.ServerPort=$PortNum &> $output"

mkdir -p AKOutPut
#echo "./arkouda_server -nl $1 2>&1 |tee -a $output"
./arkouda_server -nl $1 --ServerConfig.ServerPort=$PortNum 2>&1|tee -a AKOutPut/$output
