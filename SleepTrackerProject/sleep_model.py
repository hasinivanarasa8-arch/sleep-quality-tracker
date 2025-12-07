# ml_model.py
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

# -------------------------
# TRAINING DUMMY ML MODEL
# -------------------------
# Sample training data (you can replace this later)
# [sleep_hours, stress_level, screen_time, exercise_minutes]
X = np.array([
    [6, 7, 5, 20],
    [8, 3, 2, 40],
    [5, 8, 6, 10],
    [7, 4, 3, 30],
    [4, 9, 7, 0]
])

# Sleep quality score (0–100)
y = np.array([60, 85, 55, 75, 45])

# Train simple model
model = LinearRegression()
model.fit(X, y)

# Save model file
with open("sleep_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("ML model created successfully!")
