# if condtion:
# code to be executed if the condition is true
# else :
# code to be executed if the condition is false

age = int(input("Enter the customer age\n"))
if age >= 18:
    print("You are eligible to vote")
    if age < 35:
        print("You are eligible to join the army")
else:
    print("You go n watch pogo")
