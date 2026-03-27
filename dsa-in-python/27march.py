#leap year logic
'''
1] when single decision problem we use --> if-else, when need multiple iterations over change state -- > loops
2] below one is known as early return pattern wherein pura code run nhi hota jaise kaam hua waise controller bahar aa jata hai which helps in making the program faster.
'''
# def is_leap_year(year):
#     if year <= 0:
#         return False
#     if year % 400 == 0:
#         return True
#     if year % 100 == 0:
#         return False
#     else :
#         return year % 4 == 0
# res = is_leap_year(2024)
# print(res)

'''List  methods -- >
1] list1.append()
2] list1.remove()
3] list1.pop()
4] list1.extend(list2) --> can be used to convert nested list(2d, 3d) into a 1d list
5] list1.insert(index, "value")
6] min()
7] max()
8] sum() above 3 can be directly used with print statements
9] list1.sort() - by default ascending
    to do in descending - list1.sort(reverse = True)
10] list1.reverse()
11] sorted function - > var1 = sorted(list1)
12] list1.index()
13] enumerate function - > prints index, values --> enumerate(list1, start = value) print(index, list1)
14] in operator - > to check if the value is present in the list
15] .join() - to convert a list into a single string
        syntax - 'separator'.join(list1)
16] .split()

Tuple methods -->
None is immutable to make a change make it a list do the changes then change back to another tuple


Set methods -- > cannot store duplicate values
1] set1.intersection(set2) - common value in both the sets
2] set1.difference(set2) - different values in both the sets
3] set1.union(set2) - all the values together
4] set(set1) - to create an empty set cuz set1 = {} becomes a dict
'''

courses = ["maths", "bio", "chem", "physics", "english"]
courses.insert(1, "art")
courses.remove("art")
courses.pop()
courses2 = ["art", "sports", "design"]
courses.extend(courses2)
courses.sort()
courses.reverse()
sorted_courses = sorted(courses)
print(sorted_courses)
print("bio" in courses)
print(sorted_courses.index("maths"))
h1 = list(enumerate(sorted_courses))
print(h1)
h2 = enumerate(sorted_courses)
print(next(h2)) 


tuple1 = (1, 2, 3, 4)
l1 = list(tuple1)
l1.insert(0, 0)
tuple2 = tuple(l1)

print(tuple1)
print(tuple2)


set1 = {"math", "science", "sports"}
set2 = {"art", "design", "math"}
print(set1.intersection(set2))
print(set1.difference(set2)) # set 1 ke reference me
print(set2.difference(set1))
print(set1.union(set2))
