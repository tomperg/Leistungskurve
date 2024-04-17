from load_data import load_data
from sort import bubble_sort
import matplotlib.pyplot as plt
import numpy as np
import os

data = load_data('activity.csv')

power_power = data['PowerOriginal']
#Sort
sorted_power_W = bubble_sort(power_power)

print(sorted_power_W)

plt.plot(sorted_power_W)
plt.title('Leistungskurve')
plt.xlabel('Time (t)')
plt.ylabel('Power (W)')
plt.grid(True)

# Erstellen des figures-Ordners
if not os.path.exists('figures'):
    os.makedirs('figures')

# Speichern der Grafik im PNG-Format im figures-Ordner
plt.savefig('figures/power_curve.png')

# Anzeigen der Grafik
plt.show()