class Phone:
    name = ''
    memory = ''
    ram = 0
    d = ''
    type = ''
    iphone = ''

    def __init__(self):
        print(f"Created objects of phone:")
        self.name = "Optimus Primigga"
        self.memory = '128GB'
        self.ram = 68
        self.d = '156'
        self.type = 'gaming'
        self.iphone = "!!!!NOT    N O T    NEVER!!!!"


    def ShowOn(self):
        print(f"name: {self.name} \nmemory: {self.memory} \ndiagonal: {self.d} \ntype: {self.type} \nRAM: {self.ram} \nIphone?: {self.iphone}")
    def __del__(self):
        print("Deleted objects of phone")

if __name__ == '__main__':
    phone = Phone()
    phone.ShowOn()
    del phone