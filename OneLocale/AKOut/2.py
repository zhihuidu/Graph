#import tkinter
#import matplotlib
#matplotlib.use('TkAgg')
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import copy
import numpy as np
import pandas as pd
import sys

FontSize=16

# Check if a filename argument is provided
if len(sys.argv) < 2:
    print("Please provide a filename as an argument.")
    sys.exit(1)

# Get the filename from the command-line argument
filename = sys.argv[1]

# Read the text file
data = pd.read_csv(filename, sep=' ', header=None)

# Extract the graph name
graph_name = data[0]

# Extract iteration numbers
iteration_numbers = data.iloc[:, 1:9]
print(iteration_numbers)
bakitera=copy.deepcopy(iteration_numbers)
# reorder the data
iteration_numbers[3]=bakitera[4]
iteration_numbers[4]=bakitera[5]
iteration_numbers[5]=bakitera[6]
iteration_numbers[6]=bakitera[7]
iteration_numbers[7]=bakitera[3]
print(iteration_numbers)
# remove data will not be shown in the paper
#iteration_numbers.drop(iteration_numbers.columns[[6,7]], axis=1, inplace=True )

#plt.figure()
#plt.tight_layout()
plt.rcParams.update({'font.size': FontSize})
ax=iteration_numbers.plot.bar(rot=0, figsize=(22, 10))

#ax.legend(["FastSV", "ConnectIt","C-1m1m","C-1","C-2","C-m", "C-11mm","C-Syn"])
ax.legend(["FastSV", "ConnectIt","C-1","C-2","C-m", "C-11mm","C-1m1m","C-Syn"])
plt.yscale('log',base=4) 
#ax.set_yscale('symlog', basey=2)

plt.subplots_adjust(bottom=0.19)
plt.ylabel("Number of Iterations")
plt.xlabel("Graph ID")
plt.title("Comparison of Iterations")
plt.savefig(filename+"-IterNum.png")
plt.show()
plt.close()

execution_values = data.iloc[:, 9:17]
print(execution_values)
exetime=execution_values.to_numpy()
pda=pd.DataFrame(exetime,columns = range(1,9))
print(pda)
bakexetime=copy.deepcopy(pda)
pda[3]=bakexetime[4]
pda[4]=bakexetime[5]
pda[5]=bakexetime[6]
pda[6]=bakexetime[7]
pda[7]=bakexetime[3]
#pda.drop(pda.columns[[6,7]], axis=1, inplace=True )
print(pda)
updatetime=copy.deepcopy(pda)
#plt.figure()
#plt.tight_layout()
plt.rcParams.update({'font.size': FontSize})
ax=pda.plot.bar(rot=0, figsize=(22, 10))
#ax.legend(["FastSV", "ConnectIt","C-1m1m","C-1","C-2","C-m", "C-11mm","C-Syn"])
ax.legend(["FastSV", "ConnectIt","C-1","C-2","C-m", "C-11mm","C-1m1m","C-Syn"])
#ax.set_yscale('symlog', basey=10)
plt.yscale('log',base=4) 
plt.ylabel("Execution Time(s)")
plt.xlabel("Graph ID")
#plt.legend(ncol=3)
plt.title("Comparison of Execution Time")
plt.subplots_adjust(bottom=0.19)
plt.savefig(filename+"-ExeTime.png")
plt.show()
plt.close()

inverse=1/pda
speedup=inverse.multiply(pda.iloc[:,0], axis=0)
print(speedup)
#plt.tight_layout()
plt.rcParams.update({'font.size': FontSize})
ax=speedup.plot.bar(rot=0, figsize=(22, 10))
#ax.legend(["FastSV", "ConnectIt","C-1m1m","C-1","C-2","C-m", "C-11mm","C-Syn"],ncol=4,loc="lower center")
#ax.legend(["FastSV", "ConnectIt","C-1","C-2","C-m", "C-11mm","C-1m1m","C-Syn"],ncol=4,loc="lower center")
ax.legend(["FastSV", "ConnectIt","C-1","C-2","C-m", "C-11mm","C-1m1m","C-Syn"],ncol=2)
#ax.set_yscale('symlog', basey=2)
#plt.yscale('log',base=4) 
plt.ylabel("Speedup")
plt.xlabel("Graph ID")
plt.title("Speedup Comparison (Baseline:FastSV)")
#plt.title("Comparison of Speedups")
#plt.legend(ncol=4)
plt.subplots_adjust(bottom=0.19)
plt.savefig(filename+"-Speedup.png")
plt.show()
plt.close()


all=pd.concat([data, speedup],axis=1)
all.to_csv(filename+"-all.csv")
#all=pd.concat([data, speedup],axis=1)
#all.to_excel(filename+"-all.xlsx")

inverse2=1/updatetime
speedup2=inverse2.multiply(updatetime.iloc[:,1], axis=0)
speedup2.drop(speedup2.columns[[0,7]], axis=1, inplace=True )
print(speedup2)
#plt.tight_layout()
plt.rcParams.update({'font.size': FontSize})
ax=speedup2.plot.bar(rot=0, figsize=(22, 10))
#ax.legend(["FastSV", "ConnectIt","C-1m1m","C-1","C-2","C-m", "C-11mm","C-Syn"],ncol=4,loc="lower center")
#ax.legend(["FastSV", "ConnectIt","C-1","C-2","C-m", "C-11mm","C-1m1m","C-Syn"],ncol=4,loc="lower center")
ax.legend(["ConnectIt","C-1","C-2","C-m", "C-11mm","C-1m1m"],ncol=2)
#ax.set_yscale('symlog', basey=2)
#plt.yscale('log',base=4) 
plt.ylabel("Speedup")
plt.xlabel("Graph ID")
plt.title("Speedup Comparison (Baseline:ConnectIt)")
#plt.legend(ncol=4)
plt.subplots_adjust(bottom=0.19)
plt.savefig(filename+"-Speedup2.png")
plt.show()
plt.close()





