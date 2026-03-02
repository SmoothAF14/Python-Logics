class student:
    school = "ABD School"  # class variable

    @classmethod
    def get_school(cls):
        return cls.school
print(student.get_school())# calling the class method using the class name