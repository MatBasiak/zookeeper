# put your python code here
m1_h = int(input())
m1_m = int(input())
m1_s = int(input())
m2_h = int(input())
m2_m = int(input())
m2_s = int(input())

m1 = 3600 * m1_h + 60 * m1_m + m1_s
m2 = 3600 * m2_h + 60 * m2_m + m2_s

print(m2 - m1)
