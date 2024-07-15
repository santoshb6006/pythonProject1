# Pass some information to the function
def allow_to_attend_class(name,password):
    if name == "Santosh":
        if password == "Yes":
            print("you are allowed dude")
    else:
        print("You are not allowed")


allow_to_attend_class("Santosh","Yes")
