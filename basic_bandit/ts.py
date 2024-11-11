import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import beta
from IPython.display import clear_output
import random
import time
# Simulation of thompson sampling for a simple finite armed bandit problem.

# Reward function: Based on defined actual probabilities.

class Thompson_sampling():
  
    def sample(self, prior):
        success_prob = []
        distribution = prior
        x = np.linspace(0, 1, 100)
        for key, value in distribution.items():
            dist = beta(value[0], value[1])
            success_prob.append(dist.pdf(random.choice(x)))

        chosen_arm = success_prob.index(max(success_prob))+1

        return(chosen_arm)
    
    def reward(self, arm, actual_prob):
        re = np.random.binomial(1, actual_prob[arm])
        return re

    def update(self, distribution, chosen_arm, re):
        arm = chosen_arm
        re = re

        for key, value in distribution.items():
            if key == arm:
                value[0] = value[0] + re
                value[1] = value[1] + (1-re)
        return(distribution)        

    def dist_plot(self, distribution, trial):
        x = np.linspace(0, 1, 100)
        if trial>1:
            clear_output(wait=True)
            dist1 = beta(distribution[1][0], distribution[1][1])
            dist2 = beta(distribution[2][0], distribution[2][1])
            dist3 = beta(distribution[3][0], distribution[3][1])
            dist4 = beta(distribution[4][0], distribution[4][1])
            dist5 = beta(distribution[5][0], distribution[5][1])

            plt.figure(figsize=(8, 5))
            plt.plot(x, dist1.pdf(x), label=' arm1(α={}, β={})'.format(distribution[1][0], distribution[1][1]))
            plt.plot(x, dist2.pdf(x), label='arm2(α={}, β={})'.format(distribution[2][0], distribution[2][1]))
            plt.plot(x, dist3.pdf(x), label='arm3(α={}, β={})'.format(distribution[3][0], distribution[3][1]))
            plt.plot(x, dist4.pdf(x), label='arm4(α={}, β={})'.format(distribution[4][0], distribution[4][1]))
            plt.plot(x, dist5.pdf(x), label='arm5(α={}, β={})'.format(distribution[5][0], distribution[5][1]))
            plt.xlabel("x")
            plt.ylabel("Probability Density")
            plt.title("Beta Distribution PDF at trial{}:".format(trial))
            plt.legend()
            plt.savefig('plots.png')
            time.sleep(0.3)
            plt.close()

    def play(self, prior, actual_prob):
        trials = 100
        for i in range(trials):
            chosen_arm = self.sample(prior)
            re = self.reward(chosen_arm, actual_prob)
            distribution = self.update(prior, chosen_arm, re)
            prior = distribution
            self.dist_plot(prior, i)
        return(prior)


n_arms = 5
prior = {1: [0.1, 0.9], 2: [0.8, 0.1], 3: [0.2, 0.5], 4: [0.6, 0.7], 5: [1, 1]}
actual_prob = {1: 0.8, 2: 0.2, 3: 0.4, 4: 0.1, 5: 0.6}
TS = Thompson_sampling()

final_dist = TS.play(prior, actual_prob)

print(final_dist)









    




