# floor = "sticky"
# walls = "clean"
# if floor == "sticky": # don't forget the colon
#     print("Clean the floor!")
#     # more lines of code in this code block
#     # need to be indented as well
#     print("This print is in the codeblock!")
# # print("This print is NOT IN THE CODEBLOCK!")
# if walls == "sticky":
#     print("Clean the walls!")

# age = 20
# location = "Los Angeles"
# if age >= 21:
#     print("Have a milk cocktail")
# elif age < 21 and location == "Los Angeles":
#     print("Oat milk for you")
# else:
#     print("Strawberry milk for you")


color = ''
while color != 'quit':
    color = input('Enter "green", "yellow", "red": ').lower()
    if color == 'red':
        print('stop')
    elif color == 'green':
        print('go')
    elif color == 'yellow':
        print('wait')
    elif color == 'quit':
        break
    else:
        print('bogo')



# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):
# 2. Write the code that determines whether the letter entered is a vowel

# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':
# letter = input('Please enter a letter from a-z or A-Z: ').lower()
# if letter in 'aeiou':
#     print(f'letter {letter} is a vowel')
# else:
#     print(f'the letter {letter} is a consonant')



# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
# phrase = ''
# while phrase != 'quit':
#     phrase = input('Please enter a word or phrase ').lower()
#     if phrase == 'quit':
#         break
#     else: 
#         print(len(phrase))

    

# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

# age = input('Please enter a dog age: ') 
# converted_Age = int(age)
# dogYears = 0;
# if converted_Age < 3:
#     dogYears = 10 * converted_Age
#     print(f'The dogs age in dog years is {dogYears}')
# else:
#     dogYears = 20 + (converted_Age-2) * 7
#     print(f'The dogs age in dog years is {dogYears}')
    



# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
# print(' Enter the lengths of three side of a triangle:')
# a = input('a:  ') 
# b = input('b:  ') 
# c = input('c:  ') 

# if a == b == c:
#     print(f'A triangle with sides of {a}, {b} & {c} is a  equilateral triangle')
# elif a == b or a == c or b == c:
#     print(f'A triangle with sides of {a}, {b} & {c} is a  isosceles triangle')
# else:
#     print(f'A triangle with sides of {a}, {b} & {c} is a  scalene triangle')



# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):
# number = []
# sum = 0
# for n in range(50):
#     if n == 0:
#         number.append(0)
#         print(f" term: {n} / number: {number[n]}")
    
#     elif n ==1:
#         number.append(1)
#         print(f" term: {n} / number: {number[n]}")
#     else:
#         sum = number[n-1] + number[n-2]
#         number.append(sum)
#         print(f" term: {n} / number: {number[n]}")





# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.


month = input('Enter the month of the year (Jan - Dec):  ').lower() 
day = input('Enter the day of the month: ')
winter = ['dec','jan','feb','mar']
spring = ['mar','apr','may','jun']
summer = ['jun','jul','aug','sep']
fall = ['sep','oct','nov','dec']

if month == 'dec':
    if day < 21:
        print(f'{month} {day} is in Fall ')
    else:
        print(f'{month} {day} is in Winter ')
if month == 'mar':
    if day <= 19:
        print(f'{month} {day} is in Winter ')
    else:
        print(f'{month} {day} is in Spring ')
if month == 'jun':
    if day <= 20:
        print(f'{month} {day} is in Spring ')
    else:
        print(f'{month} {day} is in Summer ')
if month == 'sep':
    if day <= 21:
        print(f'{month} {day} is in Summer ')
    else:
        print(f'{month} {day} is in Fall ')
elif month in winter:
    print(f'{month} {day} is in Winter ')
elif month in 
# if month in winter:
#     if month == 'dec':
#         if day >= 21:
#             print(f'{month} {day} is in winter ')



# names = ["Tom", "Deborah", "Murray", "Axel"]

# for name in names:
#   print(name)


# for num in range(10):
#     print(num)

# print(range(10))

# for evenNum in range(2, 10, 2):
#     print(evenNum)

# nums = list(range(10))
# print(nums)
# odds = tuple(range(1, 10, 2))
# print(odds)

# for num in range(5, 0, -1):
#   print(num)
