class  Student:
    roll = ""
    gpa = ""

    def  setValue(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa


    def  display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

rahim = Student()
rahim.setValue(1001,3.3)
rahim.display()

karim = Student()
karim.setValue(333,4)
karim.display()