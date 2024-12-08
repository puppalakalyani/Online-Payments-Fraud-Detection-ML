import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pickle

# Sample data (you'll need to replace this with your actual data)
# This is just example data based on your app.py features
np.random.seed(42)
n_samples = 1000

# Generate synthetic data
types = np.random.randint(1, 6, n_samples)  # 1: CASH_OUT, 2: PAYMENT, 3: CASH_IN, 4: TRANSFER, 5: DEBIT
amounts = np.random.uniform(10, 1000000, n_samples)
oldbalances = np.random.uniform(0, 1000000, n_samples)
newbalances = oldbalances - amounts
# Some fraudulent transactions might have inconsistent balances
fraud_idx = np.random.choice(n_samples, size=int(n_samples * 0.1), replace=False)
newbalances[fraud_idx] = np.random.uniform(0, 1000000, len(fraud_idx))

# Create labels (0: legitimate, 1: fraud)
labels = np.zeros(n_samples)
labels[fraud_idx] = 1

# Create the feature matrix
X = np.column_stack([types, amounts, oldbalances, newbalances])
y = labels

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the model
with open('static/model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Print model accuracy
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)
print(f"Training accuracy: {train_accuracy:.4f}")
print(f"Testing accuracy: {test_accuracy:.4f}")
