#problem 1
for i in range(10):
    print("*", end=" ")
print("\n")
#problem 2
for i in range(10):
    print("*", end=" " )
print("")
for i in range(5):
    print("*", end=" ")
print()
for i in range(20):
        print("*", end=" ")
print("\n")
#problem 3
for row in range(10):
    for column in range(10):
        print("*", end=" ")
    print("")
#problem 4
for row in range(10):
    for column in range(5):
        print("*", end=" ")
    print("")
#problem 5
for row in range(5):
    for column in range(20):
        print("*", end=" ")
    print("")
#problem 6
for i in range(10):
    for j in range(10):
        print(j, end=" ")
    print("")
#problem 7
for i in range(10):
    for j in range(10):
        print(i, end=" ")
    print("")
#problem 8
for i in range(10):
    for j in range(i + 1):
        print(i, end=" ")
    print("")
#problem 9
for i in range(10):
    for j in range(i):
        print(" ", end=" ")
    for j in range(10 - i):
        print(j, end=" ")
    print()

for i in range(10):
    for j in range(10-i):
        print(j, end=" ")
    print()

#problem 10

for i in range(1, 10):
    for j in range(1, 10):
        if i * j < 10:
            print(" ", end="")

        print(i * j, end=" ")

    print()

for i in range(1, 13):
    for j in range(1, 13):
        if i * j < 100:
            print(" ", end="")
        if i * j < 10:
            print(" ", end="")

        print(i * j, end=" ")

    print()

#problem 11
for i in range(10):
    for j in range(10 - i):
        print (" ", end=" ")
    for j in range(1, i + 1):
        print (j, end=" ")
    for j in range(i - 1, 0, -1):
        print (j, end=" ")
    print()
#problem 12
for i in range(10):
    for j in range(10 - i):
        print (" ", end=" ")
    for j in range(1, i + 1):
        print (j, end=" ")
    for j in range(i - 1, 0, -1):
        print (j, end=" ")
    print()
