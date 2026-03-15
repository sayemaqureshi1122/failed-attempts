# ## Write a function: Return:"Positive Even","Positive Odd","Negative","Zero"depending on the value of n.
# def check_number(n):
#     if n == 0:
#         return "Zero"
#     elif n > 0:
#         if n & 1:
#             return "Positive Odd"
#         else:
#             return "Positive Even"
#     else:
#         return "Negative"
# res = check_number(0)
# print(res)


#Q3] Write a function:def count_digits(n):Return the number of digits in the integer without using len() or converting to string

# def count_digits(n):
#     count = 0
#     # sum = 0
#     while(n > 0):
#         # digit = n % 10
#         # sum += digit
#         n = n // 10
#         count += 1

#     return count
# res = count_digits(5832)
# print(res)

#Q4] Reverse a Number -> Write a function:def reverse_number(n):Example:reverse_number(1234) → 4321, Do NOT convert to string.
# def reverse_number(n):
#     reversed_number = ""
#     while(n > 0):
#         digit = n % 10
#         digit = str(digit)
#         reversed_number += digit
#         n = n // 10
#     return reversed_number
# res = reverse_number(1234)
# print(res)


        