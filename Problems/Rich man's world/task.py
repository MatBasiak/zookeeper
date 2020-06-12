deposit = int(input())
counter = 0
while deposit <= 700000:
    counter += 1
    deposit += (deposit / 100) * 7.1
print(counter)
