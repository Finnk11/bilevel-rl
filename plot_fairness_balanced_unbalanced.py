import matplotlib.pyplot as plt

# JFI for static (balanced) and dyn. arrivals (imbalanced) with prob=0.2
fairness_index = [0.8835536834595746, 0.8650396597698936]

traffic_type = ['balanced', 'unbalanced']

fairness_index_delay = [0.7919695148282605, 0.7411733140126263]

fig, ax = plt.subplots(1, 1, figsize=(7, 7))
ax.plot(traffic_type, fairness_index, 'bo')
ax.plot(traffic_type, fairness_index_delay, 'ro')

ax.set(xlabel='traffic_type', ylabel='fairness')
ax.legend(['queue_length','delay'], loc='lower left')

# plt.arrow(0,fairness_index[0],1,fairness_index[1]-fairness_index[0], color='blue')
ax.annotate("", xy=(1, fairness_index[1]), xytext=(0, fairness_index[0]), arrowprops=dict(arrowstyle="->",color='b',linewidth=1.5))
ax.annotate("", xy=(1, fairness_index_delay[1]), xytext=(0, fairness_index_delay[0]), arrowprops=dict(arrowstyle="->",color='r',linewidth=1.5))


fig.suptitle('Performance comparison between queue-length-based,\n'
             'and delay-based agent with static arrivals with prob=0.2\n'
             '(balanced) and dynamic arrivals with ns-peak=0.4 and\n'
             'we-peak=0.2 (unbalanced).\n')

fig.tight_layout()
plt.show()

raise Exception('exit')



fig, axs = plt.subplots(2, 1, figsize=(7, 15))
axs[0].plot(peaks, avg_queue_length_lst_dyn, '--bo')
axs[0].set(xlabel='peak', ylabel='Average queue length per lane (vehicle)')
axs[0].legend(['Fixed', 'Second List'], loc='upper left')

axs[1].plot(peaks, fairness_index_lst_dyn, '--bo')
axs[1].set(xlabel='peak', ylabel='Jain fairness index')
axs[1].legend(['Fixed', 'Second List'], loc='upper left')

fig.suptitle('Performance comparison between queue-length-based,\n'
             'and delay-based agent with static arrivals with prob=0.2'
             '(balanced) and dynamic arrivals with ns-peak=0.4 and '
             'we-peak=0.2 (unbalanced).')


plt.show()

