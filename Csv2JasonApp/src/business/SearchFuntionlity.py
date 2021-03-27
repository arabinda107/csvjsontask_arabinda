
from src.util.CommonUtil import CommonUtil
from django.http import HttpResponse,HttpResponseRedirect
import json
class SerchFuntionlity():
    def serching(search_category,search_age,search_name,actual_list):
        print("I am inside searching function")
        search_list=[]

        if search_age=='':
            search_age=500
        elif not search_age.isdigit():
            data='error'
            return data

        if search_category=='student':
            x=[data for data in actual_list if ((search_name in (data.fullName).lower()) & (CommonUtil.age_calc_month(data.age)<=(int(search_age) *12)))]
            search_list.extend(x)
            
            return search_list
        elif search_category=='teacher':
            x=[data for data in actual_list if ((search_name in (data.fullName).lower()) & (CommonUtil.age_calc_month(data.age)<=(int(search_age) *12)))]
            search_list.extend(x)
            
            return search_list
        
            