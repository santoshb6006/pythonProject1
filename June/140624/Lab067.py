def allow_to_class(name,passu):
    match name, passu:
        case "Dingg", "sss":
                print("You are allowed, case1")
        case "Pengi", "123":

                print("You are allowed, case2")
        case _:
                print("You are not allowed")


allow_to_class("Dingg","sss")
allow_to_class("Dingg","sss87")



# def allow_to_class(name):
#     match name:
#         case "Dingg":
#             print("You are allowed, case1")
#         case "Pengi":
#             print("You are allowed, case2")
#         case _:
#             print("You are not allowed")
#
#
# allow_to_class("Dingg")
