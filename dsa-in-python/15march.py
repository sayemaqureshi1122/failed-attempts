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

#Q5] — Lists: Write a function:def find_max(nums):Return the largest element in the list without using max().
# def find_max(nums):
#     max = 0
#     for i in range(len(nums)):
#         if nums[i] > max:
#             max = nums[i]
#     return max  
# res = find_max([3, 7, 2, 9, 1]) 
# print(res)  

#Q6] Question 6 — Dictionaries - > Write a function:def count_letters(word):Return a dictionary showing frequency of each character.

# Q8] Strings - Write a function:def is_palindrome(s):Return True if string is palindrome.

# def is_palindrome(s):
#     new_s = s[len(s)::-1]
#     if new_s == s:
#         return "is palindrome"
#     else:
#         return "not a palindrome"        
# res = is_palindrome("12231")
# print(res)
#list comprehension
# result = [(i*i) for i in range(1,21)if (i%2)==0]
# print(result)


'''Loops -> 
Note: do while not used in python but we can enumerate it using while with infinite loop and break statement'''
# i = 0
# while True:
#     print(i)
#     if(i % 2 == 0):
#         print("even")
#         break
#     i += 1
    

''' 1️⃣ Count digits in a number'''
# def count_digits(n):
#     count = 0
#     while(n>0):
#         digit = n % 10
#         count += 1
#         n = n // 10
#     return count
# res = count_digits(12)
# print(res)


'''2️⃣ Sum of digits'''
# def sum_of digits(n):
#     total = 0
#     while(n>0):
#         digit = n % 10
#         total += digit
#         n = n // 10
#     return total
# res = sum_of_digits(128)
# print(res)

'''3️⃣ Reverse a number (no string conversion)'''
def reverse_no(n):
    reversed_no = 0
    while(n > 0):
        digit = n % 10
        reversed_no = reversed_no * 10 + digit
        n = n // 10
    return reversed_no
res = reverse_no(12445)
print(res)
'''4️⃣ Check palindrome number'''
# def is_palindrome(n):
#     original_number = n
#     reversed_no = 0
#     while(n > 0):
#         digit = n % 10
#         reversed_no = reversed_no * 10 + digit
#         n = n // 10
#     return(original_number == reversed_no)
# res = is_palindrome(12331)
# print(res)

'''5️⃣ Print digits individually'''
# def individual_digits(n):
#     while(n>0):
#         digit = n % 10
#         print(digit)
#         n = n // 10
# individual_digits(123454)
  

        
      

