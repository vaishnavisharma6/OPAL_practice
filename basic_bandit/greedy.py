import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import norm
from IPython.display import clear_output
import random
import time

#code for greedy and epsilon-greedy bandit algorithms

# 4 sections: define reward distributions for all arms.
# Play each arm once
# Get an estimate
# Play arm according to rule: Either greedy or epsilon-greedy
# Get reward, measure regret


N = 100 #time steps

class greedy():
    def initial_estimate(self, para):
        initial = []
        for i in range(5):
            arm = para[i+1]
            reward = np.random.normal(arm[0], arm[1], 1)
            initial.append(reward)
        return(initial)



    def play(self, para, i):
     # greedy way of playing
     plays = np.ones(10)
     if i == 6:
            rewards = self.initial_estimate(para)
            chosen_arm = np.argmax(rewards)
            dist = para[chosen_arm]
            new_reward = np.random.normal(dist[0], dist[1], 1)
            plays[chosen_arm] = plays[chosen_arm] + 1
            rewards[chosen_arm] = (rewards[chosen_arm] + new_reward)//plays[chosen_arm]
     else:
         chosen_arm = np.argmax(rewards)
         dist = para[chosen_arm]
         new_reward = np.random.normal(dist[0], dist[1], 1)
         plays[chosen_arm] = plays[chosen_arm] + 1
         old_reward = rewards[chosen_arm]
         rewards[chosen_arm] = (old_reward + new_reward)//plays[chosen_arm]       

     return (rewards)
      
    def plot(self, N, i):
        rewards = self.play(para, i)
        if i >= 6:
            clear_output(wait = True)
            plt.figure(figsize = (10, 6))
            x = np.arange(0, len(rewards))
            plt.plot(x, rewards[0], label = 'arm 1')
            plt.plot(x, rewards[1], label = 'arm 2')
            plt.plot(x, rewards[2], label = 'arm 3')
            plt.plot(x, rewards[3], label = 'arm 4')
            plt.plot(x, rewards[4], label = 'arm 5')

            plt.xlabel('#trial')
            plt.ylabel('rewards')
            plt.title('Mean Rewards at trial {}'.format(i))
            plt.legend()
            plt.savefig('greedy.png')
            time.sleep(0.3)
            plt.close()


class e_greedy():
    def initial_estimate(self, para):
        initial = []
        for i in range(5):
            arm = para[i+1]
            reward = np.random.normal(arm[0], arm[1], 1)
            initial.append(reward)
        return(initial)


    def play(self, para):
        if x > epsilon:
            #exploit
        else:
            # explore    

    def plot(self, N, i):
        rewards = self.play(para)
        if i >= 6:
            clear_output(wait = True)
            plt.figure(figsize = (10, 6))
            x = np.arange(0, len(rewards))
            plt.plot(x, rewards[0], label = 'arm 1')
            plt.plot(x, rewards[1], label = 'arm 2')
            plt.plot(x, rewards[2], label = 'arm 3')
            plt.plot(x, rewards[3], label = 'arm 4')
            plt.plot(x, rewards[4], label = 'arm 5')

            plt.xlabel('#trial')
            plt.ylabel('rewards')
            plt.title('Mean Rewards at trial {} for epsilon-greedy'.format(i))
            plt.legend()
            plt.savefig('epsilon_greedy.png')
            time.sleep(0.3)
            plt.close()



# environment definition
# stationary distribution for each arm

para = {1:[80, 100], 2:[100, 10], 3:[10, 5], 4:[40, 60], 5:[30, 20]}
