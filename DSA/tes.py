class Student:
    def __init__(self,name):
        self.name = name
        self.subjects = []

    def add_subjects(self,subject):
        self.subjects.append(subject)

    def print_details(self):
        print("name:- ",self.name)
        print("subbjects;- ")
        for sub in self.subjects:
            print("\t",sub)     


newstudent = Student("amal")
newstudent.add_subjects("maths")
newstudent.add_subjects("science")
newstudent.print_details()
newstudent = Student("kamal")
newstudent.add_subjects("maths")
newstudent.add_subjects("science")
newstudent.print_details()