'''
Student  model class  
'''
from json.encoder import JSONEncoder
from src.models.Personnel import Personnel

class Student(Personnel):
    
    def __init__(self, rollNumber, className, totalMarks, grade, secPercent, hsStream, personel_dict):
        
        self.rollNumber = rollNumber
        self.className =  className
        self.totalMarks = totalMarks
        self.grade = grade
        self.secPercent = secPercent
        self.hsStream = hsStream
        
        Personnel.__init__(self, personel_dict )
    def display(self):
        print(self.rollNumber)
    
    class StudentEncoder(JSONEncoder):

        def default(self, o):
            return o.__dict__     