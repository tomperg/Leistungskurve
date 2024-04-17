from load_data import load_data
from sort import bubble_sort
import matplotlib.pyplot as plt
import numpy as np
import os

data = load_data('activity.csv')

power_power = data['PowerOriginal']
#Sort
sorted_power_W = bubble_sort(power_power)


print(data)
print(sorted_power_W)
