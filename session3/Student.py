
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, course, grade):
        if grade < 0 or grade > 20:
            print("Invalid grade")
        else:
            self.grades[course] = grade

    def average(self):
        if len(self.grades) == 0:
            return 0

        total = 0
        for grade in self.grades.values():
            total = total + grade

        return total / len(self.grades)

    def best_course(self):
        if len(self.grades) == 0:
            return "No grades"

        best_grade = -1
        best = ""

        for course, grade in self.grades.items():
            if grade > best_grade:
                best_grade = grade
                best = course

        return best

    def failed_courses(self):
        failed = []

        for course, grade in self.grades.items():
            if grade < 10:
                failed.append(course)

        return failed

    def status(self):
        avg = self.average()

        if avg >= 17:
            return "Excellent"
        elif avg >= 14:
            return "Good"
        elif avg >= 12:
            return "Normal"
        else:
            return "Probation"

    def report(self):
        print("Student:", self.name, "(ID:", self.student_id, ")")
        print()

        for course, grade in self.grades.items():
            print(course + ":", grade)
            print()

        print("Average:", self.average())
        print("Best course:", self.best_course())
        print("Failed courses:", self.failed_courses())
        print("Status:", self.status())


student1 = Student("طاها", "40312345")
student2 = Student("امیر", "40312346")

student1.add_grade("Math", 18)
student1.add_grade("Physics", 9)
student1.add_grade("Programming", 20)
student1.add_grade("English", 15)

student2.add_grade("Math", 12)
student2.add_grade("Physics", 16)
student2.add_grade("Programming", 14)
student2.add_grade("English", 18)

print("Student 1")
student1.report()

print()
print("Student 2")
student2.report()

print()
student1.add_grade("Chemistry", 25)
