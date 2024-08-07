#############################################
#                                           #
#   Random BackOff Simulation by Raavanan   #
#   Well that's it for now.                 #
#                                           #
#############################################

from random import randint
import matplotlib.pyplot as plt
import numpy as np

def begin(client):
    global next_frame,frame_len,frame_data,slot_time,end,cw_data,sta,difs,rcw_data
    nos = len(client)
    iter = 0
    while nos > 0:
        if 0 in client[0:]:
            start = np.where(client == 0)[0][0] #
            cw_data[start] = rcw_data[iter+start] 
            next_data_frame = int(cw_data[start][-1]) #setting time of next frame which is data
            end_data_frame = next_data_frame+frame_len #setting end of data frame
            end_difs = end_data_frame+difs #setting end of DIFS
            frame_data[start] = ((next_data_frame,end_data_frame))
            d_times.append(end_data_frame)
            d_times.append(end_difs)
            for _ in client:
                rcw_data.append((int(end_difs),int(end_difs)+_) if _ > 0 else (0,0)) #remain random backoff peroif of next slot
            if nos == 1:
                end = end_data_frame
            nos -=1
            iter += noc
            client[start] -= slot_time
        else:client[0:] -= slot_time


sta_name = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
slot_time = 20
CW = 0
difs = 400
frame_len=10000
next_frame = 0
end = 0
csta = lambda quantity : [(randint(7,256) - randint(0,CW))*slot_time for _ in range(quantity)] # creating and setting random backoff peroid for Stations
noc = randint(1,26) #no of clients


while True:
    sta_data = np.array(csta(noc))
    print(sta_data)
    stations = [f'Station {_}' for _ in sta_name[:noc]]
    frame_data = [(0,0) for _ in range(len(sta_data))]
    cw_data = [(0,0) for _ in range(len(sta_data))]
    d_times = []
    sta = list(sta_data)
    sta_duplicate = set(sta_data)
    rcw_data = [(0,_)  for _ in sta]
    if len(sta) == len(sta_duplicate):
        begin(sta_data)
        break
    else:
        sta_data = np.array(csta(noc))

fig, ax = plt.subplots(figsize=(10, 6))


# Plot RCW rectangles
for i, (r_start, r_end) in enumerate(rcw_data):
    ax.broken_barh([(r_start, r_end - r_start)], (i%noc, 0.2), facecolor='orange' ,alpha=0.4)

# Plot FRAME rectangles
for i, (f_start, f_end) in enumerate(frame_data):
    ax.broken_barh([(f_start, f_end - f_start)], (i, 0.35), facecolor='green')

# Plot DEFER rectangles
for i, (d_start, d_end) in enumerate(cw_data):
    ax.broken_barh([(d_start, d_end - d_start)], (i, 0.2), facecolor='orange')

# Add DIFS markers
for d in d_times:
    ax.vlines(d, ymin=-0.5, ymax=len(stations) - 0.5, linestyles='dashed')
    
for x in range(len(stations)):
    ax.arrow(0,x,end,0,width=0.02,color='black')

# Customize the plot
ax.set_yticks(range(len(stations)))
ax.set_yticklabels(stations)
ax.set_xlabel('Time')
ax.set_title('Channel Access')
#ax.set_xticks([])

plt.show()
#plt.savefig('Figure_1.png')


