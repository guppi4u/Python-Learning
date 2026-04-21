# ---QUIZ CREATOR---

def create_quiz():
    quiz_menu = '''

    ╔══════════════════════════════════════╗
    ║   Quiz Creator                       ║
    ╚══════════════════════════════════════╝

    Menu:
    1. Create a new quiz
    2. Take a quiz
    3. View quiz results
    4. Exit

    '''
    # Dictionary to hold all quizzes and their questions
    quiz_data = {} 
    while True:
        # prints the menu again after every action
        print(quiz_menu)
        # asking user for input after every action
        user_choice = int(input('Enter your choice: '))

        # Exiting the quiz creator if user selects option 4
        if user_choice == 4:
            print("Exiting the quiz creator. Goodbye!")
            break

        elif user_choice == 1:
            create_new_quiz(quiz_data)

        elif user_choice == 2:
            take_quiz(quiz_data)

        elif user_choice == 3:
            # Ask user to select a quiz to view
            if not quiz_data:
                print("No quizzes available.\n")
                continue

            print("\n" + "="*50)
            print("AVAILABLE QUIZZES")
            print("="*50)
            for idx, quiz_name in enumerate(quiz_data.keys(), start=1):
                print(f"{idx}. {quiz_name}")

            try:
                quiz_choice = int(input("\nEnter the number of the quiz you want to view: "))
                if 1 <= quiz_choice <= len(quiz_data):
                    selected_quiz = list(quiz_data.keys())[quiz_choice - 1]
                    display_quiz_content(quiz_data, selected_quiz)
                else:
                    print("Invalid choice. Please enter a valid quiz number.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")

        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")

             
def create_new_quiz(quiz_data):
    '''Function to create a new quiz and add questions to it'''
            
    option_1 = input('Enter quiz name : ').strip()

    # Store the quiz name in the quiz_data dictionary with an empty list to hold questions
    if option_1 not in quiz_data:
        quiz_data[option_1] = []
        print(f"Quiz '{option_1}' created successfully! You can now add questions to it.\n")
    else:
        print(f"Quiz '{option_1}' already exists. You can add questions to it.\n")

    while True:
            # asking user if they want to add a question to the quiz
            add_question = input('Do you want to add a question ? (yes/no)').strip().lower()

            if add_question == "no":
                print(f"Finished creating quiz '{option_1}'. Returning to main menu.\n")
                break # Exit question-adding loop, return to main menu

            if add_question == "yes":
                question = input("Question: ")
                option_a = input("Option A: ")
                option_b = input("Option B: ")
                option_c = input("Option C: ")
                option_d = input("Option D: ")
                correct_answer = input('Correct Answer (A/B/C/D):').strip().lower()

                # creating dictionary which holds questions and options
                quiz_question_data = {"question": question,
                    "options": {
                        "a": option_a,
                        "b": option_b,
                        "c": option_c,
                        "d": option_d
                    },
                        "correct_answer": correct_answer
                }

                 # Add the question to the category
                quiz_data[option_1].append(quiz_question_data)

            # asking user if they want to add another question to the quiz
            add_another_question = input('Add another question ? (yes/no)').strip().lower()
            
            if add_another_question == "no":
                print(f"Finished creating quiz '{option_1}'. Returning to main menu.\n")
                break # Exit question-adding loop, return to main menu
            elif add_another_question == "yes":
                continue # Continue to add another question

    print(f"Quiz '{option_1}' created successfully with {len(quiz_data[option_1])} questions!\n")
           
      
# Function to display available quizzes and let user take one
def take_quiz(quiz_data):
    """Function to display available quizzes and let user take one"""
    # checking if there are any quizzes available
    if not quiz_data:
        print("No quizzes available. Please create a quiz first.\n")
        return
    
      # Display available quizzes
    print("\n" + "="*50)
    print("AVAILABLE QUIZZES")
    print("="*50)
    
    # Create a list of quiz names to display with numbers
    quiz_list = list(quiz_data.keys())
    # Display quizzes with numbers and question counts
    for idx, quiz_name in enumerate(quiz_list, start=1):
        question_count = len(quiz_data[quiz_name])
        print(f"{idx}. {quiz_name} ({question_count} questions)")

    print()
    # Ask user to select a quiz by number
    try:
        quiz_choice = int(input("Enter the number of the quiz you want to take: "))

        if 1 <= quiz_choice <= len(quiz_list):
            selected_quiz = quiz_list[quiz_choice - 1]
            print(f"You have selected '{selected_quiz}' quiz. Let's start!\n")
            # Here you would call a function to actually administer the quiz
            # For example: administer_quiz(quiz_data[selected_quiz])
        else:
            print("Invalid choice. Please enter a valid quiz number.\n")
    except ValueError:
        print("Invalid input. Please enter a number corresponding to the quiz.\n")
    

 # NEW FUNCTION: Display quiz content
def display_quiz_content(quiz_data, quiz_name):
    """Display all questions and options for a selected quiz"""
    
    questions = quiz_data[quiz_name]
    
    print("\n" + "="*50)
    print(f"QUIZ: {quiz_name.upper()}")
    print("="*50)
    print(f"Total Questions: {len(questions)}\n")
    
    # Loop through each question
    for question_num, q in enumerate(questions, 1):
        print(f"Question {question_num}: {q['question']}")
        print(f"  a) {q['options']['a']}")
        print(f"  b) {q['options']['b']}")
        print(f"  c) {q['options']['c']}")
        print(f"  d) {q['options']['d']}")
        print(f"  ✓ Correct Answer: {q['correct_answer'].upper()}")
        print()
    
    print("✓ Returning to main menu...\n")




def claculate_score(quiz,anwser):
    pass


create_quiz()


