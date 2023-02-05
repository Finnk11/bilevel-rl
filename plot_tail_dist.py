import json
import matplotlib.pyplot as plt
# To read data from file:
delays_ql = json.load(open("data/json/delays_queue_length.json"))

delays_d = json.load(open("data/json/delays_delay.json"))


boxplot_data_ql = json.load(open("data/json/lane_delays_dict_ql.json"))
boxplot_data_d = json.load(open("data/json/lane_delays_dict_d.json"))

delays_ql = [float(a) for a in boxplot_data_ql['2']]
delays_d = [float(a) for a in boxplot_data_d['2']]


print('length delays_ql:',len(delays_ql))
print(delays_ql[:10])

print('length delays_d:',len(delays_d))


print('max ql:', max(delays_ql))
print('min ql:', min(delays_ql))


print('max delay:', max(delays_d))
print('min delay:', min(delays_d))


def greater_cnt_ql(t):
    greater_cnt = 0
    for d in delays_ql:
        if d > t:
            greater_cnt = greater_cnt+1
    return greater_cnt


def greater_cnt_d(t):
    greater_cnt = 0
    for d in delays_d:
        if d > t:
            greater_cnt = greater_cnt+1
    return greater_cnt

import numpy as np

print(greater_cnt_ql(150))
max_ql = max(delays_ql)

#SIZE=20
SIZE=20

upper_ql = (np.ceil(max_ql)/SIZE + 1)*SIZE
upper_ql = int(upper_ql)
print('upper ql:', upper_ql)
xTimes_ql = list(range(0, upper_ql, SIZE))
print('xTimes ql:', xTimes_ql[:10])
##################################################################
print(greater_cnt_d(150))
max_d = max(delays_d)

upper_d = (np.ceil(max_d)/SIZE + 1)*SIZE
upper_d = int(upper_d)
print('upper d:', upper_d)
xTimes_d = list(range(0, upper_d, SIZE))

print('xTimes d:', xTimes_d[:10])


# xTimes = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180]

yProbs_ql = []
for t in xTimes_ql:
    gc = greater_cnt_ql(t)
    yProbs_ql.append(float(gc)/len(delays_ql))

print(yProbs_ql)

######################################################
yProbs_d = []
for t in xTimes_d:
    gc = greater_cnt_d(t)
    yProbs_d.append(float(gc)/len(delays_d))

print(yProbs_d)


fig, ax = plt.subplots()
ax.plot(xTimes_ql, yProbs_ql, '-bo', linewidth=3.0)
ax.plot(xTimes_d, yProbs_d, '-ro', linewidth=3.0)
ax.legend(['queue_length', 'delay'], loc='upper right')
ax.set(xlabel='t(s)', ylabel='P(Delay>t)')

plt.suptitle('Delay tail distribution with dynamic arrival \n'
             'with ns-peak=0.4 and we-peak=0.2 on lane 2.\n')

fig.tight_layout()

plt.show()