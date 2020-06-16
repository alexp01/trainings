student2 = {
            "Name" : "Smith",
            "Grades" : [7, 4, 8, 5, 8]
        }

class Student():
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

Student_one = Student('Smith', [30, 60, 90])

print (Student_one.name)
print (Student_one.grades)

print (Student_one.average())

Student_two = Student('Smith', [30, 60, 90])
print (Student_two.name)

# OR print(student.average(Student_one))
#     How to give a parameter also to he method, besides the default one : self
#     def average(self, friend):
# print (Student_one.average("Giuseppe"))

