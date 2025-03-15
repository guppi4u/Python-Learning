import re
from collections import defaultdict
from sklearn.naive_bayes import ComplementNB, GaussianNB, MultinomialNB, BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris(as_frame=True)

# Extract the features (data) and the target (labels)
df = iris['data']
target = iris['target']

# Split the data into training and testing sets
# 70% of the data will be used for training, and 30% for testing
X_train, X_test, y_train, y_test = train_test_split(
    df, target, shuffle=True, train_size=0.7)

# Initialize the Multinomial Naive Bayes model
model = MultinomialNB()

# Train the model using the training data
model.fit(X_train, y_train)

# Predict the labels for the test set
y_predicted = model.predict(X_test)

# Print the model class and accuracy score
print(f'Model: {model.__class__}')
print(f'Accuracy: {accuracy_score(y_test, y_predicted):.4f}')

# Generate and display the confusion matrix
cm = confusion_matrix(y_test, y_predicted)
ConfusionMatrixDisplay(cm).plot()

# Show the plot
plt.show()
