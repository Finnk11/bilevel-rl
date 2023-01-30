import matplotlib.pyplot as plt

# JFI for static (balanced) and dyn. arrivals (imbalanced) with prob=0.2
fairness_index = [0.9095971373792151, 0.8221136616917429]
traffic_type = ['balanced', 'unbalanced']

fig, ax = plt.subplots(1, 1, figsize=(7, 7))
ax.plot(traffic_type,fairness_index,'bo')

ax.set(xlabel='traffic_type', ylabel='fairness')
ax.legend(['queue_length'], loc='upper left')

# plt.arrow(0,fairness_index[0],1,fairness_index[1]-fairness_index[0], color='blue')
ax.annotate("", xy=(1, fairness_index[1]), xytext=(0, fairness_index[0]), arrowprops=dict(arrowstyle="->",color='b',linewidth=1.5))

fig.suptitle('Performance comparison between queue-length-based,\n'
             'and delay-based agent with static and dynamic\n'
             'arrivals of prob 0.2.')


plt.show()

raise Exception('exit')



fig, axs = plt.subplots(2, 1, figsize=(7, 15))
axs[0].plot(peaks, avg_queue_length_lst_dyn, '--bo')
axs[0].set(xlabel='peak', ylabel='Average queue length per lane (vehicle)')
axs[0].legend(['Fixed', 'Second List'], loc='upper left')

axs[1].plot(peaks, fairness_index_lst_dyn, '--bo')
axs[1].set(xlabel='peak', ylabel='Jain fairness index')
axs[1].legend(['Fixed', 'Second List'], loc='upper left')

fig.suptitle('Performance comparison between fixed, queue-length-based,\n'
             'and delay-based agent with dynamic uniform\n'
             'arrivals at all lanes wrt certain peaks.')


plt.show()

