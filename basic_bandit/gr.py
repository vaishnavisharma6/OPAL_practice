import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import random
import time
from IPython.display import clear_output


class greedy():

    def initial_estimate(self, k, para):
        rewards = []
        plays = []
        for i in range(k):
            arm = para[i+1]
            reward = np.random.normal(arm[0], arm[1], 1)    #sampling from normal distribution of reward of ith arm
            rewards.append(reward)
            plays.append(1)
        return(rewards, plays)

    def greedy_plot(self, r1,r2,r3,r4,r5):
        plt.figure(figsize = (10, 6))
        N = np.arange(0, len(r1))
      
        plt.plot(N,r1, label = 'arm 1')
        plt.plot(N,r2, label = 'arm 2')
        plt.plot(N,r3, label = 'arm 3')
        plt.plot(N,r4, label = 'arm 4')
        plt.plot(N,r5, label = 'arm 5')
        plt.xlabel('#trial')
        plt.ylabel('mean reward')
        plt.title('reward estimates at each trial')
        plt.legend()
        plt.savefig('greedy.png')
        plt.close()


    def play(self, rewards, plays, para, T):
        r1 = []
        r2 = []
        r3 = []
        r4 = []
        r5 = []
        r1.append(rewards[0])
        r2.append(rewards[1])
        r3.append(rewards[2])
        r4.append(rewards[3])
        r5.append(rewards[4])
        for i in range(T):
            chosen_arm = np.argmax(rewards)
            arm = para[chosen_arm+1]
            new_reward = np.random.normal(arm[0], arm[1], 1)
            plays[chosen_arm] += 1
            rewards[chosen_arm] = (rewards[chosen_arm] + new_reward)//plays[chosen_arm]
            if T%5 == 0:
                r1.append(rewards[0])
                r2.append(rewards[1])
                r3.append(rewards[2])
                r4.append(rewards[3])
                r5.append(rewards[4])                

        self.greedy_plot(r1,r2,r3,r4,r5)
    
    


    

k = 5
para = {1:[80, 10], 2:[100, 10], 3:[10, 5], 4:[40, 20], 5:[30, 20]}
gr = greedy()
rewards, plays = gr.initial_estimate(k, para)

gr.play(rewards, plays, para, 95)



