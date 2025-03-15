# Description: This file is used to calculate the accuracy score of the model
# The accuracy score is the proportion of correct predictions in the dataset

# The accuracy score is calculated using the accuracy_score function from the sklearn.metrics module


from sklearn.metrics import accuracy_score
# The accuracy score is calculated by comparing the true values with the predicted values

y_true = [0, 1, 1, 1, 0, 1, 0, 0, 1, 0]

y_pred = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
# The accuracy score is calculated by passing the true values and the predicted values to the accuracy_score function
accuracy = accuracy_score(y_true, y_pred)

print(f"Accuracy Score: {accuracy}")

# calculate the accuracy score of the model

print(accuracy_score([1, 2, 3, 4], [1, 2, 0, 4]))
# Output: 0.75
# The accuracy score is 0.75, which means 75% of the predictions are correct
# The accuracy score is calculated by comparing the true values with the predicted values
# The accuracy score is the proportion of correct predictions in the dataset
