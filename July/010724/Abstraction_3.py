from abc import ABC, abstractmethod
class ATB(ABC):
    @abstractmethod
    def perform_test1(self):
        pass
    def perform_test2(self):
        pass
class Santosh(ATB):
    def perform_test1(self):
        print("Task one is done")
    def perform_test2(self):
        print("Task two is done")

class Madhu(ATB):
    def perform_test1(self):
        print("Task one is not done")
    def perform_test2(self):
        print("Task two is done")


santu=Santosh()
santu.perform_test1()
santu.perform_test2()

madhu=Madhu()
madhu.perform_test1()
madhu.perform_test2()