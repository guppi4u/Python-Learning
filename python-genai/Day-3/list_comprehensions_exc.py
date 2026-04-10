# creating list comprehensions exercise 

def list_compre_exercise():

    students = [
    {
        "student_id": "alice_001",
        "name": "Alice Johnson",
        "grade": 10,
        "scores": [85, 92, 78, 88, 95]
    },
    {
        "student_id": "bob_002",
        "name": "Bob Smith",
        "grade": 10,
        "scores": [78, 80, 82, 79, 81]
    },
    {
        "student_id": "charlie_003",
        "name": "Charlie Brown",
        "grade": 10,
        "scores": [92, 95, 89, 94, 97]
    },
    {
        "student_id": "diana_004",
        "name": "Diana Prince",
        "grade": 10,
        "scores": [88, 91, 87, 90, 89]
    },
    {
        "student_id": "evan_005",
        "name": "Evan Davis",
        "grade": 10,
        "scores": [76, 72, 75, 74, 77]
    },
    {
        "student_id": "fiona_006",
        "name": "Fiona Green",
        "grade": 10,
        "scores": [94, 93, 96, 92, 95]
    },
    {
        "student_id": "grace_007",
        "name": "Grace Lee",
        "grade": 10,
        "scores": [30, 20, 63, 88, 11]
    }
]

    # calcute average 

    average = [sum(s['scores']) / len(s['scores']) for s in students]

    print(f'Average student score : {average}')
    
    print('*' * 60)

    # Get names of students with average > 85
    top_students = [s["name"] for s in students if sum(s["scores"]) / len(s["scores"]) > 85]

    print(f'Top students  : {top_students}')
    print('*' * 60)


    # Create list of (name, average) tuples
    student_averages = [(s["name"], sum(s["scores"]) / len(s["scores"])) for s in students]

    print(f'Student average :{student_averages}')

    print('*' * 60)

list_compre_exercise()
