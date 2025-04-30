###########################
# 1. Basic lambda to add 10
###########################
add_10 = lambda x: x + 10
print(add_10(5))  # 15


###########################
# 2. Multiply two numbers
###########################
multiply = lambda a, b: a * b
print(multiply(3, 4))  # 12

###########################
# 3. Find maximum of two numbers
###########################
maximum = lambda x, y: x if x > y else y
print(maximum(10, 20))  # 20

###########################
# Categorize into minor or adult
###########################
age_category = lambda age: "Minor" if age < 18 else "Adult"
print(age_category(16))  # Minor

###########################
# Speed limit violation
###########################
speed_check = lambda speed: "Overspeed" if speed > 80 else "Normal"
print(speed_check(90))  # Overspeed

###########################
# 4. Check if a number is even
###########################
is_even = lambda x: x % 2 == 0
print(is_even(8))  # True

###########################
# 5. Find length of a string
###########################
length = lambda s: len(s)
print(length("hello"))  # 5

###########################
# 6. Return "Positive" or "Negative"
###########################
pos_neg = lambda x: "Positive" if x >= 0 else "Negative"
print(pos_neg(-5))  # Negative

###########################
# 7. Square a number
###########################
square = lambda x: x ** 2
print(square(6))  # 36

###########################
# 8. Cube a number
###########################
cube = lambda x: x ** 3
print(cube(3))  # 27

###########################
# 9. Get first character of a string
###########################
first_char = lambda s: s[0]
print(first_char("Python"))  # P

###########################
# 10. Combine two strings
###########################
combine = lambda s1, s2: s1 + " " + s2
print(combine("Good", "Morning"))  # Good Morning


##################################
######## using map(function,iterable)
##################################
# 11. Square all numbers in a list
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16, 25]

##################################
# 12. Convert all strings to uppercase
##################################
words = ['apple', 'banana', 'cherry']
uppercased = list(map(lambda x: x.upper(), words))
print(uppercased)  # ['APPLE', 'BANANA', 'CHERRY']

##################################
# 13. Add 5 to each number
##################################
plus_five = list(map(lambda x: x + 5, nums))
print(plus_five)  # [6, 7, 8, 9, 10]

##################################
# 14. Multiply corresponding elements from two lists
##################################
a = [2, 3, 4]
b = [5, 6, 7]
products = list(map(lambda x, y: x * y, a, b))
print(products)  # [10, 18, 28]

##################################
# 15. Convert list of numbers to their string form
##################################
numbers = [10, 20, 30]
as_strings = list(map(lambda x: str(x), numbers))
print(as_strings)  # ['10', '20', '30']

##################################
# 16. Add 2 if number is even, else add 3
##################################
adjusted = list(map(lambda x: x+2 if x%2==0 else x+3, nums))
print(adjusted)  # [4, 5, 6, 7, 8]

##################################
# 17. Replace odd numbers with 0
##################################
replace_odds = list(map(lambda x: 0 if x%2!=0 else x, nums))
print(replace_odds)  # [0, 2, 0, 4, 0]

##################################
# 18. Get first letter of each word
##################################
words = ["hello", "world", "python"]
first_letters = list(map(lambda x: x[0], words))
print(first_letters)  # ['h', 'w', 'p']

##################################
# 19. Extract domain names from emails
##################################
emails = ['user1@gmail.com', 'user2@yahoo.com', 'user3@outlook.com']
domains = list(map(lambda x: x.split('@')[1], emails))
print(domains)  # ['gmail.com', 'yahoo.com', 'outlook.com']

##################################
# 20. Add corresponding elements if sum > 10, else 0
##################################
nums1 = [4, 5, 7]
nums2 = [8, 3, 2]
special_sum = list(map(lambda x, y: x+y if (x+y) > 10 else 0, nums1, nums2))
print(special_sum)  # [12, 0, 0]


##################################
# 21. Keep even numbers only
##################################
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]

##################################
# 22. Keep odd numbers only
##################################
odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)  # [1, 3, 5]

##################################
# 23. Keep numbers greater than 5
##################################
greater_than_five = list(filter(lambda x: x > 5, nums))
print(greater_than_five)  # [6]

##################################
# 24. Keep strings longer than 4 characters
##################################
words = ['cat', 'tiger', 'lion', 'elephant']
long_words = list(filter(lambda x: len(x) > 4, words))
print(long_words)  # ['tiger', 'elephant']

##################################
# 25. Keep positive numbers
##################################
numbers = [-5, -1, 0, 2, 8]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)  # [2, 8]

##################################
# 26. Keep numbers divisible by both 2 and 3
##################################
nums = [3, 6, 9, 12, 15, 18]
div_2_and_3 = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, nums))
print(div_2_and_3)  # [6, 12, 18]

##################################
# 27. Keep emails ending with '@gmail.com'
##################################
emails = ['user1@gmail.com', 'user2@yahoo.com', 'user3@gmail.com']
gmail_only = list(filter(lambda x: x.endswith('@gmail.com'), emails))
print(gmail_only)  # ['user1@gmail.com', 'user3@gmail.com']

##################################
# 28. Keep numbers between 10 and 20 (inclusive)
##################################
nums = [5, 10, 15, 20, 25]
between_10_20 = list(filter(lambda x: 10 <= x <= 20, nums))
print(between_10_20)  # [10, 15, 20]

##################################
# 29. Keep names starting with 'A'
##################################
names = ['Alice', 'Bob', 'Alex', 'Brian', 'Angela']
a_names = list(filter(lambda x: x.startswith('A'), names))
print(a_names)  # ['Alice', 'Alex', 'Angela']

##################################
# 30. Keep odd numbers and square them
##################################
nums = [1, 2, 3, 4, 5]
odd_squares = list(map(lambda x: x**2, filter(lambda x: x%2!=0, nums)))
print(odd_squares)  # [1, 9, 25]


###########################
# Categorize into minor or adult
###########################
age_category = lambda age: "Minor" if age < 18 else "Adult"
print(age_category(16))  # Minor