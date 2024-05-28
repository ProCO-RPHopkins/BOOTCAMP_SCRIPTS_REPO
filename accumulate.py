total = 0  # This could be named anything but make sure it makes sense

for num in [1,2,3,4,5,]:
    total = total + num # Could use total += num as well

print(total)

for i in range(5):
    print(i)

for i in range(1,6):
    total += i
print(total)

def count_occurrences(elements, target):
    count = 0
    for i in elements:
        if target == i:
            count += 1
    return count # elements are the list of numbers. Target is the 2 (or occurrences) in print statement
elements = [1,2,3,2,4,2,5]

print(count_occurrences(elements, 1)) # Shows one occurrence of 1
print(count_occurrences(elements, 2)) # Shows three occurrences of 2
print()

def find_max(numbers):
    max = numbers[0]
    for i in numbers:
        if max < i:
            max = i
    return max

numbers = [5,2,6,8,9]

print(find_max(numbers))