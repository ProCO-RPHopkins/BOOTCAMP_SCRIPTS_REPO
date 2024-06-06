
s = "cabcacdd"

def count_letters(s, letter):
    return sum(1 for l in s if l == letter)

count_a = count_letters(s, "a")
count_b = count_letters(s, "b")
count_c = count_letters(s, "c")
count_d = count_letters(s, "d")

print(f"There are {count_a} a's in the string.")
print(f"There are {count_b} b's in the string.")
print(f"There are {count_c} c's in the string.")
print(f"There are {count_d} d's in the string.")
print()
print()

from collections import Counter

s = "cabcacdd"
counts = Counter(s)

for letter in 'abcd':
    print(f"There are {counts[letter]} {letter}'s in the string.")



