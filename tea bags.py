import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np
from datetime import datetime
from pyscript import display

DEBUG: bool = False

# def time_to_int(t: datetime.time):
#     return t.hour * 3600 + t.minute * 60 + t.second

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

if DEBUG:
    print(f'\n{len(data)=}\n{sorted(data, key=lambda x: x[0])[:5]=}\n')

# Separate dates from clock times.
date_times = [(t[0].date(), t[1]) for t in data]
clock_times = [(t[0].time(), t[1]) for t in data]

# # Calculate average time of day tea was had.
# avg_time = np.mean([time_to_int(t[0]) for t in clock_times])
# print(f'{avg_time=} {datetime.time(avg_time // 3600, (avg_time % 3600) // 60, avg_time % 60)=}')


if DEBUG:
    print(f'{date_times[:5]=}\n{clock_times[:5]=}')

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

if DEBUG:
    print(f'{r[:5]=}\n{theta[:5]=}')
    print(f'\n{min(r)=} {np.mean(r)=} {max(r)=} {np.std(r)=}')
    print(f'\n{min(theta)=} {np.mean(theta)=} {max(theta)=} {np.std(theta)=}')

# Plot the data.
fig = plt.figure(dpi=90)
ax = fig.add_subplot(projection='polar')
ax.scatter(label='Entry', x=theta[1:-1], y=r[1:-1], c=r[1:-1], cmap='gist_rainbow')
ax.scatter(label='Terminal Entry', x=[theta[0], theta[-1]], y=[r[0], r[-1]], facecolor='white', edgecolors='black')

# Scale the radial axis based on the range of dates.
r_axis_space = 0.3
ax.set_rmin(min(r) - r_axis_space)
ax.set_rmax(max(r) + r_axis_space)

# Set the labels for the radial axis
ax.set_rlabel_position(210)
ax.set_rgrids([min(r), np.mean(r), max(r)], labels=[str(min(r)), f'{np.mean(r):.01}', str(max(r))])

# Get the labels for the angular axis
deg_per_clock_num = 360 / 12
clock_angles = [i * deg_per_clock_num for i in range(12)]
# Construct labels so they emulate a 12-hour clock
clock_labels = [str(i) for i in range(1, 12+1)]
clock_labels = [clock_labels[-1]] + clock_labels[:-1]

# Pair the fractions of pi with clock times, for reference.
if DEBUG:
    pi_slice = 2 * np.pi / 12
    clock_labels = [f'{t}, {pi_slice * i:.02}π' for i, t in enumerate(clock_labels)]

# Set the location of 0 for theta.
ax.set_theta_zero_location('N')

# Set theta to increcrease clockwise.
ax.set_theta_direction('clockwise')

# Set the labels for the angular axis
ax.set_thetagrids(angles=clock_angles, 
                  labels=clock_labels)

# Customize plot appearance.
ax.set_title('Time of Day I Drank Tea')
fig.set_facecolor('None') # Global background
ax.set_facecolor('None') # Polar plot background

# Add plot legend.
plt.legend(loc='lower right', bbox_to_anchor=(1.3, 1)) 
# plt.legend(loc='lower right') 

# Send the plot to the DOM (the div with id `tbplot`)
display(fig, target="tbplot")