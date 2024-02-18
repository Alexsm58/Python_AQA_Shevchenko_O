#завдання 1
class Dog:
    #calculate the cost of a dog using the static method
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def bark(self):
        return 'Woof!'

    @staticmethod
    def calculate_price(age):
        base_prise = 600
        price = base_prise * age * 0.5
        return int(price)

dog1 = Dog('Buddy', 30, 2)
print(dog1.bark())
print(f'The {dog1.name} cost: {Dog.calculate_price(2)}')

dog2 = Dog('Buldog', 35, 1)
print(f'The {dog2.name} cost: {Dog.calculate_price(4)}')


#завдання 2
class Company:
    #describe what the company does using class method
    def __init__(self, name, industry, locations):
        self.name = name
        self.industry = industry
        self.locations = locations

    def get_name(self):
        return self.name

    @classmethod
    def from_info_company(cls, name, industry):
        return cls(name, industry, None)

toyota = Company.from_info_company('Toyota', 'cars')
google = Company.from_info_company('Google', 'soft')
print(f'{toyota.get_name()} company makes {toyota.industry}')
print(f'{google.get_name()} company makes {google.industry}')
