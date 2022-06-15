class  Donkey():
    def __init__(self, name, cargo, years):
        self.cargo = cargo
        self.years = years
        self.name = name

    def info (self):
        print('Donkey-boy', self.name, ',', self.cargo)

    def cry(self):
        return 'Eeyore' * self.years
    def work_hard(self, amount):
        if amount > 5:
            a = amount//5
            self.years = self.years - a
        else:
            self.years = self.years + 2
    def carry(self, load):
         if load <= self.cargo:
             print('True')
         else:
             print('False')


d = Donkey('Pinoccio', 10, 5)
d.info()
print(d.cry())
d.work_hard(16)
print(d.cry())
print(d.carry(10))







