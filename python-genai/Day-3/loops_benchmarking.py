
import timeit

def learning_list_compre():
    
    traditional_code = '''
squares_traditional = []
for x in range(200):
    squares_traditional.append(x ** 2)
'''
    
    comprehension_code = '''
list_compre_squares = [x**2 for x in range(200)]
'''
    
    # Run tests for 100000
    trad_time = timeit.timeit(stmt=traditional_code, number=100000)
    comp_time = timeit.timeit(stmt=comprehension_code, number=100000)
    
    # Display results in table format
    print("=" * 70)
    print(f"{'Method':<30} {'Total Time':<20} {'Avg per Run':<20}")
    print("=" * 70)
    print(f"{'Traditional for loop':<30} {trad_time:<20.6f} {trad_time/100000:<20.9f}")
    print(f"{'List Comprehension':<30} {comp_time:<20.6f} {comp_time/100000:<20.9f}")
    print("=" * 70)
    
    # Verdict
    faster = "List Comprehension" if comp_time < trad_time else "Traditional Loop"
    ratio = max(trad_time, comp_time) / min(trad_time, comp_time)
    print(f"\n🏆 Winner: {faster} ({ratio:.2f}x faster)\n")

learning_list_compre()
