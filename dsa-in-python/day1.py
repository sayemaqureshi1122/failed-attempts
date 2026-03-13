# Strings and arrays
# arr1 = [1, 2, 3, 4]
# arr1.reverse()
# print(arr1)
# arr1.append(0)
# print(arr1)
# arr1.pop(3)
# print(arr1)
# arr1.remove(3)
# print(arr1)
# arr1.insert(1, 1)
# print(arr1)
# arr1.sort()
# print(arr1)


# str1 = "sayema"
# str1.split()
# print(str1)
# str1.isdigit()

# ## questions
# Q1] Take a number from user and print if it's even or odd.
# num = int(input())
# if num % 2 == 0:
#     print(f"{num} is a even number")
# else:
#     print(f"{num} is a odd number")

# #Q2] Take a string and print its first and last character.
# s = input().strip()
# print(s[0])
# print(s[-1])

# # 3] Print Numbers From 1 to 20
# for i in range(1, 21):
#     print(i)

# #Q4] Print the Greater of Two Numbers
# a, b = map(int, input().split())
# if a == b:
#     print("equal")
# else:
#     print(max(a, b))

# #Q5] Print a Name Multiple Times
# s = input().strip()
# n = int(input())
# for i in range(n):
#     print(s)
    
# #Q6] Count Vowels in a String
# s = input().strip()
# lower_s = s.lower()
# vowels = "aeiou"
# # count = 0
# # for ch in s:
# #     if ch in vowles:
# #         count += 1

# # for i in s:
# #     if i == "a" or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i =='A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
# #         count += 1
# count = sum(1 for ch in lower_s if ch in vowels)
# print(count)

# #Q7] Reverse a String Using Slicing
# s = input().strip() 
# # print(s[::-1])
# rev = []
# n = len(s) - 1
# while(n >= 0):
#     # rev += s[n]
#     rev.append(s[n])
#     n -= 1
# print("".join(rev))

# Q8] Count Digits in an Integer

# n = int(input())
# to_string = str(n)
# print(len(to_string))

# n = int(input())
# n = abs(n)
# if n == 0:
#     print(1) 
# else:  
#     count = 0
#     while (n > 0):
#         n= n//10
#         count += 1
#     print(count)

# #Q2239 leetcode   // try this again
# nums = list(map(int, input().split()))
# closest_num = nums[0]
# for i in nums:
#     if abs(i) < abs(closest_num):
#         closest_num = i
# if closest_num < 0 and abs(closest_num) in nums:
#     print(abs(closest_num))
# else:
#     print(closest_num)
