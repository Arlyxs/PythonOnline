class Computer:
    # class or static variable
    type = 'laptop'

    def __init__(self, cpu, ram, storage):
        #  instance variable
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

# method
    def config(self):
        print('Config is: ', self.cpu, self.ram, self.storage, self.type)


com1 = Computer('i5', 16, 1)
com2 = Computer('Ryzen 3', 32, 2)
# change the static or class variable value
Computer.type = 'PC'
'''
Computer.config(com1)
Computer.config(com2)
# or call using the object directly
'''
com1.config()
com2.config()
