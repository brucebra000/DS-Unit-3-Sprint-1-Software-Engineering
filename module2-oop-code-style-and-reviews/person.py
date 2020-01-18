class Human(): #stores information about a person
    def __init__(self, name, gender, age, height, weight, haircol):
        self.name = name
        self.gender = gender
        self.age = age + "yrs"
        self.height = height + "in"
        self.weight = weight + "lb"
        self.haircol = haircol + " hair"

    @property
    def bio(self):
        '''
        Prints a person's full bio
        '''
        return f'{self.name}, {self.gender}, {self.age}, {self.height}, {self.weight}, {self.haircol}'

class Employee(Human): #stores information about an person (like 'Human' but with an occupation listed)
    def __init__(self, name, gender, age, height, weight, haircol, occupation):
        super().__init__(name, gender, age, height, weight, haircol)
        self.occupation = occupation

    @property
    def employee_bio(self):
        '''
        Prints a employee's full bio
        '''
        return f'{self.name}, {self.gender}, {self.age}, {self.height}, {self.weight}, {self.haircol}, {self.occupation}'


if __name__ == "__main__":
    garry = Human("Garry", "Male", "26", "5.8", "162", "brown")
    print(garry.gender)

    print()
    print(garry.bio)

    lilith = Employee("Lilith", "Female", "35", "5.4", "134", "Black", "Data Scientist")
    print()
    print(lilith.employee_bio)