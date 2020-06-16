# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9417828#overview

# Rules:
# - staticmethods should not be used. If used you needt o be sure that that object will not be inherited
# - classmethod will be used when you do not want to use the self from the inherited class, and you prefer using you own internal self

class FixedFloat:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return (f'FixedFloat {self.value:.2f}') # this will limit the float to 2 decimals. Example 13.6543 will be displayed 12.65

     # if we keep this as static, the below code will print: FixedFloat 3.82
    # "money2 = Euro.from_sum (1.354, 2.46436)
    # print(money2)"
    #
    # because the money2.from_sum Object, is using the from_sum from FixedFloat and the self from Fixed Float will ge the sum value, and the print will be from FixFloat
    # to use the print from Euro we need to declare from_sum as classmethod
    # @staticmethod
    # def from_sum(value1, value2):
    #     return FixedFloat(value1+value2)

    @classmethod
    def from_sum(cls,value1, value2):
        return cls(value1+value2)

class Euro(FixedFloat):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = '£'

    def __repr__(self):
        return (f'Euro {self.value:.3f} {self.symbol}')

new_number = FixedFloat.from_sum(20.554, 0.745643)
print(new_number)

money1 = Euro(2.46436)
print(money1)

money2 = Euro.from_sum (1.354, 2.46436) # Euro class is passed as a first parameter. So the cls argument will get the Euro object as a parameter.
print(money2)