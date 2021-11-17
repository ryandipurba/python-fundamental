# if

numbers = 8

if numbers < 10:
    print(f'{numbers} is less than 10')
elif numbers > 10:
    print(f'{numbers} is greater than 10')
else:
    print(f'{numbers} equal 10')

# for
print("\nloop")
number = [1, 2, 3, 4, 5]
for x in number:
    print(x)

fruits = ["pineapple", "apple", "orange"]
for food in fruits:
    print("I like eat", food)

print('\nwhile loop')
count = 0
while count < 9:
    print("The count is: ", count)
    count = count + 1

print("Hello Good bye!")
