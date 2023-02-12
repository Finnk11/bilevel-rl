import json
import matplotlib.pyplot as plt

# To read data from file:
boxplot_data_d = json.load(open("data/json/boxplot_d.json"))
boxplot_data_ql = json.load(open("data/json/boxplot_ql.json"))

print(boxplot_data_d.keys())
print(len(boxplot_data_d['0']))
# print(boxplot_data['0'][:50])
print(len(boxplot_data_d['1']))
print(len(boxplot_data_d['2']))
print(len(boxplot_data_d['3']))

fig, (ax1,ax2) = plt.subplots(1,2,sharey=True)

# Creating plot
bp_ql = ax1.boxplot(boxplot_data_ql.values())
ax1.set_xticklabels(boxplot_data_ql.keys())
ax1.set_xlabel('Lane Index')
ax1.set_ylabel('Number of waiting vehicles')
ax1.set_title('queue_length')
# ax.set_suptitle('Title')

bp_d = ax2.boxplot(boxplot_data_d.values())
ax2.set_xticklabels(boxplot_data_d.keys())
ax2.set_xlabel('Lane Index')
ax2.set_title('delay')

plt.suptitle('Number of vehicles waiting at each lane with\n '
             'dynamic arrivals with ns-peak=0.4 and we-peak=0.2.')
# show plot)
fig.tight_layout()
plt.show()