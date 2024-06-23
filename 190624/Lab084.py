#lambda arguments:expression
def find_odd_even(num):
    if num%2==0:
        print("Even num", num)
    else:
        print("Odd num", num)

find_odd_even(121)

Odd_eve=lambda num: "Even" if num%2==0 else "odd"
print(Odd_eve(13))
print(Odd_eve(314))