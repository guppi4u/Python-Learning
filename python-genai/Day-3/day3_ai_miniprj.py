# ===================================
# QUIZ CREATOR PROGRAM
# ===================================
# Description: A program to create quizzes and take them
# Features: Create quizzes, take quizzes, calculate scores
# Author: Your Name
# Date: 2026
# ===================================

# ===================================
# DATA STRUCTURE
# ===================================
quizzes = []

# ===================================
# HELPER FUNCTIONS
# ===================================

def calculate_score(user_answers, correct_answers):
    """Calculate score based on user answers"""
    
    if len(user_answers) == 0:
        return {"total": 0, "correct": 0, "score_percentage": 0}
    
    correct_count = sum(1 for user, correct in zip(user_answers, correct_answers) 
                        if user == correct)
    
    total_questions = len(correct_answers)
    score_percentage = (correct_count / total_questions) * 100
    
    return {
        "total": total_questions,
        "correct": correct_count,
        "score_percentage": round(score_percentage, 2)
    }


def display_results(quiz_name, score_details, user_answers, correct_answers, questions):
    """Display the quiz results in a formatted way"""
    
    print("\n" + "="*60)
    print(f"RESULTS FOR: {quiz_name.upper()}")
    print("="*60)
    
    print(f"\nCorrect Answers: {score_details['correct']}/{score_details['total']}")
    print(f"Score: {score_details['score_percentage']}%")
    
    print("\n" + "-"*60)
    print("DETAILED RESULTS:")
    print("-"*60)
    
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}: {question['question']}")
        print(f"Your Answer: {user_answers[i].upper()}")
        print(f"Correct Answer: {correct_answers[i].upper()}")
        
        if user_answers[i] == correct_answers[i]:
            print("✓ CORRECT")
        else:
            print("✗ WRONG")
    
    print("\n" + "="*60 + "\n")


# ===================================
# MAIN FUNCTIONS
# ===================================

def create_quiz():
    """Allow user to create a new quiz"""
    
    quiz_name = input("Enter quiz name: ").strip()
    
    # Check if quiz already exists
    for quiz in quizzes:
        if quiz["name"].lower() == quiz_name.lower():
            print(f"Quiz '{quiz_name}' already exists!\n")
            return
    
    # Create new quiz
    new_quiz = {
        "name": quiz_name,
        "questions": []
    }
    
    print(f"✓ Quiz '{quiz_name}' created!\n")
    
    # Add questions
    while True:
        add_question = input("Add question? (yes/no): ").strip().lower()
        
        if add_question == "no":
            if len(new_quiz["questions"]) == 0:
                print("You must add at least one question!\n")
                continue
            print(f"✓ Quiz '{quiz_name}' saved with {len(new_quiz['questions'])} question(s)!\n")
            quizzes.append(new_quiz)
            break
        
        elif add_question == "yes":
            question_text = input("Enter question: ").strip()
            
            print("Enter 4 options:")
            option_a = input("  Option A: ").strip()
            option_b = input("  Option B: ").strip()
            option_c = input("  Option C: ").strip()
            option_d = input("  Option D: ").strip()
            
            correct_answer = input("Correct answer (a/b/c/d): ").strip().lower()
            
            if correct_answer not in ['a', 'b', 'c', 'd']:
                print("Invalid answer! Please enter a, b, c, or d\n")
                continue
            
            question_dict = {
                "question": question_text,
                "options": {
                    "a": option_a,
                    "b": option_b,
                    "c": option_c,
                    "d": option_d
                },
                "correct_answer": correct_answer
            }
            
            new_quiz["questions"].append(question_dict)
            print("✓ Question added successfully!\n")
        
        else:
            print("Invalid input! Please enter 'yes' or 'no'\n")


