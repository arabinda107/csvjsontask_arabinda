from json.encoder import JSONEncoder


class TeacherList(object):

    def __init__(self, teacherRecordCount, data):
        self.teacherRecordCount = teacherRecordCount
        self.data = data

        
class TeacherListEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__ 
