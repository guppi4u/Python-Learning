
# -----Task 6: Combining Concepts


def process_scores():
    user_score_list=[] # creating an empty list to hold user values 

    while True:
        # 1 -User input
        user_input =input('Enter the value (comma seperated) or "break" to quit > ')

        # 2 -Quit condition
        if user_input.lower()=='break':
            print('Exist ....Thank you')
            break
        # 3 - input conversion from 'str' to 'int' with list comprehensions and error hadling 
        try:
            scores=[int(score.strip()) for score in user_input.split(',')] # list comprehensions
        except ValueError:
            print('Invalid input')
            continue

        # 4- Validating score between 0-100
        if any(s < 0 or s > 100 for s in scores):
            print('All scores must be between 0 and 100!!')
            continue

        # 5 Convert to grade using list comprehensions 
        def get_grade(score):
            return 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F'
        
        pairs=[(score,get_grade(score)) for score in scores]
        user_score_list.extend(pairs)
        
         # 6 Show immediate feedback
        for score, grade in pairs:
            print(f"  ✓ {score} → {grade}")
    
    return user_score_list
        

    # Test it
if __name__ == "__main__":
    all_results = process_scores()
    
    print("\n" + "="*45)
    print("FINAL RESULTS")
    print("="*45)
    for score, grade in all_results:
        print(f"Score: {score:3d} | Grade: {grade}")

process_scores()