# Calculating student grades and sum ,avg, max , mini 

def calulate_grades(score):

    if score >=90:
        return 'A'
    elif score >=80:
        return 'B'
    elif score >=70:
        return 'C'
    elif score >=60:
        return 'D'
    else:
        return 'F'

def calulate_scroes(scores):
    """Process a list of scores and return statistics."""
    if not scores:
        return None
    
    total =sum(scores)
    average =total /len(scores)
    maximum = max(scores)
    minimum = min(scores)

    grades=[calulate_grades(score) for score in scores]
    
    return  {
        "total":total,
        "average":average,
        "maximum":maximum,
        "minimum":minimum,
        "grades":grades

    }

# Usage
scores = [85, 92, 78, 96, 88]
stats = calulate_scroes(scores)

print(f"Average: {stats['average']:.2f}")
print(f"Grades: {stats['grades']}")

    