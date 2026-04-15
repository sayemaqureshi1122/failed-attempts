# ''' STRING METHODS '''
# # 1] .upper() 
# ''' Logic - 
# 1] a var to store the res.
# 2] then loop through each char of  the string and convert it into it's unicode using ord() method
# 3] check if the char is a lower case and in order to be that it's code has to be in range 97-122.
# 4] if yes then sub that code from 32 as the exact difference between the a-z and A-Z is 32 (ie a - 97 and A - 65, so 97-32 = 65 =>A)
# 5] if it's already a upper case, space, number keep it as it is.'''
# a = "A"
# print(ord(a))


# def manual_upper_method(text):
#     result = ""
#     for character in text:
#         char_code = ord(character)
#         if char_code>= 97 and char_code <= 122:
#             to_upper = char_code - 32
#             num_to_char = chr(to_upper)
#             result += num_to_char
#         else:
#             result +=character
#     return result
# input_str = "hello my name is sayema"
# res = manual_upper_method(input_str)
# print(res)

# # 2] .lower()

# '''Logic - 
# 1] a var to store resultant str as strings as immutable we cannot use the og one.
# 2] run a for loop for each char and check if it's char_code is between A - 65 to Z - 90.
# 3] if yes then add +32 to the char code to get lower case.
# 4] if already a lower, space , number add the character as it is to the resultant string.'''

# def manual_lower_method(text):
#     result = ""
#     for character in text:
#         char_code = ord(character)
#         if char_code >= 65 and char_code <= 90:
#             result += chr(char_code + 32)
#         else:
#             result += character
#     return result
# input_str = "Hello World! 123 @ HELLO GOOD AFTERNOON EVERYONE"
# res = manual_lower_method(input_str)
# print(res)

# 3] .strip() 

''' Logic - 
1] will start from left side of the str
2] apply a loop until the start is less than len(str) and value of start is white space.
3] if yes is incremented to next iteration to check if the next char if white space.
4] else not a white space moves out the loop
5] now from the end will apply the loop to check if end[str] is white space 
6[ if yes end is decremented in order to check the next string
7] finally print just the part where start and end string ended to remove all the white spaces from the starting and from the end of the given string .'''


# str2 = "                Hello Fellow programmer i am learning python       " # here when i  print the normal string it includes all the spaces as well which can be unnecessary to just get the valid input we use strip to avoid unnecessary white spaces.
# print(str2)

# def manual_stripMethod(text):
#     start = 0
#     while start < len(text) and text[start] == " ": # using while loop cuz we don't know ramge to run the loop.
#         start += 1
#     end = len(text)-1 
    
#     while end < len(text) and text[end] == " " :
#         end -= 1
#     return text[start : end + 1] # using end+1 cuz the slicing in python exclude the last margin and include the start ones.
# input_str = "                Hello Fellow programmer i am learning python       " # it removes both the preceding and trailing ones.
# res = manual_stripMethod(input_str)
# print(res)
         

# # 3.1] .rstrip()
# def manual_rightStrip(text):
#     end = len(text) - 1
#     while end < len(text) and (text[end] == " " or text[end] == "!") :
#             end -= 1
#     return text[:end + 1]
# input_str = "!!!!Hello Word!!!!!     "   # here as it is a rstrip it only removes the trailing char we want not the preceding ones.
# res = manual_rightStrip(input_str)
# print(res)

# # 3.2] .lstrip()
# def manual_lstripMethod(text):
#     start = 0
#     while start < len(text) and (text[start] == " " or text[start] == "!"):
#         start += 1
#     return text[start:]
# input_str = "!!!!!!!!!       Hello Word!!!!!     " #here since it's left strip it only removes tha preceding char not the trailing ones.
# res = manual_lstripMethod(input_str) 
# print(res)


# # 4] .replace(input_str, old_word, new_word)
# def manual_replace(text, old_word, new_word):
#     result = " "
#     old_len = len(old_word)
#     i = 0
#     while i < len(text):
#         if text[i:i + old_len] == old_word:
#             result += new_word
#             i += old_len
#         else:
#             result += text[i]
#             i += 1
            
#     return result
# input_str = "I have a Red car and a Red bike"
# res = manual_replace(input_str, "a", "is")  
# print(res)

# # 2 edge cases - 1] if we put old word = "a" and new word = "is" we get I hisve is Red cisr isnd is Red bik cuz python doesn't know english it just checks the sequence .
# # 2]  The Case-Sensitivity Problem - "Red".replace("red", "Blue") will do nothing. It returns "Red" unchanged.

# # 5] .count()
# def manual_count(text, word):
#     count = 0
#     word_len = len(word)
#     i = 0
#     while i < len(text):
#         if text[i:i+word_len] == word:
#             count += 1
#             i += word_len
#         else:
#             i += 1
#     return count
# input_str = "apple is a fruit , we should eat apple everyday. An apple a day keeps doctor away"
# res = manual_count(input_str,"apple")
# print(res)

# # 6] find() and index() 
# def manual_findMethod(text, word):
#     i = 0
#     word_len = len(word)
#     while i < len(text):
#         if text[i:word_len+i] == word:
#              return i
#         else : 
#              i += 1
#     #return -1
#     #raise ValueError("substring not found")  #we add this line instead of return -1 for index() method as it throws an error we it cannot find the word in the string.
# input_str = "we should eat apple everyday. An apple a day keeps may doctor away."
# res = manual_findMethod(input_str, "may")
# print(res)


    


        
  