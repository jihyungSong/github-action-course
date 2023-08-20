STATUS = ['normal', 'sleepy', 'hungry', 'angry']

class Cat(object):

    def __init__(self, name):
        self.name = name
        self.status = 'normal'

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_status(self):
        return self.status
    
    def set_status(self, status):
        if status not in STATUS:
            raise ValueError('Not allowed status')
        
        self.status = status

    def meow(self):
        return 'Meow~'
    