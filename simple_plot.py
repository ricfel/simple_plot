import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('inflammation.csv', delimiter=',')

fig = plt.figure(figsize=(10,3))

# arrange subplots inside of figure
axes1 = fig.add_subplot(1,3,1)
axes2 = fig.add_subplot(1,3,2)
axes3 = fig.add_subplot(1,3,3)

axes1.set_ylabel('average')
axes1.plot(data.mean(axis=0))

axes2.set_ylabel('max')
axes2.plot(data.max(axis=0))

axes3.set_ylabel('min')
axes3.plot(data.min(axis=0))

axes1.set_ylim(0, data.max()*1.33)

plt.show()