import json
import matplotlib.pyplot as plt

# To read data from file:
trip_info_list_ql = json.load(open("data/json/trip_info_list_ql.json"))
# trip_info_list_d = json.load(open("data/json/trip_info_list_d.json"))

time_window_arrivals_list = [0]*36
time_window_injections_list =[0]*36

for i in range(36):
    for veh in trip_info_list_ql:
        if (i + 1)*100 > float(veh['arrival_sec']) >= i*100:
            time_window_arrivals_list[i] += 1
        if (i + 1) * 100 > float(veh['depart_sec']) >= i * 100:
            time_window_injections_list[i] += 1


print('arrivals list:', time_window_arrivals_list)
print('departures list:', time_window_injections_list)


x_axis = list(range(36))

fig, ax = plt.subplots()
ax.plot(x_axis, time_window_arrivals_list, 'bo', linewidth=0.5)
ax.plot(x_axis, time_window_injections_list, 'ro', linewidth=0.5,alpha=0.5)
ax.legend(['arrivals ql','departures ql'], loc='upper left')
ax.set(xlabel='t(100s)', ylabel='number of vehicles per time windows')

plt.suptitle('Injections vs Arrivals for ql agent with\n'
             'dynamic arrivals with ns-peak=0.4 and we-peak=0.2.')

fig.tight_layout()
plt.show()
