#1
for number in range(2, 21, 2):
    print(number)

#2
my_string = "Olympic College"
for char in my_string:
    print(char.upper())

#3
n = int(input("Enter a positive integer: "))
while n <= 0:
    n = int(input("Please enter a positive integer: "))

total_sum = 0
for i in range(1, n + 1):
    total_sum += i

print("The sum of integers from 1 to", n, "is:", total_sum)

#4
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2}", end="   ")
    print()

#5
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        print("Exiting...")
        break
    print(f"You entered {number}")
