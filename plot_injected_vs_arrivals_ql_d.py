import json

import matplotlib.pyplot as plt
import numpy as np

# To read data from file:
trip_info_list_ql = json.load(open("data/json/trip_info_list_ql.json"))
trip_info_list_d = json.load(open("data/json/trip_info_list_d.json"))

time_window_arrivals_list_ql = [0] * 36
time_window_injections_list_ql = [0] * 36
time_window_arrivals_list_d = [0] * 36
time_window_injections_list_d = [0] * 36

for i in range(36):
    for veh in trip_info_list_ql:
        if (i + 1) * 100 > float(veh['arrival_sec']) >= i * 100:
            time_window_arrivals_list_ql[i] += 1
        if (i + 1) * 100 > float(veh['depart_sec']) >= i * 100:
            time_window_injections_list_ql[i] += 1

for i in range(36):
    for veh in trip_info_list_d:
        if (i + 1) * 100 > float(veh['arrival_sec']) >= i * 100:
            time_window_arrivals_list_d[i] += 1
        if (i + 1) * 100 > float(veh['depart_sec']) >= i * 100:
            time_window_injections_list_d[i] += 1

print('arrivals list:', time_window_arrivals_list_ql)
print('departures list:', time_window_injections_list_ql)

x_axis = list(range(36))

fig, ax = plt.subplots()
ax.plot(x_axis, time_window_arrivals_list_ql, 'bo', linewidth=0.5)
ax.plot(x_axis, time_window_injections_list_ql, 'ro', linewidth=0.5, alpha=0.5)
ax.legend(['arrivals ql', 'departures ql'], loc='upper left')
ax.set(xlabel='t(100s)', ylabel='number of vehicles per time windows')

plt.suptitle('Injections vs Arrivals for ql agent with\n'
             'dynamic arrivals with ns-peak=0.4 and we-peak=0.2.')

fig.tight_layout()
plt.show()

x = np.array(time_window_injections_list_ql)
y = np.array(time_window_arrivals_list_ql)

x2 = np.array(time_window_injections_list_d)
y2 = np.array(time_window_arrivals_list_d)

fig2, ax2 = plt.subplots()
m, b = np.polyfit(x, y, 1)
m2, b2 = np.polyfit(x2, y2, 1)
plt.scatter(x, y, c='b')
plt.scatter(x2, y2, c='r')
plt.plot(x, m * x + b, c='b')
plt.plot(x2, m2 * x2 + b2, c='r')
ax2.set(xlabel='departures per time window', ylabel='arrivals per time windows')
ax2.legend(['queue-length agent', 'delay agent'], loc='lower right')
plt.suptitle('both agents\ncorrelation (departures, arrivals) per time window t = 100s')
fig2.tight_layout()
plt.show()
