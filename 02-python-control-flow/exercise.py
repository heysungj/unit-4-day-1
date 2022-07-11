# floor = "sticky"
# walls = "clean"
# if floor == "sticky": # don't forget the colon
#     print("Clean the floor!")
#     # more lines of code in this code block
#     # need to be indented as well
# #     print("This print is in the codeblock!")
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

# color = ""
# while color != 'quit':
# # while True:
#     color = input('Enter "green", "yellow", "red": ').lower()
#     print(f'The user entered {color}')

#     if color == "green":
#         print("Go!")
#     elif color == "yellow":
#         print("Slow Down!")
#     elif color == "red":
#         print("Stop!")
#     # elif color == "quit":
#     #     break
#     else:
#         print("Bogus!")

# names = ["Tom", "Deborah", "Murray", "Axel"]

# for name in names:
#   print(name)


# for num in range(10):
#     print(num)

# print(range(10))

# for evenNum in range(2, 10, 2):
#     print(evenNum)

nums = list(range(10))
print(nums)
odds = tuple(range(1, 10, 2))
print(odds)

for num in range(5, 0, -1):
  print(num)
