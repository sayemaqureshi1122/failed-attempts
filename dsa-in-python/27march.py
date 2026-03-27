#leap year logic
'''
1] when single decision problem we use --> if-else, when need multiple iterations over change state -- > loops
'''
def is_leap_year(year):
    if year <= 0:
        return False
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    else :
        return year % 4 == 0
res = is_leap_year(2024)
print(res)