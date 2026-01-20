import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import StrMethodFormatter

data = pd.read_csv("Housing.csv")
y = data["price"].values
x1 = data["area"].values
x2 = data["bedrooms"].values

n = len(y)
sum_x1y = 0
sum_x2_2 = 0
sum_x2y = 0
sum_x1x2 = 0
sum_x1_2 = 0
sum_y = 0
sum_x1 = 0
sum_x2 = 0

for i in range(n):
    sum_x1y += x1[i] * y[i]
    sum_x2_2 += x2[i] * x2[i]
    sum_x2y += x2[i] * y[i]
    sum_x1x2 += x1[i] * x2[i]
    sum_x1_2 += x1[i] * x1[i]
    sum_y += y[i] 
    sum_x1 += x1[i]
    sum_x2 += x2[i]

print("∑X1Y: ", sum_x1y)
print("∑X2^2: ", sum_x2_2)
print("∑X2Y: ", sum_x2y)
print("∑X1X2: ", sum_x1x2)
print("∑X1^2: ", sum_x1_2)

denominator  = (sum_x1_2 * sum_x2_2) - (sum_x1x2)**2
b1 = ((sum_x1y * sum_x2_2) - (sum_x2y * sum_x1x2)) / denominator
b2 = ((sum_x2y * sum_x1_2) - (sum_x1y * sum_x1x2)) / denominator

y_mean = (sum_y / n)
x1_mean = (sum_x1 / n)
x2_mean = (sum_x2 / n)

a = y_mean - (b1* x1_mean) - (b2 * x2_mean)
y_predict = []

for i in range(n):
    y_hat = a + (b1 * x1[i]) + (b2 * x2[i])
    y_predict.append(y_hat)

x1_range = np.linspace(min(x1), max(x1), 20)
x2_range = np.linspace(min(x2), max(x2), 20)
X1, X2 = np.meshgrid(x1_range, x2_range)
Y_plane = a + b1 * X1 + b2 * X2
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1, x2, y)
ax.plot_surface(X1, X2, Y_plane, alpha=0.5)
ax.set_xlabel("Area")
ax.set_ylabel("Bedrooms")
ax.set_zlabel("Price")
ax.zaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
plt.show()