from datetime import date, datetime

class Validator(object):
      
    def required_keys_exist(self, fieldnames):
        csv_headers = ['id', 'category', 'firstname', 'lastname', 'gender', 'dob', 'previous_school', 
                       'doj', 'class', 'post', 'salary', 'class_teacher_of', 'roll_no', 'emp_no', 
                       'total_marks', 'city', 'aadhar_number', 'contact_number', 'blood_group', 
                       'subject_teaches', 'hs_stream', 'sec_percent']
        
        if set(fieldnames)  != set(csv_headers):
            print(" Required CSV header could not match, Aborting!!!")
            return False;
        return True;
    
    def validate_csv_row(self, row, date_format, row_count):
        '''
        Validate DOB & DOJ
        '''
        dob = row['dob']
        doj = row['doj']
       
        if not self.__valid_date( dob,date_format): 
            print("Incorrect date format for dob , It should be m/d/yyyy, value is:" + 
                  str(row['dob']) + " For row: "  + str(row_count) )
            return False;
        if doj is not None and len(doj) > 0:
            if not self.__valid_date(dob,date_format): 
                print("Incorrect date format for doj , It should be m/d/yyyy, value is: " + str(row['doj'])
                  + " For row: "  + str(row_count) )
                return False;
        
        return True
        '''
            Validate roll_number
            Rule: Must be Numeric type
        '''
       
        '''
            Validate total_marks
            Must be Numeric and <=1000
        '''
        
    def __valid_date(self, date_str, date_format):
        try:
            #datetime.strptime(date_str, date_format)
            datetime.strptime(date_str, '%m/%d/%Y')
            return True;
        except ValueError:
            return False