import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wesop.settings")
django.setup()

from product.models import *  
from users.models import *

CSV_PATH_PRODUCTS='wesop_data/시트 5-Features.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None) 
        for row in data_reader:
            if row[1]:
                names = row[1]
                Feature.objects.create(name = names)
            # if row[2]:
            #     sub_menu_name = row[2]
            #     menu = MainCategory.objects.get(id=menu_id)
            #     Subcategory.objects.create(name = sub_menu_name,main_category= menu)