# #unicode -  a unique code given to each char present in the world which helps to set the same standard of char code throughout the world.

# print("\u2602") # prints an umbrella

# #multiline string -  to print that we can use escape seq char (\n) or we can use triple single or double quote.

# print('''A single drop, day after day,
# Will carve the hardest stone away.
# It isn’t speed that wins the climb,
# But showing up, one step at time.''')

# # indexing - accessing each item of str
# name = "sayema"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])

# # looping through the str
# print("using for loop")
# for character in name:
#     print(character)

#indexing
name = "sayema"
print(name[:]) # by default python adds 0 - start  and len(str) - at the end
 
# for -ve indexing the python adds len(str) - index to get the +ve index
# here it will be len(name) -1 : len(name) -4 => 5-1 : 5-4 => 4:1  not possible so prints nothing
print(name[-1:-4])
print(name[::-1])
print(name.upper())


