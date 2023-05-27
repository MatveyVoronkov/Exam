import random

class Pet:
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
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out.....")
            self.alive = False

        elif self.gladness <= 0:
            print("Dog needs to see the vet")
            self.alive = False

        elif self.gladness >5:
            print("Good mood")
            self.alive = False

    def end_on_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress)}')

    def elive(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f'{day:=^50}')
        print('1 - to eat')
        print('2 - to slipp')
        print('3 - to chill')
        live_cube = (input('Enter your choise:'))
        if live_cube == 1:
            print('You entered 1 variant (eat)')
            self.to_eat()
        elif live_cube == 2:
            print('You entered 2 variant (slepp)')
            self.to_slepp()
        elif live_cube == 3:
            print('You entered 3 variant (chill)')
            self.to_chill()
        else:
            print('Not correct choise.You can enter only 1 or 2 or 3')
        self.end_on_day()
        self.is_alive()
dog = Pet(name ='Dog')
for day in range(365):
    if dog.alive==False:
      print('Dog lose :(')
      break
      dog.life(day)
