class Car():
    doors = 4
    wheels = 4

    def detail(self, name):
        return f'The name of the car is {name} it has {self.wheels} and {self.doors} Doors'



c1 = Car()
print(c1.doors)
print(c1.wheels)
print(c1.detail('Benz'))
c2 = Car()
print(c2.doors)
print(c2.wheels)
print(c2.detail('Lexus'))
