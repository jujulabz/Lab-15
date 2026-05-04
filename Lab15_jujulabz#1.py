""""" 
Plot a math formula

Melissa Palmer

This program plots a sine wave using matplotlib.

5/1/2026

"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import math

x_values = []
y_values = []

for degree in range(0, 361):
    radians = math.radians(degree)
    x_values.append(degree)
    y_values.append(math.sin(radians))


