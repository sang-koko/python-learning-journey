start = int(input("Enter the first number: "))
end = int(input("Enter the second number: "))
sum = 0
for i in range(start, end + 1):
    if i % 2 == 0:
        sum += i

print("Sum of even numbers =", sum)
