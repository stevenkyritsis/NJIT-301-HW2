import numpy as np
from matplotlib import pyplot as plt

#1
# poisson distribution data for y-axis
s = np.random.poisson(lam=10, size=100)

y = plt.hist(s, 10, density=True)

plt.xlabel('Time')
plt.ylabel('Visitors')

# showing the graph
plt.show()

#2
def GD(f, start, lr, n_iter=50, tol=1e-05):
    result = start
    for _ in range(n_iter): 
        new_val = -lr * np.gradient(f)
        if np.all(np.abs(new_val) <= tol):
            break
        result += new_val
    return result

mu = np.mean(s)
var = np.var(s, ddof=1)

GD(s, y, 0.2)