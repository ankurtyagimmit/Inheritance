class University:
    def getUdetails(self):
        self.uName=input("Enter university Name:")
        self.uRID=input("Enter reg. (University) No.:")

    def showUdetails(self):
        print("University Name",self.uName)
        print("University Reg.No.:",self.uRID)


class Collage(University):
    def getClgDetails(self):
        self.cName=input("Enter Collage Name:")
        self.cRID=input("Enter Reg.(Collage)No.:")
        self.getUdetails()

    def showClgDetails(self):
        print("Collage Name",self.cName)
        print("Collage reg.No.",self.cRID)
        self.showUdetails()


class Student(Collage):
    def getStudentDetails(self):
        self.sName=input("Enter Student Name:")
        self.sRoll=input("Enter Student's Enroll No.:")
        self.sBranch=input("Enter Student Branch:")

        self.getClgDetails()

    def showStudentDetails(self):
        print('*********\nStudent Details********')
        print("Student Details",self.sName)
        print("Student Name",self.sName)
        print("Student Enroll No.",self.sRoll)
        print("Student Branch",self.sBranch)

        self.showClgDetails()

s=Student()
s.getStudentDetails()
s.showStudentDetails()
        
