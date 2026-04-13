# Creating a function with multiple return 

def analyze_numbers():

    collected_numbers=[]

    # numbers=[12, 45, 8, 23, 56, 9, 34, 67, 3, 91]
    while True:
        try:
            user_input=int(input('Enter the numbers (or exit to quit) >  '))  
            collected_numbers.append(user_input)
        except ValueError:
            break
    if not collected_numbers:  # Handle empty list
        return {'error': 'No numbers entered'}
    total =sum(collected_numbers)
    average =total / len(collected_numbers)   
    maximum =max(collected_numbers)
    minimum =min(collected_numbers)
    count =len(collected_numbers)
    even_num=0
    odd_num=0
    for i in collected_numbers:
        if i % 2 ==0:
            even_num+=1
        elif i % 2 ==1:
            odd_num+=1

    return {
        'sum':total,
        'average': average,
        'maximum':maximum,
        'minimum':minimum,
        'count':count,
        'even':even_num,
        'odd':odd_num
    }

result=analyze_numbers()
print(result)