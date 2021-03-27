'''
CsvParser class to read the data from the CSV file
'''
import csv
import sys
from src.models.Student import Student
from src.models.Teacher import Teacher
from unicodedata import category
from src.util.CommonUtil import CommonUtil
from src.business.Validator import Validator


class CSVParser:

    student_list = []
    teacher_list = []
    
    '''
    Main method to read csv row wise and create list of objects
    '''
    def csv_to_dict(self, csv_file, data_date_format):
        with open(csv_file, newline='') as csvFile:
            csv_reader = csv.DictReader(csvFile)
            csv_reader.fieldnames
            print(csv_reader.fieldnames)
            
            validaor_obj = Validator()
            if validaor_obj.required_keys_exist( csv_reader.fieldnames) == False:
                sys.exit()
            # next(csvReader, None)  # Skip the header
            # Unpack the row directly in the head of the for loop..
           
            row_count = 1;
            for row in csv_reader:
                '''
                    Validate a single CSV row
                '''
                if validaor_obj.validate_csv_row( row, data_date_format, row_count) == False:
                    sys.exit()
                
                #category = row['category'].lower()
                #fullname=row['firstname']+" "+row['lastname']
                #exact_age=CommonUtil.cal_age_month(self, row['dob'])
                category = row['category'].lower()
                if (category == 'student'): 
                    student = self.__creare_student_data(row)
                    self.student_list.append(student)
                elif category == 'teacher':
                    teacher = self.__create_teacher_data(row)
                    self.teacher_list.append(teacher)
                row_count +=1 

                
            
    
    '''
    Create student object from CSV row
    '''
    def __creare_student_data(self, row):
                
        personnel_data =  self.__set_personnel_data(row)        
        total_marks = None
        grade = None
        sec_percent = None
        if len(row['total_marks']) > 0 :
            total_marks = int(row['total_marks'])
            grade =  CommonUtil.calculate_grade(self,total_marks)
                
        if len(row['sec_percent']) > 0 :
            sec_percent = int(row['sec_percent'])
                
        student = Student( row['roll_no'], row['class'], total_marks, grade, sec_percent, 
                           row['hs_stream'].title(), personnel_data)

        return student
        
    def __create_teacher_data(self, row):

        personnel_data=self.__set_personnel_data(row)
        servicePeriod=CommonUtil.calculate_period_by_date(self,row['doj'])
        sal=CommonUtil.salCal(self,row['salary'])
        teacher=Teacher( row['emp_no'],row['class_teacher_of'],row['doj'],servicePeriod,row['previous_school'],row['post'],sal,row['subject_teaches'],personnel_data)
        return teacher

        
    '''
    Set Common Personnel Attributed
    '''
    def __set_personnel_data(self, row):
        
        personnel_data = {}
        personnel_data['id'] = int(row['id']) 
        personnel_data['fullname'] = "{0} {1}".format( row['firstname'].title(), row['lastname'].title() )
        
        gender = row['gender'].lower()
        if gender == 'm':
            personnel_data['gender'] = 'Male'
        else:
            personnel_data['gender'] = 'Female'
            
        personnel_data['dob'] = row['dob']
        personnel_data['age'] = CommonUtil.calculate_period_by_date(self, row['dob'])       
        personnel_data['aadhar'] = row['aadhar_number']
        personnel_data['city'] = row['city'].title()
        personnel_data['contact_number'] = row['contact_number']
        
        return personnel_data        
