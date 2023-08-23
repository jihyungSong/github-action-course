
class Human(object):
    def __init__(self, name):
        self.name = name
        self.age = 20

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def get_info(self):
        return f'My name is {self.name} and {self.age} years old.'
