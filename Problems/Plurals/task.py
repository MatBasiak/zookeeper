number = int(input())
word = input()

# write a condition for plurals
if number >= 2 or number == 0:
    word += "s"
print(number, word)
