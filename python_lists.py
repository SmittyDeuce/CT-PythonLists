# 1. Python List Transformation
# Objective:
# The aim of this assignment is to practice advanced list operations and transformations.

# Problem Statement:
# You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.

# Task 1: Given the list of grades:
# Sort the grades in descending order and display the sorted list.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# print(sorted(grades))


# Task 2: Calculate the average grade and display it.

# def average_calculator(lists):
#     listLength = len(lists)
#     print(listLength)
#     if ( len(lists) == 0):
#         return 0
#     else:
#         firstElement = lists.pop(0)
#         totalSum = firstElement + average_calculator(lists)
#         return totalSum / listLength
# print(average_calculator(grades))

def average_calculator(lists):
    totalSum = sum(grades)
    average = totalSum / len(lists)
    print(average)
# average_calculator(grades)

# Task 3: Replace any grade below 80 with the value Failed.
def replaceWithFailed(lists):
    for element in lists:
        if (element < 80):
            lessThan80 = lists.index(element)
            lists[lessThan80] = 'Failed'
    print(lists)
# replaceWithFailed(grades)

# 2. Advanced List Methods and Identity Operators
# Objective:
# The aim of this assignment is to delve deeper into list methods and understand the nuances of identity operators.

# Problem Statement:
# You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

# Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
# Find out which students both submitted their assignments and attended the class.
# for name in submitted:
#     if name in attended:
#         print(f'{name} has submitted their assignments and attended class')

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.
# if sorted(submitted) == sorted(attended):
#     print(True)
# else:
#     print(False)
        
# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.
def removeStudent (list1, list2):
    for student in list1:
        if (student in list1) and (student not in list2):
            list1.remove(student)
    print(list1)
# removeStudent(attended, submitted)

# 3. Advanced Slicing Techniques
# Objective:
# The aim of this assignment is to master the art of slicing in Python lists.

# Problem Statement:
# You have a list of daily temperatures for a month, and you'd like to extract specific data from it.

# Task 1: Given the list of temperatures:

# temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
# Extract the temperatures for the second week (7 days) of the month.
#  try gettting idx from elements 8-14 and print those ones
# Task 2: Extract all the temperatures above 100.

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

# 4. List Comprehensions and Membership Operators
# Objective:
# The aim of this assignment is to practice using list comprehensions and membership operators in Python.

# Problem Statement:
# You have a list of numbers, and you'd like to generate a new list based on certain conditions.

# Task 1: Given the list:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use a list comprehension to create a new list containing only even numbers.

# Task 2: Use a list comprehension to create a new list containing numbers greater than 5.

# Task 3: Check if the number 7 is in the original numbers list.

# 5. Deep Dive into Python Lists
# Objective:
# The aim of this assignment is to integrate various list operations and methods to solve a complex problem.

# Problem Statement:
# You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

# Task 1: Given the lists:

# students = ["John", "Doe", "Jane", "Smith"]
# grades = [85, 90, 78, 88]
# activities = ["Football", "Music", "Art", "Dance"]
# Create a new list where each element is a dictionary with keys name, grade, and activity and the corresponding values from the provided lists.

# Task 2: Filter out students who have grades below 80.

# Task 3: For the remaining students, add a new key-value pair in their dictionary: "status": "Passed".

