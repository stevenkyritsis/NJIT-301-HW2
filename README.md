# NJIT-301-HW2
<h3> By Steven Kyritsis </h3>
<p>First I import numpy as np and pyplot as plt from matplot.<br></p>

```python
import numpy as np
from matplotlib import pyplot as plt
```
<p>For the first problem I made a variable "s" to hold the values of the poisson distribution using the following below:<br></p>

```python
s = np.random.poisson(lam=10, size=100)
```

<p>Next I created a histogram array thad stored the values in the variable "y"(we will need the values for the next problem)<br></p>

```python
y = plt.hist(s)
```

<p>To plot the graph I used the following:<br></p>

```python
plt.show()
```

<p>This is the output of the graph:<br></p>

![Graph](/images/image1.png)

<p>For problem 2 I had created a Gradient Descent Algorithm with the following: <br></p>

```python
def GD(f, start, lr, n_iter, tol):
    result = start
      
    for _ in range(n_iter): 
        new_val = -lr * np.gradient(f)
        if np.all(np.abs(new_val) <= tol):
            break
        result += new_val
    return result
```

<p>After the gradient descent algorithm was created I stored the mean and variance of the poisson distribution in the following variables: <br></p>

```python
mu = np.mean(s)
var = np.var(s, ddof=1)
```

<p>Once the values were assigned to the variables I passed them into the gradiend descent function.</p>

```python

```