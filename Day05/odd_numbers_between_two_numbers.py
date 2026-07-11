start = int(input("Enter the first number: "))
end = int(input("Enter the second number: "))
for i in range(start, end + 1):
    if i % 2 != 0:
        print(i)
