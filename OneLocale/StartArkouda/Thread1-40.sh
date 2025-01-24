#!/bin/bash


if [ "$#" -le 1 ];
then
    echo "usage: ./StartServer   <#locales> <PortNum> "
    exit
fi

#we first use MAX_LOGICAL threads to run it
numNodes=$1
PortNum=$(($2 + 2))
d=`date +%F-%H-%M-%S`
hostname=`hostname`
export CHPL_RT_NUM_THREADS_PER_LOCALE=20
output="$d-$hostname-Server-$1-Locales-$PortNum$3-Threads$CHPL_RT_NUM_THREADS_PER_LOCALE"
mkdir -p AKOutPut
echo "./arkouda_server -nl $1 --ServerConfig.ServerPort=$PortNum 2>&1|tee -a AKOutPut/$output"
./arkouda_server -nl $1 --ServerConfig.ServerPort=$PortNum 2>&1|tee -a AKOutPut/$output


PortNum=$((2 + PortNum))
export CHPL_RT_NUM_THREADS_PER_LOCALE=40
output="$d-$hostname-Server-$1-Locales-$PortNum$3-Threads$CHPL_RT_NUM_THREADS_PER_LOCALE"
mkdir -p AKOutPut
echo "./arkouda_server -nl $1 --ServerConfig.ServerPort=$PortNum 2>&1|tee -a AKOutPut/$output"
./arkouda_server -nl $1 --ServerConfig.ServerPort=$PortNum 2>&1|tee -a AKOutPut/$output




#Following, we  use 2^i  threads to run it
# Set the value of N to the desired limit
N=40  # Change this to your desired value

adj=1
# Use a for loop to iterate through the sequence
for ((i = 1; i <= N; i *= 2)); do

export CHPL_RT_NUM_THREADS_PER_LOCALE=$i
echo $CHPL_RT_NUM_THREADS_PER_LOCALE
PortNum=$((2 + PortNum))

#adj=$adh*(-1)
d=`date +%F-%H-%M-%S`
hostname=`hostname`
output="$d-$hostname-Server-$1-Locales-$PortNum$3-Threads$CHPL_RT_NUM_THREADS_PER_LOCALE"
numNodes=$1

mkdir -p AKOutPut
echo "CHPL_RT_NUM_THREADS_PER_LOCALE=$i"  |tee -a AKOutPut/$output
echo "./arkouda_server -nl $1 --ServerConfig.ServerPort=$PortNum 2>&1|tee -a AKOutPut/$output"
./arkouda_server -nl $1 --ServerConfig.ServerPort=$PortNum 2>&1|tee -a AKOutPut/$output
done
