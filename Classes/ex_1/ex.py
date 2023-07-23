class Car:
    name = ''
    engine = ''
    wheel_drive = ''
    hp = 0
    h = 0
    w = 0
    type = ''

    def __init__(self):
        print(f"Created objects of car:")
        self.name = "Toyota Supra"
        self.engine = 'V6'
        self.wheel_drive = 'rear'
        self.hp = 725
        self.h = 1265
        self.w = 1490
        self.type = 'hatchback'

    def ShowOn(self):
        print(f"name: {self.name}, \nengine: {self.engine}, \nwheel drive: {self.wheel_drive}, \nHP: {self.hp}, \nHigh: {self.h}, \nweight: {self.w}, \ntype: {self.type}")
    def __del__(self):
        print("Deleted objects of car")

if __name__ == '__main__':
    car = Car()
    car.ShowOn()
    del car