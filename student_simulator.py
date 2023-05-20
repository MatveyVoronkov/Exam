import random

class Student:
    def __init__(self, name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True

    def to_study(self):
        print("I will speep")
        self.gladness -= 3
        self.progress += 0.12

    def to_slepp(self):
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out.....")
            self.alive = False

        elif self.gladness <= 0:
            print("Deprestion...")
            self.alive = False

        elif self.gladness >5:
            print("Passed exectly...")
            self.alive = False

