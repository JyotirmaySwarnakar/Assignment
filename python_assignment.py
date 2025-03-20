#Q1:
numbers = [5, 12, 3, 8, 9, 1, 23, 6]

largest = numbers[0]  

for number in numbers:
    if number > largest:
        largest = number  

print("The largest number is:", largest)

#Q2:

filename = "jyotirmay.txt"  # Your file name

with open(filename, 'r') as file:
    text = file.read()
    
lines = text.split('\n')
line_count = len(lines)
word_count = len(text.split())
char_count = len(text)

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)
