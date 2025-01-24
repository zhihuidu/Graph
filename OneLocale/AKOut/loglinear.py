import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Create some example data
x_small = np.linspace(1, 10, 100)  # small x range for linear scale
x_large = np.logspace(1, 3, 100)   # larger x range for log scale
y_small = np.sqrt(x_small)          # some function for small x
y_large = np.log(x_large)           # some function for large x

fig, ax = plt.subplots()

# Plot the small x range in linear scale
ax.plot(x_small, y_small, label='Linear part')

# Create a twin x-axis for log scale plot
ax2 = ax.twiny()

# Plot the large x range in log scale
ax2.plot(x_large, y_large, color='orange', label='Log part')
ax2.set_xscale('log')

# Formatting and labels
ax.set_xlabel('X (linear)')
ax2.set_xlabel('X (log)')
ax.set_ylabel('Y')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))  # Ensures integer ticks on linear x-axis

# Combine legends from both axes
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines + lines2, labels + labels2)

plt.title('Hybrid Plot with Linear and Log Scales on X-axis')
plt.show()

