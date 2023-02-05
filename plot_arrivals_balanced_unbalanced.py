import matplotlib.pyplot as plt

# Arrivals for static (balanced) and dyn. arrivals (unbalanced) with prob=0.2
arrival_count = [2022, 1560]
traffic_type = ['balanced', 'unbalanced']

arrival_count_delay = [2573, 2555]

fig, ax = plt.subplots(1, 1, figsize=(7, 7))
ax.plot(traffic_type,arrival_count,'bo')
ax.plot(traffic_type,arrival_count_delay,'ro')

ax.set(xlabel='traffic_type', ylabel='arrivals')
ax.legend(['queue_length','delay'], loc='lower left')

# plt.arrow(0,fairness_index[0],1,fairness_index[1]-fairness_index[0], color='blue')
ax.annotate("", xy=(1, arrival_count[1]), xytext=(0, arrival_count[0]), arrowprops=dict(arrowstyle="->",color='b',linewidth=1.5))

ax.annotate("", xy=(1, arrival_count_delay[1]), xytext=(0, arrival_count_delay[0]), arrowprops=dict(arrowstyle="->",color='r',linewidth=1.5))

fig.suptitle('Performance comparison between queue_length-based,\n'
             'and delay-based agent with static arrivals with\n'
             ' prob=0.2 (balanced) and dynamic arrivals with\n'
             ' ns-peak=0.4 and we-peak=0.2 (unbalanced).')

fig.tight_layout()
plt.show()

