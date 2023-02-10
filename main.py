import random


class Student:


    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 100
        self.satiety = 10






    def to_study(self):
        print("Time to study!")
        self.progress += 0.15
        self.gladness -= 3
        self.satiety -= 2


    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.satiety -= 1


    def to_chill(self):
        print("Reset time")
        self.gladness += 5
        self.gladness -= 0.2
        self.satiety -= 1


    def to_eat(self):
        print("I am eating")
        self.satiety += 3
        self.money -= 15

    def job(self):
        print("ran out of money")
        self.money += 100
        self.gladness -= 1
        self.satiety -= 2



    def is_alive(self):
        if self.progress <- 0.5:
            print("Cast aut....")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression..")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally....")
            self.alive = False
        elif self.money <= 0:
            print("ran out of money")
            self.gladness += -5
            self.progress -= 0.2
            self.money += 100
        elif self.satiety <= 0:
            self.satiety += 3




    def end_of_day(self):
        print(f"Progress = {self.progress}")
        print(f"Gladness = {self.gladness}")
        print(f"Money = {self.money}")
        print(f"Satiety = {self.satiety}")


    def live(self, day):
        day = "Day " + str(day) + " Of " + self.name + " Life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_eat()
        elif live_cube == 4:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


nick = Student(name="nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
