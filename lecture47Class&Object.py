#  Class = Template

class  Student:
    roll = ""
    gpa = ""

rahim = Student()
#  here  rahim  is   a  object  of  Student Class
print(isinstance(rahim,Student))
rahim.roll = 101
rahim.gpa = 3.44

print(f"Roll : {rahim.roll}, GPA : {rahim.gpa}")

karim = Student()
#  here  kahim  is   a  object  of  Student Class
print(isinstance(rahim,Student))
karim.roll = 103
karim.gpa = 3.00

print(f"Roll : {karim.roll}, GPA : {karim.gpa}")

