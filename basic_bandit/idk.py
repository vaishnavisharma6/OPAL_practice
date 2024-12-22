import numpy as np
import matplotlib.pyplot as plt

rewards = [0, 1, 2, 3]
x = np.arange(0, len(rewards))
plt.figure(figsize = (10, 6))
plt.plot(x, rewards)
plt.show()