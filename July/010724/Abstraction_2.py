from abc import abstractmethod


class Automations():
    @abstractmethod
    def payfee(self):
        pass
    def enrolled(self):
        print("you are enrolled")

class Santosh(Automations):

    def payfee(self):
        print("fee paid by son")

class Madhu(Automations):
    pass
    def payfee(self):
        print("fee not paid by madhu")

santu=Santosh()
(santu.payfee())

madhu= Madhu()
(madhu.payfee())