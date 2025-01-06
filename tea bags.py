import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np
from pyscript import display


# # Load the .csv data.
# data = np.genfromtxt('./tea bag transcription.csv', 
#                     dtype=str, 
#                     delimiter=',')

# # Convert the data to a list.
# data = [list(i) for i in data]

# # Remove enclosing quotes from data.
# i = 0
# while i < len(data):
#     data[i] = [entry.replace('"', '') for entry in data[i]]
#     i += 1

# # Fixing random state for reproducibility
# np.random.seed(0)

# Compute areas and colors
N = 150 # data points
r = 2 * np.random.rand(N) # radius 
theta = 2 * np.pi * np.random.rand(N)
marker_size = 100 * r**2 # size of each point
colors = theta

fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=marker_size, cmap='hsv', alpha=0.75)

# Restrict the range of theta to [0deg,180deg].
ax.set_thetamin(0)
ax.set_thetamax(360)

# Get the labels for the angular axis
deg_per_clock_num = 360 / 12
clock_angles = [i * deg_per_clock_num for i in range(12)]
# Construct labels so they emulate a 12-hour clock
clock_labels = [f'{i}:00' for i in range(1, 12+1)]
clock_labels = clock_labels[2::-1] + clock_labels[:2:-1]

# Set the labels for the angular axis
ax.set_thetagrids(angles=clock_angles, 
                  labels=clock_labels)

# Set the labels for the radial axis
ax.set_rgrids([1], labels=['1'])

# Send the plot to the DOM (the div with id `tbplot`)
display(fig, target="tbplot")