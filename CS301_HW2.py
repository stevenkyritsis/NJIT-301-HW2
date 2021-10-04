import numpy as np
from matplotlib import pyplot as plt

#1
# poisson distribution data for y-axis
s = np.random.poisson(lam=10, size=100)

plt.hist(s)

# showing the graph
plt.show()

#2
def gradient_descent(x, y, theta, alpha, m, numIterations):
    xTrans = x.transpose()
    for i in range(0, numIterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        # avg cost per example (the 2 in 2*m doesn't really matter here.
        # But to be consistent with the gradient, I include it)
        cost = np.sum(loss ** 2) / (2 * m)
        print("Iteration %d | Cost: %f" % (i, cost))
        # avg gradient per example
        gradient = np.dot(xTrans, loss) / m
        # update
        theta = theta - alpha * gradient
    return theta

mu = np.mean(s)
var = np.var(s, ddof=1)

gradient_descent(gradient=10.0, start=100.0, learn_rate=0.2, n_iter=1)