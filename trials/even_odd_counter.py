
'''
Even–Odd Counter

Input a list of numbers and count how many are even vs odd.

Bonus: Accept input as a single comma-separated string like "1,2,3,4,5".
'''
numbers = input(f"input a single comma-separated string of numbers:  ")
#print(numbers)

if (numbers):
      num_list=[int(num) for num in numbers.split(",")]
      for n in num_list:
            if n % 2 == 0: 
                print(f"{n} is even")
            else:
                print(f"{n} is odd")
else:
    print(f"no input provided") 
