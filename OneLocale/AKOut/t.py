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
execution_values = data.iloc[:, 9:17]
print(execution_values)
exetime=execution_values.to_numpy()
pda=pd.DataFrame(exetime,columns = range(1,9))
print(pda)
inverse=1/pda
speedup=inverse.multiply(pda.iloc[:,0], axis=0)
print(speedup)
#plt.tight_layout()
plt.rcParams.update({'font.size': FontSize})
ax=speedup.plot.bar(rot=0, figsize=(22, 10))
#ax.legend(["FastSV", "ConnectIt","C-1m1m","C-1","C-2","C-m", "C-11mm","C-Syn"],ncol=4,loc="lower center")
ax.legend(["FastSV", "ConnectIt","C-1m1m","C-1","C-2","C-m", "C-11mm","C-Syn"],ncol=2)
#ax.set_yscale('symlog', basey=2)
#plt.yscale('log',base=2) 
plt.ylabel("Speedup")
plt.xlabel("Graph ID")
plt.title("Speedup Comparison (Baseline:FastSV)")
#plt.legend(ncol=4)
plt.subplots_adjust(bottom=0.19)
plt.savefig(filename+"-Speedup.png")
plt.show()
plt.close()


inverse2=1/pda
speedup2=inverse.multiply(pda.iloc[:,1], axis=0)
print(speedup)
#plt.tight_layout()
plt.rcParams.update({'font.size': FontSize})
ax=speedup2.plot.bar(rot=0, figsize=(22, 10))
#ax.legend(["FastSV", "ConnectIt","C-1m1m","C-1","C-2","C-m", "C-11mm","C-Syn"],ncol=4,loc="lower center")
ax.legend(["ConnectIt","C-1m1m","C-1","C-2","C-m", "C-11mm"],ncol=2)
#ax.set_yscale('symlog', basey=2)
#plt.yscale('log',base=2) 
plt.ylabel("Speedup")
plt.xlabel("Graph ID")
plt.title("Speedup Comparison (Baseline:ConnectIt)")
#plt.legend(ncol=4)
plt.subplots_adjust(bottom=0.19)
plt.savefig(filename+"-Speedup2.png")
plt.show()
plt.close()
