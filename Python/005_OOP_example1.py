class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    def average(self):
        return sum(self.grades) / len(self.grades)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekSalary (self):
        return self.salary * 35

student1 = WorkingStudent('Smith', 'MIT', 10.45)

print (student1.name)
student1.grades.append(57)
student1.grades.append(100)
print (student1.average())

# adding @properly makes that method to became a property as it only calculated something, and does not do complex things
print (student1.weekSalary)


