class Car:

    def __init__(self):
        self.brand_name = 'Audi '
        self.model = 'r8'
        self.__engine_name = '5.2 L V10'

    def __engine(self):
        return '5.2 L V10'

    def get_description(self):
        return self.brand_name + self.model + " is the car"


c = Car()
print(c.get_description())
print("Accessing Private Method: ", c._Car__engine())
print("Accessing Private variable: ", c._Car__engine_name)

'''
Audi r8 is the car
Accessing Private Method:  5.2 L V10
Accessing Private variable:  5.2 L V10
'''