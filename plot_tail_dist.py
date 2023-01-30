import json
import matplotlib.pyplot as plt
# To read data from file:
delays = json.load(open("data/json/delays_queue_length.json"))

print(len(delays))
print(type(delays[0]))


print('max:', max(delays))
print('min:', min(delays))


def greater_cnt(t):
    greater_cnt = 0
    for d in delays:
        if d > t:
            greater_cnt = greater_cnt+1
    return greater_cnt

import numpy as np
print(greater_cnt(150))
max=max(delays)

upper=(np.ceil(max)/20 + 1)*20
upper = int(upper)
print('upper:',upper)
xTimes = list(range(0,upper,20))
print('xTimes:',xTimes[:10])

#xTimes = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180]

yProbs = []
for t in xTimes:
    gc = greater_cnt(t)
    yProbs.append(float(gc)/len(delays))

print(yProbs)



fig, ax = plt.subplots()
ax.plot(xTimes, yProbs, '-bo', linewidth=3.0)
ax.legend(['queue_length'], loc='upper right')
ax.set(xlabel='t(s)', ylabel='P(Delay>t)')

plt.suptitle('Delay tail distribution with dynamic arrival \n'
             'with peak=0.2 (queue_length agent).')

plt.show()