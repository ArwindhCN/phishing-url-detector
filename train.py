import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1. Load the dataset
try:
    data = pd.read_csv('phishing.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'phishing.csv' not found. Please download it and put it in this folder.")
    exit()

# 2. Separate Features (X) and Labels (y)
# The column 'class' is the answer. 'Index' is just ID numbers, so we drop both.
X = data.drop(['class', 'Index'], axis=1)
y = data['class']

# 3. Split into Training (80%) and Testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and Train the Model
print("Training the Decision Tree model...")
model = DecisionTreeClassifier(max_depth=12, random_state=42)
model.fit(X_train, y_train)

# 5. Test the Model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"--------------------------------")
print(f"Model Training Complete!")
print(f"Accuracy Score: {accuracy * 100:.2f}%")
print(f"--------------------------------")

# 6. Save the Model
joblib.dump(model, 'phishing_model.pkl')
print("Model saved to 'phishing_model.pkl'")