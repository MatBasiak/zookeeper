# put your python code here
first = abs(int(input()))
second = abs(int(input()))
third = abs(int(input()))
total = 0

if first % 2 != 0:
    first += 1
if second % 2 != 0:
    second += 1
if third % 2 != 0:
    third += 1

total = first + second + third
total //= 2
print(total)
