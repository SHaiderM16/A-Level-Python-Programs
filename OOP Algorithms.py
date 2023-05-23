# Object Oriented Programming (OOP) Algorithms

# Defining a Class
class Picture():
    # PRIVATE Description: STRING
    # PRIVATE Width: INTEGER
    # PRIVATE Height: INTEGER
    # PRIVATE FrameColour: STRING

    def __init__(self, Desc, W, H, FC):
        self.__Description = Desc
        self.__Width = int(W)
        self.__Height = int(H)
        self.__FraameColour = FC

    def GetDescription(self):
        return self.__Description

    def GetWidth(self):
        return self.__Width

    def GetHeight(self):
        return self.__Height

    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, NewDesc):
        self.__Description = NewDesc


ArtistDesc = input("Enter picture's description:")
ArtistWidth = input("Enter picture's width:")
ArtistHeight = input("Enter picture's height:")
ArtistColour = input("Enter picture's colour:")

# Creating objects
Img1 = Picture(ArtistDesc, ArtistWidth, ArtistHeight, ArtistColour)

temp1 = Img1.GetDescription()
print(temp1)

# Inheritance

class Employee():
    # DECLARE Name: STRING
    # DECLARE Age: INTEGER

    def __init__(self, NameP, AgeP):
        self.__Name = NameP
        self.__Age = AgeP

    def GetName(self):
        return self.__Name

class PartTime(Employee):
    # DECLARE HourlyRate: INTEGER

    def __init__(self, NameP, AgeP, HourlyRateP):
        super().__init__(NameP, AgeP)
        self.HourlyRate = HourlyRateP

    def DailyWage(self, HoursWorked):
        Answer = HoursWorked * self.__HourlyRate
        return Answer

class FullTime(Employee):
    # DECLARE MonthlyRate: INTEGER

    def __init__(self, NameP, AgeP, MonthlyRateP):
        super().__init__(NameP, AgeP)
        self.__MonthlyRate = MonthlyRateP

    def YearlySalary(self):
        Answer = 12 * self.__MonthlyRate
        return Answer

Worker = PartTime("Bhatti", 50, 20)
PermWorker = FullTime("Majid", 60, 3000)

print(PermWorker.GetName())
print(PermWorker.YearlySalary())
