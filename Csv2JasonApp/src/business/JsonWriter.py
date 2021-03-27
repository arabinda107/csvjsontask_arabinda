'''
JsonWriter class is to convert the data to the JSON file
'''
import json
import os
import time

from src.models.StudentList import StudentList, StudentListEncoder
from src.models.TeacherList import TeacherList,TeacherListEncoder

class JsonWriter(object):

    '''
    Convert Student & Teacher list to JSON
    And Save the JSON to the specified file 
    '''
    def convert_list_2_json(self, data_list, category):
        if category=='student':
            record_count=len(data_list)
            student_list = StudentList(record_count,data_list)
            json_data = json.dumps(student_list,cls=StudentListEncoder,indent=4)
            return json_data
        else:
            record_count=len(data_list)
            teacher_list = TeacherList(record_count,data_list)
            json_data = json.dumps(teacher_list, indent=4, cls=TeacherListEncoder)
            return json_data



        
        

        
            
           
            
            
    