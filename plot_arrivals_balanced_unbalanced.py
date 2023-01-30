import matplotlib.pyplot as plt

# Arrivals for static (balanced) and dyn. arrivals (unbalanced) with prob=0.2
arrival_count = [1980, 1488]
traffic_type = ['balanced', 'unbalanced']

fig, ax = plt.subplots(1, 1, figsize=(7, 7))
ax.plot(traffic_type,arrival_count,'bo')

ax.set(xlabel='traffic_type', ylabel='arrivals')
ax.legend(['queue_length'], loc='upper left')

# plt.arrow(0,fairness_index[0],1,fairness_index[1]-fairness_index[0], color='blue')
ax.annotate("", xy=(1, arrival_count[1]), xytext=(0, arrival_count[0]), arrowprops=dict(arrowstyle="->",color='b',linewidth=1.5))

fig.suptitle('Performance comparison between queue-length-based,\n'
             'and delay-based agent with static and dynamic\n'
             'arrivals of prob 0.2.')


plt.show()

