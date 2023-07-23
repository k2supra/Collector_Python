class Profession:
    name = ''
    category = ''
    salary = 0
    work_hours = ''

    def __init__(self):
        print(f"Created objects of Profession:")
        self.name = "Elon Mask"
        self.category = 'Every'
        self.salary = 999999999999999999
        self.work_hours = '25/8'


    def ShowOn(self):
        print(f"Name: {self.name} \nCategory: {self.category} \nSalary: {self.salary}$ \nWork_hours: {self.work_hours}")
    def __del__(self):
        print("Deleted objects of Profession")

if __name__ == '__main__':
    profession = Profession()
    profession.ShowOn()
    del profession