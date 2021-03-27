'''
Common Utility class 
'''
from dateutil import relativedelta
from datetime import date, datetime

class CommonUtil:
    
    def calculate_grade(self, total_marks):
        grade = None
        # grade Calculation
        if total_marks >= 800 :
            grade = "A"            
        elif total_marks >= 700 :
            grade = "B"                
        elif total_marks >= 600 :
            grade = "C"            
        elif total_marks >= 500 :
            grade = "D"
        
        return  grade
    
    def calculate_period_by_date(self, target_date):
        target_date = datetime.strptime(target_date, '%m/%d/%Y')
        today = date.today()
        datetime_today = date(today.year, today.month, today.day)
        time_difference = relativedelta.relativedelta(datetime_today, target_date)
        return "{0} Yrs {1} Months".format(str(time_difference.years) ,str(time_difference.months))
    def salCal(self,sal):
        actual_sal="{:,}".format(int(sal))
        return actual_sal
    def age_calc_month(person_age):
        numbers=[]
        for data in person_age.split():
            if data.isdigit():
                numbers.append(int(data))
        age=numbers[0]*12+numbers[1]
                
        return age

        
    
