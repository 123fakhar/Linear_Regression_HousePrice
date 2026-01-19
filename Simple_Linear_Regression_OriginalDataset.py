import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
data = pd.read_csv("Housing.csv")

x = data["area"].values
y = data["price"].values

n = len(x)
sum_x = 0
sum_y = 0
sum_xy = 0
sum_x2 = 0

for i in range(n):
    sum_x += x[i]
    sum_y += y[i]
    sum_xy += x[i] * y[i]
    sum_x2 += x[i] * x[i]

print("∑X: ", sum_x)
print("∑Y: ",sum_y)
print("∑XY: ", sum_xy)
print("∑X^2: ", sum_x2)

numerator = n*sum_xy - (sum_x * sum_y)
denominator = n*sum_x2 - (sum_x)**2
b = numerator / denominator
print("Slope b: ",b)

y_mean = sum_y / n
x_mean = sum_x / n
a = y_mean - b * x_mean
print("Intercept a: ", a)

y_predict = []
for i in range(n):
    y_hat = a + b * x[i]
    y_predict.append(y_hat)

print("Predictions: ", y_predict)

plt.scatter(x,y, label = "Actual Data")
plt.plot(x,y_predict, color = "red", label = "Regression Line")
plt.xlabel("Area Sqft")
plt.ylabel("Prices PKR")
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
plt.legend()
plt.show()