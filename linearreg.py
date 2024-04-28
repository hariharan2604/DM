# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Provided data
X = np.array([60, 76, 80, 90, 53, 64, 85, 55]).reshape(-1, 1)  # Midterm Exam scores
y = np.array([53, 77, 78, 93, 64, 69, 89, 66])  # Final Exam scores

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions

# New Midterm Exam score for prediction
new_midterm_score = np.array([[70]])  # Example: predict for a Midterm score of 70

# Predict the Final Exam score
predicted_final_score = model.predict(new_midterm_score)

print("Predicted Final Exam Score for Midterm Exam Score 70:", predicted_final_score[0])



