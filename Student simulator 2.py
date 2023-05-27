import random
money = 100
class Student:
    def __init__(self, name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True

    def to_eat(self):
        print("Dog will eat")
        self.gladness -= 3
        self.progress += 0.12

    def to_slepp(self):
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        print("You need money to chill")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out.....")
            print("You need to study harder")
            self.alive = False

        elif self.gladness <= 0:
            print("Depression")
            self.alive = False

        elif self.gladness >5:
            print("Good mood")
            print("Do you want to chill")
            self.alive = False

    def end_on_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress)}')

    def elive(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f'{day:=^50}')
        print('1 - to study')
        print('2 - to slipp')
        print('3 - to chill')
        live_cube = (input('Enter your choise:'))
        if live_cube == 1:
            print('You entered 1 variant (study)')
            self.to_eat()
            money += 1
        elif live_cube == 2:
            print('You entered 2 variant (slepp)')
            self.to_slepp()
        elif live_cube == 3:
            print('You entered 3 variant (chill)')
            self.to_chill()
            money -= 1
        else:
            print('Not correct choise.You can enter only 1 or 2 or 3')
        self.end_on_day()
        self.is_alive()
nick = Student(name ='nick')
for day in range(365):
    if nick.alive==False:
      print('Student lose :(')
      break
      nick.life(day)
