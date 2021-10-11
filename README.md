# NJIT-301-HW2
<h3> By Steven Kyritsis </h3>
<p>First I imported the libraries I will be using.<br></p>

```python
import random
import math
import statistics
import matplotlib.pyplot as plt
```
<p>Next I had two variables to hold the lambda and number of events values and use the values to simulate the probabilities.<br></p>

```python
#simulates 10 visits per minute
_lambda = 10
#simulates 100 views
_num_events = 100
_event_num = []
_inter_event_times = []
_event_times = []
_event_time = 0

for i in range(_num_events):
	_event_num.append(i)
	#Get a random probability value from the uniform distribution's PDF
	n = random.random()

	#Generate the inter-event time from the exponential distribution's CDF using the Inverse-CDF technique
	_inter_event_time = -math.log(1.0 - n) / _lambda
	_inter_event_times.append(_inter_event_time)

	#Add the inter-event time to the running sum to get the next absolute event time
	_event_time = _event_time + _inter_event_time
	_event_times.append(_event_time)

	#print it all out
	print(str(i) +',' + str(_inter_event_time) + ',' + str(_event_time))

#plot the inter-event times
fig = plt.figure()
fig.suptitle('Times between consecutive events in a simulated Poisson process')
plot, = plt.plot(_event_num, _inter_event_times, 'bo-', label='Inter-event time')
plt.legend(handles=[plot])
plt.xlabel('Index of event')
plt.ylabel('Time')
plt.show()


#plot the absolute event times
fig = plt.figure()
fig.suptitle('Absolute times of consecutive events in a simulated Poisson process')
plot, = plt.plot(_event_num, _event_times, 'bo-', label='Absolute time of event')
plt.legend(handles=[plot])
plt.xlabel('Index of event')
plt.ylabel('Time')
plt.show()

_interval_nums = []
_num_events_in_interval = []
_interval_num = 1
_num_events = 0

print('INTERVAL_NUM,NUM_EVENTS')

for i in range(len(_event_times)):
	_event_time = _event_times[i]
	if _event_time <= _interval_num:
		_num_events += 1
	else:
		_interval_nums.append(_interval_num)
		_num_events_in_interval.append(_num_events)

		print(str(_interval_num) +',' + str(_num_events))

		_interval_num += 1

		_num_events = 1

#print the mean number of events per unit time
print(statistics.mean(_num_events_in_interval))

#plot the number of events in consecutive intervals
fig = plt.figure()
fig.suptitle('Number of events occurring in consecutive intervals in a simulated Poisson process')
plt.bar(_interval_nums, _num_events_in_interval)
plt.xlabel('Index of interval')
plt.ylabel('Number of events')
plt.show()
```

<p>This is the output of the graphs:<br></p>

![Graph1](/images/image1.png)
![Graph2](/images/image2.png)
![Graph3](/images/image3.png)

<p>For problem 2 I had created a Gradient Descent Algorithm with the following: <br></p>

```python
def gradient_descent(f, start, lr, n_iter, tol):
    result = start
      
    for _ in range(n_iter): 
        new_val = -lr * np.gradient(f)
        if np.all(np.abs(new_val) <= tol):
            break
        result += new_val
    return result
```