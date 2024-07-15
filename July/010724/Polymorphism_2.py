class Father():
    def home(self):
        # return "Old Home"
        print("Old Home 5 bhk")


class Son(Father):
    pass
    def home(self):
    # #     return "New Home10 bhk"
    #         print("new Home 10 bhk")
            super().home()
            print("new Home 11 bhk")


son = Son()
print(son.home())
