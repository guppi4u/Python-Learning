import re
from collections import defaultdict
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt


def load():
    """
    Load the dataset from a CSV file and parse it into a list of emails.
    Each email is represented as a dictionary with 'spam' and 'text' keys.
    """
    emails = []

    # Open the dataset file
    with open('Day15/spam_ham_dataset.csv', 'rt', encoding='utf-8') as file:
        for line in file:
            # Match lines with the format: id,spam/ham,text
            # Adjust regex for text with commas
            m = re.match(r'\d+,(spam|ham),(.+)', line.strip())

            if m:
                # Determine if the email is spam
                spam = m.group(1) == 'spam'
                # Get the email subject/text
                subject = m.group(2)
                # Append the email to the list
                emails.append({'spam': spam, 'text': subject})
            elif len(emails) > 0:
                # If the line doesn't match, append it to the last email's text
                emails[-1]['text'] += ' ' + line.strip()

    return emails


def get_common_words(emails):
    """
    Get the 1000 most common words from the list of emails.
    """
    frequencies = defaultdict(int)

    for email in emails:
        # Get word counts for the email text
        counts = get_counts(email['text'])

        for word, count in counts.items():
            # Update the frequency of each word
            frequencies[word] += count

    # Sort words by frequency in descending order and get the top 1000
    words = dict(sorted(frequencies.items(),
                 reverse=True, key=lambda item: item[1]))
    common_words = list(words.keys())[:1000]

    return common_words


def get_counts(text):
    """
    Count the frequency of each word in the given text.
    """
    frequencies = defaultdict(int)

    # Find all words in the text
    words = re.findall(r'\w+', text.lower())  # Use lowercase for consistency

    for word in words:
        # Increment the count for each word
        frequencies[word] += 1

    return frequencies


def get_frequencies(emails, words):
    """
    Get the frequency of the given words in each email.
    """
    frequencies = []

    for email in emails:
        # Get word counts for the email text
        counts = get_counts(email['text'])
        # Create a row of word frequencies for the email, adding 0 if the word isn't present
        row = [counts.get(word, 0) for word in words]
        frequencies.append(row)

    return frequencies


def main():
    """
    Main function to load data, train a Naive Bayes model, and evaluate its performance.
    """
    # Load the dataset
    emails = load()

    # Get the 1000 most common words
    words = get_common_words(emails)

    # Get the frequency of these words in each email
    X = get_frequencies(emails, words)
    # Get the labels (spam or not spam) for each email
    y = [email['spam'] for email in emails]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, shuffle=True, train_size=0.7)

    # Initialize the Bernoulli Naive Bayes model
    model = BernoulliNB()
    # Train the model
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


# Run the main function
if __name__ == '__main__':
    main()

# Output:
# Model: BernoulliNB()
# Accuracy: 0.8986
