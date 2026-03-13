arr = list(map(int, input().split()))
your_points = 23
sum = 0
for i in range(len(arr)):
    sum += arr[i]
print(sum)
avg = (sum)/ len(arr)
if avg < your_points:
    print("yes")
else:
    print("no")