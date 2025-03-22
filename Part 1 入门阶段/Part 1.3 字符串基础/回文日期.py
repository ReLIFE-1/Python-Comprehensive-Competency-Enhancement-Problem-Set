def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
    
def is_pal(date):
    s = str(date)
    return s == s[::-1]

def days(year,month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    if month in [4,6,9,11]:
        return 30
    if is_leap(year) and month == 2:
        return 29
    else:
        return 28

def is_vaild(date):
    year = date // 10000
    month = date % 10000 // 100
    day = date % 100
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days(year,month):
        return False
    return True

start_date = int(input())
end_date = int(input())
cnt = 0
for i in range(start_date,end_date + 1):
    if is_pal(i) and is_vaild(i):
        cnt += 1

print(cnt)
