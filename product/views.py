import json

from django.http  import JsonResponse
from django.views import View

from product.models import MainCategory

class CategoryView(View):
    def get(self, request):
        main_categories     = MainCategory.objects.all()

        results = [
            {   
                'main_category_id' : main_category.id,
                'main_category'    : main_category.name,
                'sub_category'     : [
                    {
                        'id'       : main_sub_category.sub_category.id,
                        'name'     : main_sub_category.sub_category.name,
                        'category' :[
                            {   
                                'id'  : category.id,
                                'name': category.name
                                    }for category in main_sub_category.category_set.all()
                            ]
                    } for main_sub_category in main_category.mainsubcategory_set.all()
                ]
                }for main_category in main_categories
            ]

        return JsonResponse({'results' : results}, status = 200)
    
