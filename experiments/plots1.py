import matplotlib
import matplotlib.pyplot as plt


def jains_fairness_index(d):
    if len(d) > 1:
        return sum(d) ** 2 / (len(d) * sum([i ** 2 for i in d]))
    return 1

def plot_fairness_over_time(simulation):
    future_arrival_times = [int(float(vehicle['arrival_sec'])) for vehicle in simulation]
    vehicles = [vehicle for vehicle in simulation]
    past_vehicles = []
    past_arrival_times = []
    max_time = max(future_arrival_times)
    cumulative_arrivals = []
    fairness_over_time = []
    total_arrivals = 0

    for t in range(max_time + 1):
        arrivals_at_t = 0

        while future_arrival_times[0] == t:
            past_arrival_times.append(future_arrival_times.pop(0))
            past_vehicles.append(vehicles.pop(0))
            arrivals_at_t += 1
            if not future_arrival_times:
                break

        total_arrivals += arrivals_at_t
        cumulative_arrivals.append(total_arrivals)
        past_time_losses = [int(float(vehicle['timeLoss_sec'])) for vehicle in past_vehicles]
        fairness_over_time.append(jains_fairness_index(past_time_losses))

    assert len(fairness_over_time) == len(cumulative_arrivals)

    fig, ax1 = plt.subplots()
    ax1.set_xlabel(f'time (in simulation steps)')
    ax1.set_ylabel('cumulative number of arrvials', color='tab:blue')
    ax1.plot(cumulative_arrivals, color='tab:blue', alpha=0.75)
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('jains fairness index', color='tab:red')
    ax2.plot(fairness_over_time, color='tab:red', alpha=0.75)
    ax2.tick_params(axis='y', labelcolor='tab:red')

    fig.suptitle('Static agent: cumulative arrivals / fairness comparison')
    fig.tight_layout()
    plt.show()



