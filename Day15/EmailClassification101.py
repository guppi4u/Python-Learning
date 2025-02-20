'''
The program reads a file (spam_ham_dataset.csv), uses a regular expression to detect and classify lines as either "spam" or "ham", and stores the subject/content of each email. It handles multi-line emails by appending the continuation of the subject if needed. Finally, it prints a list of dictionaries with each email's classification and text.
'''
import re


def spamEmailload():

    # creating empty email list

    emails = []

    # this opens csv file in read text mode
    with open('Day15/spam_ham_dataset.csv', 'rt') as file:

        # iterating through the line
        for line in file:

            # this will match digits , seperate it as spam or ham and rest of char in the line
            m = re.match(r'\d+,(spam|ham),(.*)', line)

            # grouping of email as spam or ham
            if (m):
                spam = m.group(1) == 'spam'

                subject = m.group(2)

                # append email in below dic pattern onto email list

                emails.append({'spam': spam, 'text': subject})

             # If a line doesn't match the pattern (e.g., a continuation of the subject), this block checks if there are any previously collected email entries in the emails list.

            elif len(emails) > 0:
               # If there are existing emails, this adds the current line to the subject of the last email entry (concatenating the lines).
                emails[-1]['text'] += line

    return emails


def main():
    emailList = spamEmailload()

    print(emailList)

    # Count spam emails using list comprehension
    spam_count = sum(1 for email in emailList if email['spam'])

    print(f"Number of spam emails: {spam_count}")
    # print(emails)


main()
