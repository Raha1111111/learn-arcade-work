# 11.5.1.1
for i in range(10):
    print("Hi")

# 11.5.1.2
for i in range(5):
    print("Hello")
print("There")

# 11.5.1.3
for i in range(5):
    print("Hello,")
    print("There")

# 11.5.1.4
for i in range(10):
    print(i)

# 11.5.1.5
for i in range(1, 11):
    print(i)

# Another way Print the numbers 1 to 10.
for i in range(10):
    # Add one to i, just before printing
    print(i + 1)

# 11.5.1.6
# One way to print the even numbers 2 to 10
for i in range(2, 12, 2):
    print(i)

# Another way to print the numbers 2 to 10
for i in range(5):
    print((i + 1) * 2)

# 11.5.1.7
for i in range(10, 0, -1):
    print(i)

# 11.5.1.8
for item in [2, 6, 4, 2, 4, 6, 7, 4]:
    print(item)

# 11.5.1.9
for i in range(3):
    print("a")
    for j in range(3):
        print("b")

# 11.5.1.10
a = 0
for i in range(10):
    a = a + 1
print(a)

# 11.5.1.11
a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1
print(a)
# 11.5.1.12

a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)

# 11.5.1.13
total = 0
for i in range(1, 101):
    total += i
print(total)
