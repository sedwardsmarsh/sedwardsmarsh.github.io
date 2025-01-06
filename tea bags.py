import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np
from datetime import datetime
from pyscript import display

def parse_timestamp(timestamp: str) -> datetime:
    formats = [
        "%m/%d/%y %I:%M %p",  # 12-hour clock with AM/PM
        "%m/%d/%y %I:%M%p",   # 12-hour clock with AM/PM no spacing
        "%m/%d/%y %H:%M",     # 24-hour clock
        "%m/%d/%y %I:%M",     # 12-hour clock without AM/PM
    ]
    for fmt in formats:
        try:
            return datetime.strptime(timestamp, fmt)
        except ValueError:
            continue
    raise ValueError(f"Timestamp format not recognized: {timestamp}")

# Load the .csv data.
data = np.genfromtxt('./tea bag transcription.csv', 
                    dtype=str, 
                    delimiter=',',
                    skip_header=1)

# Remove double quotes in data.
data = [[timestamp.replace('"', '') for timestamp in pair] for pair in data]

# Convert timestamps to datetime objects.
data = [[parse_timestamp(ts) for ts in pair if len(ts) > 0] for pair in data]

# Replace timestamps which have corrections.
# The new format of data will be list[tuple[datetime, bool]] 
# The bool indicates whether the timestamp was corrected.
data = [(ts, False) if len(ts)==1 else (ts[1], True) for ts in data]

print(f'{len(data)=} {data[:5]=}')

# Separate dates from clock times.
# date_times = [[clock_time for ts in pair]]
# clock_times = [[]]

# print(f'{date_times[:5]} {clock_times[:5]}')


# Fixing random state for reproducibility
np.random.seed(0)

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
clock_labels = clock_labels[::-1]

# Set the location of 0 for theta.
ax.set_theta_zero_location('N')

# Set the labels for the angular axis
ax.set_thetagrids(angles=clock_angles, 
                  labels=clock_labels)

# TODO: Scale the radial axis dynamically based on the range of dates.
# Set the labels for the radial axis
ax.set_rgrids([1], labels=['1'])

# Send the plot to the DOM (the div with id `tbplot`)
display(fig, target="tbplot")