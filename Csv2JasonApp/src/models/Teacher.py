'''
Student  model class  
'''
from json.encoder import JSONEncoder
from src.models.Personnel import Personnel

class Teacher(Personnel):
    def __init__(self,empNo,classTeacher,doj,servicePeriod,previousSchool,post,salary,subjectTeaches,personel_dict):

        self.empNo=empNo
        self.classTeacher=classTeacher
        self.doj=doj
        self.servicePeriod=servicePeriod
        self.previousSchool=previousSchool
        self.post=post
        self.salary=salary
        self.subjectTeaches=subjectTeaches
        Personnel.__init__(self,personel_dict)

    class TeacherEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__   




        