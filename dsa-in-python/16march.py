''' if-elif-else statement - >
    1] greater than - >
    2] less than - <
    3] greater than equal - >=
    4] less than equal - <=
    5] assignment - =
    6] equal - ==
    7] strictly equal - ===
    8] is - this one checks that if it is the same object or not that means it checks 
    (id(a) == id(b)) cuz each obj stored in the mem has different id and that's how it differs from ==.
    
    
    False values:
        False - boolean
        None
        Zero
        empty sequence - "" -> empty str, () -> empty tuple, [] -> empty list, {} -> empty dict.
'''

'''Q1] Problem 1 — Even or Odd'''
# def check_even_odd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# res = check_even_odd(28)
# print(res)

''' Q2] Problem 2 — Positive / Negative / Zero'''
# def number_type(n):
#     if n == 0:
#         return "Zero"
#     elif n > 0:
#         return "Positive"
#     else:
#         return "Negative"
# res = number_type(0)
# print(res)

'''Q3] Problem 3 — Largest of Three Numbers'''
# def largest_of_three(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else :
#         return c
# res = largest_of_three(4, 5, 5)
# print(res)

# #using built -in function
# list1 = [1, 5, 5]
# print(max(list1))

# def largest_of_three(a, b, c):
#     largest = a
#     if b > largest:
#         largest = b
#     if c > largest :
#         largest = c

#     return largest

# res = largest_of_three(1, -4, 3)
# print(res)
    

# '''Q4] Problem 4 — Leap Year'''
# def is_leap_year(year):
#     if year % 400 == 0 :
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
# res = is_leap_year(1900)
# print(res)

'''Note: always use boolean logic instead of "is a leap year" use true false. '''

'''Q5] Problem 5 — Grade Calculator'''
# def calculate_grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 75 and marks <= 89:
#         return "B"
#     elif marks >= 50 and marks <= 74:
#         return "C"
#     elif marks >= 35 and marks <= 49:
#         return "D"
#     else:
#         return "F"
# res = calculate_grade(35)
# print(res)