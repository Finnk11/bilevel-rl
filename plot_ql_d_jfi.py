import json
import matplotlib.pyplot as plt

# read data from file:
#reward_list_ql = json.load(open("data/json/reward_list_ql.json"))

#trip_info_list_ql = json.load(open("data/json/trip_info_list_ql.json"))

# create plot for delay agent
reward_list_d = json.load(open("data/json/reward_list_d.json"))

trip_info_list_d = json.load(open("data/json/trip_info_list_d.json"))


print('length reward_list_d:', len(reward_list_d))
print(reward_list_d[:10])


print('length trip_info_list:', len(trip_info_list_d))

time_windows = list(range(0, 3600, 5))
print('time_windows:', time_windows[:10])


# d = {el:0 for el in a}
def jains_fairness_index(d):
    if len(d) > 1:
        return sum(d) ** 2 / (len(d) * sum([i ** 2 for i in d]))
    return 1


time_window_delays_dict = {i: [] for i in range(720)}

# collect vehicles per time window
for veh in trip_info_list_d:
    j = int(float(veh['arrival_sec'])//5)
    # append to all subsequent time steps
    for k in range(j, 720, 1):
        time_window_delays_dict[k].append(float(veh['timeLoss_sec']))

time_window_fairness_dict = {i: jains_fairness_index(time_window_delays_dict[i]) for i in range(720)}


print('time_window_fairness_dict:', len(time_window_fairness_dict.keys()))





# raise Exception('exit')





x_axis = list(range(720))

fig, ax = plt.subplots()
ax.plot(x_axis, reward_list_d, '-b', linewidth=1.0)
ax.plot(x_axis, time_window_fairness_dict.values(), '-r', linewidth=1.0)
ax.legend(['delay (/340000)', 'fairness index'], loc='lower left')
ax.set(xlabel='t(5s)', ylabel='normalized delay (/340000) and JFI')

plt.suptitle('Cumulative delay reward and fairness index with\n'
             'dynamic arrival with ns-peak=0.4 and we-peak=0.2.')


fig.tight_layout()
plt.show()