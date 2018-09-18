#helper function to check if a number is even or not
def is_even(number):
    return number % 2 == 0

def even_number_of_evens(numbers):
    #list comprehension to clean up code
    evens = sum([1 for n in numbers if is_even(n)]) #add +1 to evens for each number if number is even
    return False if evens == 0 else is_even(evens) #return false unless evens is even

#Tests
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")