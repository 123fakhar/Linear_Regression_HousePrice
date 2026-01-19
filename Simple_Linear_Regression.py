import matplotlib.pyplot as plt
X = [30,22,16,7,14,23,26]
Y = [15,8,12,17,10,7,13]

n = len(X)
sum_x = 0
sum_y = 0
sum_xy = 0
sum_x2 = 0


for i in range(n):
    sum_x = sum_x + X[i]
    sum_y = sum_y + Y[i]
    sum_xy += X[i] * Y[i]
    sum_x2 += X[i] * X[i]


print("∑X: ", sum_x)
print("∑Y: ", sum_y)
print("∑XY: ", sum_xy)
print("∑x^2: ", sum_x2)

numerator = n*sum_xy - (sum_x * sum_y)
denominator = n * sum_x2 - (sum_x)**2

b = numerator / denominator 
print("Slope b: ", b)
y_mean = (sum_y / n)
x_mean = (sum_x / n)

a = y_mean - (b* x_mean)
print("Intercept a: ", a)

y_predict = []
for i in range(n):
    y_hat = a + b * X[i]
    y_predict.append(y_hat)

print("Predictions: ", y_predict)

plt.scatter(X,Y , label = "Actual Data")
plt.plot(X,y_predict , color = "red" , label = "Regression Line")
plt.xlabel("Hour Studied")
plt.ylabel("Scores")
plt.legend()
plt.show()