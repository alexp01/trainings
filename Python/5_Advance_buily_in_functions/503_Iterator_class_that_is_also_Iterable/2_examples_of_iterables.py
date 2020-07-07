class Generate100numbers:
    def __init__(self):
        self.number = 1

    def __next__(self):
        if self.number <= 100:
            number = self.number
            self.number += 1
            return number
        else:
            raise StopIteration()

    def __iter__(self):
        return self

nr = Generate100numbers()

print (sum(nr))

# The bellow class is also an iterable even if it doesn ot have de __iter__dunder method

class Cars:
    def __init__(self):
        self.name = ['fiesta', 'focus']

    def __len__(self):
        return len(self.name)

    def __getitem__(self, item):
        return self.name[item]

for x in Cars():
    print(x)