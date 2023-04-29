from sklearn.linear_model import LinearRegression
import numpy as np

# input data
X = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500, 550])
y = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# create linear regression model
model = LinearRegression().fit(X.reshape(-1, 1), y)

# predict number of grocery trips for $350 spent
x_new = np.array([[350]])
y_new = model.predict(x_new)