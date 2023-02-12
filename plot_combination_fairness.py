import json
import matplotlib.pyplot as plt

# convex combination r*queue_length + (1-r)*delay
r = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

fairness_list = [0.7511349438974342
, 0.6692027539560388
, 0.848436164239729, 0.8597337735463367, 0.8636020584245274, 0.8748982475840527,  0.8844770386838862
, 0.7631453506931073, 0.8724700458479122, 0.861191140085667
,0.8588870571072106
]



fig, ax = plt.subplots()
ax.plot(r, fairness_list, '-ro', linewidth=1.0)
ax.legend(['combined reward fairness'], loc='lower right')
ax.set(xlabel='r', ylabel='fairness')

plt.suptitle('Combined reward r*queue_length+(1-r)*delay with\n'
             'dynamic arrival with ns-peak=0.4 and we-peak=0.2.')


fig.tight_layout()
plt.show()