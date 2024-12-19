import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Input Reading
F, N = map(int, input().split())
data = [list(map(float, input().split())) for _ in range(N)]
T = int(input())
test_data = [list(map(float, input().split())) for _ in range(T)]

# Splitting Features and Target
data = np.array(data)
X_train = data[:, :-1]  # Features
y_train = data[:, -1]   # Target prices

# Polynomial Regression (degree < 4)
poly = PolynomialFeatures(degree=3, include_bias=False)
X_train_poly = poly.fit_transform(X_train)

model = LinearRegression()
model.fit(X_train_poly, y_train)

# Transform Test Data
X_test = np.array(test_data)
X_test_poly = poly.transform(X_test)

# Predict Prices
predictions = model.predict(X_test_poly)

# Output Predictions
for price in predictions:
    print(round(price, 2))
