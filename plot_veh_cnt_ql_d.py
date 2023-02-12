import json
import matplotlib.pyplot as plt

# To read data from file:
veh_cnt_list_ql = json.load(open("data/json/veh_cnt_list_ql.json"))
veh_cnt_list_d = json.load(open("data/json/veh_cnt_list_d.json"))

x_axis = list(range(720))


fig, ax = plt.subplots()
ax.plot(x_axis, veh_cnt_list_ql, '-b', linewidth=0.5)
ax.plot(x_axis, veh_cnt_list_d, '-r', linewidth=0.5)
ax.legend(['vehicle count ql','vehicle count d'], loc='lower right')
ax.set(xlabel='t(5s)', ylabel='number of vehicles')

plt.suptitle('Vehicle counts for queue-length and delay agent with\n'
             'dynamic arrivals with ns-peak=0.4 and we-peak=0.2.')

fig.tight_layout()
plt.show()