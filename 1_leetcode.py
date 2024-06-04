lists = ["a", "b", "c", "d"]

for l in lists:
    print(l)


s = "cabcacdd"
count = 0

for letters in s:
    if letters == "a":
        count += 1
        result = count

print(f"There are {result} 'a's in the list.")