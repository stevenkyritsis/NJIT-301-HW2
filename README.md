# NJIT-301-HW2
<h3> By Steven Kyritsis </h3>

First I import numpy as np and pyplot as plt from matplot.


```python
import numpy as np
from matplotlib import pyplot as plt
```

For the first problem I made a variable "s" to hold the values of the poisson distribution using the following below:
```python
s = np.random.poisson(lam=10, size=100)
```

Next I created a histogram array thad stored the values in the variable "y"(we will need the values for the next problem)

```python
y = plt.hist(s)
```

To plot the graph I used the following:
```python
plt.show()
```

<p>This is the output of the graph:<br></p>

![Graph]
(/images/image1.png)

