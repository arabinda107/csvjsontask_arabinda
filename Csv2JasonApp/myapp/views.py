from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from jproperties import Properties
import os.path
from os import path
import csv
import json
import sys
import src.business
from src.util import CommonUtil
from src.business.CSVParser import CSVParser
from src.business.JsonWriter import JsonWriter
from src.models.Student import Student
from src.models.Teacher import Teacher
from .forms import SearchForm
from django.views.decorators.cache import never_cache
from src.business.SearchFuntionlity import SerchFuntionlity

def home(request):
    # Taking JSON store path input
    json_save_path = "/home/arabinda/guna"

    # Read the config file
    configs = Properties()
    with open('app.properties', 'rb') as config_file:
        configs.load(config_file)

    #csv_master_file = {configs.get("CSV_MASTER_FILE").data}
    # 'D:\\Data\\csv\\input.csv' #
    csv_master_file = str(configs["CSV_MASTER_FILE"].data)
    data_date_format = str(configs['DATA_DATE_FORMAT'].data)

    if not path.exists(csv_master_file):
        print ("Master file could not be found!!!")
        sys.exit()
    csv_parser_obj = CSVParser() 
    csv_parser_obj.csv_to_dict(csv_master_file, data_date_format)
    student_list = csv_parser_obj.student_list
    teacher_list=csv_parser_obj.teacher_list
   
    if request.method=='GET':

        fm = SearchForm(request.GET)
        if fm.is_valid():
            search_name = (fm.cleaned_data['name']).lower()
            search_category=(fm.cleaned_data['category']).lower()
            search_age=fm.cleaned_data['age']
            
            #Searching from both student and teacher list
            if search_category=="student":
                actual_list=SerchFuntionlity.serching(search_category,search_age,search_name,student_list)
            elif search_category=="teacher":
                actual_list=SerchFuntionlity.serching(search_category,search_age,search_name,teacher_list)
            json_writer = JsonWriter()
            final_json=json_writer.convert_list_2_json(actual_list,search_category)
            
            #Error json 
            try:
                if actual_list=='error':
                    error_list={'data':402,'message':"Bad Request"}
                    final_json=json.dumps(error_list,indent=4)
            except ValueError:
                pass
            return HttpResponse(final_json,content_type='application/json')
    else:
        fm=SearchForm()

    return render(request,"home.html",{'form':fm})


