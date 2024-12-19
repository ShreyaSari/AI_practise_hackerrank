# Data
physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

# Number of students
n = len(physics)

# Compute sums
sum_x = sum(physics)
sum_y = sum(history)
sum_xy = sum(x * y for x, y in zip(physics, history))
sum_x2 = sum(x ** 2 for x in physics)

# Calculate slope (m) and intercept (c)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
c = (sum_y - m * sum_x) / n

# Predict History score for Physics score of 10
x = 10
y = m * x + c

# Output
print(round(y, 1))
