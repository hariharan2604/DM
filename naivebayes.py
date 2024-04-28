import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load the data from the CSV file
data = pd.read_csv("weather.csv")

# Split the data into features (X) and target variable (y)
X = data.drop(columns=["Rain"])
y = data["Rain"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Train the classifier on the training data
gnb.fit(X_train, y_train)
# Sample new data
new_data = pd.DataFrame({
    "Temperature": [23],
    "Humidity": [75],
    "WindSpeed": [10]
})

# Make prediction on the new data
prediction = gnb.predict(new_data)

print("Predicted Rain:", prediction)

# Make predictions on the testing data

