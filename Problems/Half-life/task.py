start_atoms = int(input())
final_atoms = int(input())
days = 0
while start_atoms >= final_atoms:
    start_atoms //= 2
    days += 12
print(days)
