input_string = input("Enter numbers : ")
numbers = input_string.split()

largest = float(numbers[0])

for i in range(1, len(numbers)):
    current = float(numbers[i])
    if current > largest:
        largest = current

print("The largest number is:", largest)