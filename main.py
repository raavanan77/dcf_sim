#############################################
#                                           #
#   Random BackOff Simulation by Raavanan   #
#   Well that's it for now.                 #
#                                           #
#############################################

from random import randint
import matplotlib.pyplot as plt
import numpy as np

slot_time = 20
CW = 0
difs = 20

random = lambda x : randint(7,256) - randint(0,x)
csta = lambda quantity : [random(CW)*slot_time for _ in range(quantity)]

sta = np.array(csta(5))
stations = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E']

frame_data = [(1, 3), (5, 7), (2, 4), (4, 6), (6, 8)] 
defer_data = [(0, 1), (3, 5), (1, 2), (2, 4), (4, 6)] 

d_times = [1, 1.1, 3, 4]

fig, ax = plt.subplots(figsize=(10, 6))

# Plot FRAME rectangles
for i, (f_start, f_end) in enumerate(frame_data):
    ax.broken_barh([(f_start, f_end - f_start)], (i, 0.8), facecolor='green')

# Plot DEFER rectangles
for i, (d_start, d_end) in enumerate(defer_data):
    ax.broken_barh([(d_start, d_end - d_start)], (i, 0.8), facecolor='orange', alpha=0.5)

# Add DIFS markers
for d in d_times:
    ax.vlines(d, ymin=-0.5, ymax=len(stations) - 0.5, linestyles='dashed')

# Customize the plot
ax.set_yticks(range(len(stations)))
ax.set_yticklabels(stations)
ax.set_xlabel('Time')
ax.set_title('Channel Access')
ax.set_xticks([])

plt.show()


