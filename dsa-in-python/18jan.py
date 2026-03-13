# ## reverse a string
# str1  = input("enter a string : ")
# rev = ""
# for i in str1:
#     rev = i + rev
    
# print(rev)

# for index, value in enumerate(str1):
#     print(index, value)
    
# ## count no of char in string
# str2 = input("enter : ")
# count = 0
# for i in str2 :
#     count += 1
    
# print(count)

num1 = int(input("enter a num: "))
sum  = 0 
while num1 > 0:
    last_digit = num1 // 10
    

print(sum)


list1 = list(map(int, input().split()))
min = list1[0]
for i in range(len(list1)-1):
    if list1[i] < min:
        min  = list1[i]
print(min)