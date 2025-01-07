def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = []
average = calculate_average(my_numbers) 
print(f"The average is: {average}") #This will print 0 as expected

my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers) 
print(f"The average is: {average}") #This will print 3.0 as expected

my_numbers = [1, 2, 'a', 4, 5] #This will throw TypeError
average = calculate_average(my_numbers)
print(f"The average is: {average}")