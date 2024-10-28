# In this child class inherit from multiple parent class.
# The order in which child class inherits is also important. As MRO follows that order.

class Student:
    def __init__(self,id ,name):
        self.roll_no = id
        self.name = name
    def showName(self):
        print(self.name)

class Singer:
    def __init__(self,name):
        self.name = name
    def FavSong(self):
        print("Perfect by Edsheeran")

class SingerStudent(Student,Singer):
    def FavSinger(self):
        print("Ed Sheeran")

stud1 = SingerStudent(1 , "Ganesh")
stud1.showName()
stud1.FavSong()
stud1.FavSinger()