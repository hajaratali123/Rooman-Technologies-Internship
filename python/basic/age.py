age = int(input("Enter your age: "))
isCitizen = input("Are you a citizen? (True/False): ")

if age >= 18 and isCitizen == "True":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")