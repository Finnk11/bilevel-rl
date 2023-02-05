import argparse
import os
import sys

import mlflow
import tempfile
import xml.etree.cElementTree as elementTree

from stable_baselines3.common.logger import HumanOutputFormat, Logger
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.dqn import DQN

from utils.logger import MLflowOutputFormat, log_agent_params, log_env_params, log_meta_params, log_net_params, log_rew_params
from utils.callbacks import SUMOEvalCallback
from utils.configuration import generate_agent, generate_env_from_config, parse_config

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)

else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")


def main(args):
    print('CUR DIR:',os.getcwd())
    agent_config, env_config, reward_config, net_arch, train_config, meta_config = parse_config(args)
    env = generate_env_from_config(env_config, reward_config)
    eval_env = Monitor(env)
    model = DQN.load('./best_models/best_model_dynamic.zip')
    obs = env.reset()

    # file stored as /tmp/tmpxfdfe343id
    trip_file = env.trip_file

    i = 0
    queue_length_lst = []
    lane_index_lst = []
    vehs_on_lane_dict = {0: [], 1: [], 2: [], 3: []}
    while i < 720:
        for j, laneID in enumerate(env.sumo.trafficlight.getControlledLanes('nt1')):
            queue_length = env.sumo.lane.getLastStepHaltingNumber(laneID)
            vehs_on_lane = env.sumo.lane.getLastStepVehicleIDs(laneID)
            # vehs_on_lane_halting = []

            # select only halting vehicles
            for veh in vehs_on_lane:
                if env.sumo.vehicle.getSpeed(veh) < 0.1:
                    if veh not in vehs_on_lane_dict[j]:
                        vehs_on_lane_dict[j].append(veh)

            if queue_length > 0:
                queue_length_lst.append(queue_length)
                # record the lane
                lane_index_lst.append(j)
        # lane_ids = env.sumo.trafficlight.getControlledLanes('nt1')

        # for lane_id in lane_ids:
        #    queue_length = env.sumo.lane.getLastStepHaltingNumber(lane_id)
        #    if queue_length > 0:
        #        queue_length_lst.append(queue_length)

        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        env.render()
        i = i+1

    # average queue length of waiting vehicles
    # avg_queue_length = float(sum(queue_length_lst)) / len(queue_length_lst)
    # print('average queue length:', avg_queue_length)
    # collect average queue length for different arrival probs
    # avg_queue_length_lst.append(avg_queue_len)

    env.sumo.close()

    # read trip info file into list
    tree = elementTree.ElementTree(file=trip_file)
    trip_info_list = []

    for child in tree.getroot():
        trip = child.attrib
        trip_info = {'id': trip['id'],
                     'depart_sec': trip['depart'],
                     'arrival_sec': trip['arrival'],
                     'duration_sec': trip['duration'],
                     'timeLoss_sec': trip['timeLoss'],
                     'wait_step': trip['waitingCount'],
                     'wait_sec': trip['waitingTime'],
                     }
        trip_info_list.append(trip_info)

    delays = [float(a['timeLoss_sec']) for a in trip_info_list]
    print('#delays:', len(delays))

    id_delay_dict = {}
    for t in trip_info_list:
        id_delay_dict[t['id']] = t['timeLoss_sec']

    lane_delays_dict = {0: [], 1: [], 2: [], 3: []}

    for i in range(4):
        for k in vehs_on_lane_dict[i]:
            if k not in list(id_delay_dict.keys()):
                # vehicles on the way at simulation end not counted
                continue
            else:
                lane_delays_dict[i].append(id_delay_dict[k])

    print('lane_delays_dict[2]:',lane_delays_dict[2][:10])

    import json

    json.dump(delays, open("data/json/delays_ql.json", 'w'))

    json.dump(lane_delays_dict, open("data/json/lane_delays_dict_ql.json", 'w'))

    # Jain's fairness index
    # Equals 1 when all vehicles have the same delay
    def fairness_index(d):
        return sum(d) ** 2 / (len(d) * sum([i ** 2 for i in d]))

    fairness_index = fairness_index(delays)

    arrivals = [float(a['arrival_sec']) for a in trip_info_list]
    print('arrivals:', len(arrivals))
    arr = [x > 0 for x in arrivals]
    print('#ARRIVALS:',sum(arr))

    # collect fairness index for various arrival probs
    # fairness_index_lst.append(fairness_index)

    # print("AVG QUEUE LENGTH:", avg_queue_length)
    print("FAIRNESS INDEX:", fairness_index)

    import json
    lane_id_queue_length_dict = {0: [], 1: [], 2: [], 3: []}
    for laneID, queue_length in zip(lane_index_lst, queue_length_lst):
        lane_id_queue_length_dict[laneID].append(queue_length)

    print('delays length:', len(delays))
    print('lane_index_list length:',len(lane_index_lst))
    # To save the dictionary into a file:
    json.dump(lane_id_queue_length_dict, open("data/json/boxplot_ql.json", 'w'))
    print('Data stored to json file')


if __name__ == '__main__':
    print(os.path.join(os.getcwd(), 'configs/DQN.ini'))
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-path', type=str, default=os.path.join(os.getcwd(), 'nets/configs/DQN.ini'), help="experiment config path")
    parser.add_argument('--queue', type=str, required=False, help="initial weight for queue")
    parser.add_argument('--brake', type=str, required=False, help="initial weight for brake")
    arguments = parser.parse_args()

    main(arguments)
