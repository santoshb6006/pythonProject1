# ATM try to get the money when you try to withdraw more than limit.
# This need to be handle using exception. To enhance the user experience

try:
    bal = 1000
    pin: int = int(input("Enter the pin number:\n"))
    if pin == 123456:
        print("Welcome to the HDFC Bank")
        amount = int(input("Enter the amount to be withdrawn\n"))
        if amount < bal:
            print("Please collect the cash")
except Exception as e:
        print(e)
        print("Please enter valid amount:", e)
