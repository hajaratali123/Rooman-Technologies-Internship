start = int(input("Enter the starting number: "))

print("Even numbers from" , 1, "to", start)
for i in range(1, start ):
    if i % 2 == 0:
        print(i)
print("Odd numbers from", 1, "to", start)
for i in range(1, start):
    if i % 2 != 0:
        print(i)

print("while loop : ")

while start >= 0:
    if start % 2 ==0:
        print(start,"number id even ")
    else:
        print(start,"number is odd ")