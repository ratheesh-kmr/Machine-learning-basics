import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


df = pd.read_csv('d_data.csv')


X = df.drop('Will_go', axis=1)  # Features
y = df['Will_go']               # Target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


clf = DecisionTreeClassifier(max_depth=3, random_state=42)


clf.fit(X_train, y_train)

# Step 6: Operational Phase - Make predictions

y_pred = clf.predict(X_test)

# Step 7: Calculate the accuracy

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Step 8: Plot the decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=X.columns, class_names=['Not Go', 'Will Go'], filled=True)
plt.show()
