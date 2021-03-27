from json.encoder import JSONEncoder


class StudentList(object):

    def __init__(self,studentRecordCount,data):

        self.studentRecordCount=studentRecordCount
        self.data = data

        
class StudentListEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__        
