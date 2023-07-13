class Student:

    def __init__(self, grade, age):

        self.grade = grade
        self.age = age

    def __repr__(self):
        return f"Student is in {self.grade}, is {self.age} years old"

    def grade_calc(self, grade):
        if grade < 70:
            return "Fail:("
        else:
            return "Pass:)"

    def what_school(self, age):
        if age < 14:
            return "middle school"
        else:
            return "high school"

    class BloomTechStudent:

        def __init__(self, course):
            self.course = course

        def what_course(self, course):
            if course == "Data Science":
                return "nerd!"
            else:
                return "you're still a nerd"


if __name__ == '__main__':
    my_student = Student(90, 17)
    print(my_student.grade_calc(90))
    print(my_student.what_school(14))
    
