'''
Base model class  
'''
from json.encoder import JSONEncoder

class Personnel(object):
    
    def __init__(self, data_dict):    
        self.id = data_dict['id'] 
        self.fullName = data_dict['fullname']
        self.gender = data_dict['gender'] 
        self.dob = data_dict['dob']
        self.age = data_dict['age']
        self.aadhar = data_dict['aadhar']
        self.city = data_dict['city'] 
        self.contactNumber = data_dict['contact_number']
                 
class PersonnelEncoder(JSONEncoder):

        def default(self, o):
            return o.__dict__                        
