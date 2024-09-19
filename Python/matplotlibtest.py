# Add your code below:
import matplotlib
import random
numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
print(numbers_b)
matplotlib.pyplot.plot(numbers_a, numbers_b)
matplotlib.pyplot.show()