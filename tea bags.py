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
data: list[tuple[datetime, bool]] = [(ts[0], False) if len(ts)==1 else (ts[1], True) for ts in data]
data.sort()

print(f'{len(data)=} {data[:5]=}')

# Separate dates from clock times.
date_times = [(t[0].date(), t[1]) for t in data]
clock_times = [(t[0].time(), t[1]) for t in data]

# print(f'{date_times[:5]} {clock_times[:5]}')

# Convert dates into r points.
# Use the oordinal time.
r = [d[0].toordinal() for d in date_times]
# Scale r into [0,1]
r_min = np.min(r)
r_max = np.max(r)
r = [(i - np.min(r)) / (np.max(r) - np.min(r)) for i in r]

# Convert times into theta points.
# Represent time as a fraction of the day and scale to 2pi radians.
theta = [(c[0].hour + c[0].minute / 60 + c[0].second / 60) / 12 * 2 * np.pi for c in clock_times]

print(f'{r[:5]=}\n{theta[:5]=}')

# Fixing random state for reproducibility
np.random.seed(0)

# Compute areas and colors
# N = 159 # data points
# r = 2 * np.random.rand(N) # radius 
# theta = 2 * np.pi * np.random.rand(N)
# marker_size = [.5 * p for p in r] # size of each point
# colors = theta

# Plot the data.
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
# c = ax.scatter(theta, r, c=colors, s=marker_size, cmap='hsv', alpha=0.75)
c = ax.scatter(theta, r, c=r, cmap='gist_rainbow')
ax.scatter([theta[0], theta[-1]], [r[0], r[-1]], facecolor='none', edgecolors='black')

# Scale the radial axis based on the range of dates.
ax.set_rmin(min(r) - 0.1)
ax.set_rmax(max(r) + 0.1)

# Set the labels for the radial axis
ax.set_rgrids([min(r), np.mean(r), max(r)], labels=[str(min(r)), f'{np.mean(r):.01}', str(max(r))])

# Get the labels for the angular axis
deg_per_clock_num = 360 / 12
clock_angles = [i * deg_per_clock_num for i in range(12)]
# Construct labels so they emulate a 12-hour clock
clock_labels = [str(i) for i in range(1, 12+1)]
clock_labels = [clock_labels[-1]] + clock_labels[:-1]

# Pair the fractions of pi with clock times, for reference.
# pi_slice = 2 * np.pi / 12
# clock_labels = [f'{t}, {pi_slice * i:.02}π' for i, t in enumerate(clock_labels)]

# Set the location of 0 for theta.
ax.set_theta_zero_location('N')

# Set theta to increcrease clockwise.
ax.set_theta_direction('clockwise')

# Set the labels for the angular axis
ax.set_thetagrids(angles=clock_angles, 
                  labels=clock_labels)

# Set the labels for the radial axis
ax.set_rgrids([1], labels=['1'])

# TODO: Scale the radial axis dynamically based on the range of dates.
# Scale the radial axis based on the range of dates.
ax.set_rmin(min(r))
ax.set_rmax(max(r))

# Send the plot to the DOM (the div with id `tbplot`)
display(fig, target="tbplot")