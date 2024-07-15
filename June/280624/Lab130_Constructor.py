# Web Automation-Selenium
# Page- is a real world entity

class VWOLoginPage:
    email = None
    pwd = None

    # def __init__(self, email,pwd):
    def __init__(self, email_arg, pwd_arg):
        self.email = email_arg
        self.pwd = pwd_arg

    def login_conf(self):
        if self.pwd == "123456":
            print(f" {self.email},Login Allowed")
        else:
            print(f" {self.email}, Not Allowed")


amit = VWOLoginPage("fsdjhkdgs@mail.com", "543123")
amit.login_conf()

sant = VWOLoginPage("sant@gmail.com", "123456")
sant.login_conf()