def take_quiz():
    """
    Display available quizzes and let user take one
    Collects answers and displays results
    """
    
    # Check if any quizzes exist
    if not quizzes:
        print("No quizzes available! Please create a quiz first.\n")
        return
    
    # Display available quizzes
    print("\n" + "="*60)
    print("AVAILABLE QUIZZES")
    print("="*60)
    
    for index, quiz in enumerate(quizzes, 1):
        question_count = len(quiz["questions"])
        print(f"{index}. {quiz['name']} ({question_count} questions)")
    
    # Get user's choice
    print()
    try:
        quiz_choice = int(input("Select a quiz number (or 0 to go back): "))
        
        # Handle "go back" option
        if quiz_choice == 0:
            print("✓ Returning to main menu...\n")
            return
        
        # Validate choice
        if quiz_choice < 1 or quiz_choice > len(quizzes):
            print("Invalid choice!\n")
            return
        
        # Get the selected quiz
        selected_quiz = quizzes[quiz_choice - 1]
        
        # Run the quiz
        run_quiz(selected_quiz)
        
    except ValueError:
        print("Please enter a valid number!\n")


def run_quiz(quiz):
    """
    Display quiz questions one by one and collect answers
    
    Parameters:
    - quiz: Dictionary containing quiz data
    """
    
    print("\n" + "="*60)
    print(f"QUIZ: {quiz['name'].upper()}")
    print("="*60)
    print(f"Total Questions: {len(quiz['questions'])}\n")
    
    input("Press Enter to start the quiz...")
    
    user_answers = []
    correct_answers = []
    
    # Display each question and collect answer
    for i, question in enumerate(quiz["questions"], 1):
        print("\n" + "-"*60)
        print(f"Question {i}/{len(quiz['questions'])}")
        print("-"*60)
        print(f"\n{question['question']}\n")
        
        # Display options
        print("Options:")
        for option_key, option_value in question["options"].items():
            print(f"  {option_key.upper()}) {option_value}")
        
        # Get user's answer
        while True:
            user_answer = input("\nYour answer (a/b/c/d): ").strip().lower()
            
            if user_answer in ['a', 'b', 'c', 'd']:
                user_answers.append(user_answer)
                correct_answers.append(question["correct_answer"])
                break
            else:
                print("Invalid input! Please enter a, b, c, or d")
    
    # Calculate score
    score_details = calculate_score(user_answers, correct_answers)
    
    # Display results
    display_results(quiz["name"], score_details, user_answers, 
                   correct_answers, quiz["questions"])

def main_menu():
    """
    Display main menu and handle user choices
    """
    
    while True:
        quiz_menu = '''
        
╔════════════════════════════════════════╗
║         QUIZ CREATOR PROGRAM           ║
╚════════════════════════════════════════╝

Menu:
1. Create a new quiz
2. Take a quiz
3. View all quizzes
4. Exit

        '''
        
        print(quiz_menu)
        
        try:
            user_choice = int(input("Enter your choice (1/2/3/4): "))
            
            if user_choice == 1:
                print()
                create_quiz()
            
            elif user_choice == 2:
                take_quiz()
            
            elif user_choice == 3:
                view_all_quizzes()
            
            elif user_choice == 4:
                print("Thank you for using Quiz Creator! Goodbye!\n")
                break
            
            else:
                print("Invalid choice! Please enter 1, 2, 3, or 4\n")
        
        except ValueError:
            print("Please enter a valid number!\n")


def view_all_quizzes():
    """
    Display all created quizzes with their details
    """
    
    if not quizzes:
        print("No quizzes created yet!\n")
        return
    
    print("\n" + "="*60)
    print("ALL QUIZZES")
    print("="*60)
    
    for i, quiz in enumerate(quizzes, 1):
        print(f"\n{i}. {quiz['name']}")
        print(f"   Questions: {len(quiz['questions'])}")
        
        # Show first 3 questions as preview
        for j, question in enumerate(quiz['questions'][:3], 1):
            print(f"   {j}. {question['question']}")
        
        if len(quiz['questions']) > 3:
            print(f"   ... and {len(quiz['questions']) - 3} more questions")
    
    print("\n" + "="*60 + "\n")


# ===================================
# PROGRAM ENTRY POINT
# ===================================

if __name__ == "__main__":
    main_menu()


