import numpy as np
from matplotlib import pyplot as plt

#1
# poisson distribution data for y-axis
s = np.random.poisson(lam=10, size=100)

y = plt.hist(s)

# showing the graph
plt.show()

#2
def GD(f, start, lr, n_iter=50, tol=1e-05):
    res = start
      
    for _ in range(n_iter): 
        # graident is calculated using the np.gradient 
        # function.
        new_val = -lr * np.gradient(f)
        if np.all(np.abs(new_val) <= tol):
            break
        res += new_val
          
    # we return a vector as the gradient can be
    # multivariable function. if the function has 1
    # dependent variable then it returns a scalar value.
    return res

mu = np.mean(s)
var = np.var(s, ddof=1)

GD(s, y, 10.0, 100.0, 0.2, 1)
