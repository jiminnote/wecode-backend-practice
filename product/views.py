import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from product.models import (
    Product, 
    MainCategory, 
    Recommend
)

from .models import Product, MainCategory

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        main_category_id = request.GET.get('main_category_id')
        category_id      = request.GET.get('category_id')
        sort             = request.GET.get('sort')
        limit            = int(request.GET.get('limit', 20))
        offset           = int(request.GET.get('offset', 0))
        
        q = Q()
        
        if category_id:
            q &= Q(category__id = category_id)
            
        if main_category_id:
            q &= Q(category__main_sub_category__main_category_id = main_category_id)
        
        sort_set = {
            'random' : '?'
        }
        
        order_field = sort_set.get(sort, 'id')
        products    = Product.objects.filter(q).order_by(order_field)[offset:offset+limit]
        
        result = [
            {
                "products" : 
                    {
                        "product_id"     : product.id,
                        "product_name"   : product.name,
                        "category_id"    : product.category.id,
                        "category_name"  : product.category.name,
                        "product_detail" : [
                            {
                                "product_option_id" : product_option.id,
                                "size_mL"           : product_option.sizes_mL,
                                "price"             : product_option.price,
                                "image_url"         : product_option.image_url,
                            } for product_option in product.productoption_set.all()
                        ],
                        "product_feature" : [
                            {
                            "id"      : feature.feature.id,
                            "feature" : feature.feature.name,
                            "content" : feature.content
                            }for feature in product.Products_feature.filter(is_addtional=False)
                        ]
                    }
            } for product in products
        ]
        
        return JsonResponse({"message" : result}, status = 200)

class ProductdetailView(View):
    def get(self,request, product_id):
        try: 
            product          = Product.objects.get(id=product_id)
            product_options  = product.productoption_set.all()
            recommends       = Recommend.objects.filter(reference_product_id=product_id)
            product_features = product.Products_feature.all()
            product_options  = [
                {
                    'id'              : product_option.id,
                    'sizes_mL'        : product_option.sizes_mL,
                    'image_url'       : product_option.image_url,
                    'price'           : product_option.price,
                    'is_include_pump' : product_option.is_include_pump,
                    'content'         : product_option.content
                } for product_option in product_options 
            ]
            
            recommends = [
                {
                    'name'              : recommend.recommend_product.name,
                    'product_id'        : recommend.recommend_product.productoption_set.first().product_id ,   
                    'product_image_url' : recommend.recommend_product.productoption_set.first().image_url,
                    'product_content'   : recommend.recommend_product.Products_feature.first().content,
                    
                } for recommend in recommends 
            ]
            
            product_features = [
               { 
                    'feature': [
                        {   'id'      : feature.id,
                            'content' : feature.content,
                            'feature' : feature.feature.name
                    }for feature in product_features.filter(is_addtional=False)],
                    'manual' :[ 
                        {   'id'      : feature.id,
                            'content' : feature.content,
                            'feature' : feature.feature.name
                    }for feature in product_features.filter(is_addtional=True)]
                }
            ] 
                        
            products = {
                'id'                   : product.id,
                'name'                 : product.name,
                'content'              : product.content,
                'main_category'        : product.category.main_sub_category.main_category.name,       
                'category'             : product.category.name,
                'additional_name'      : product.additional_name,
                'additional_content'   : product.additional_content,
                'additional_image_url' : product.additional_image_url,
                'features'             : product_features,
                'product_option'       : product_options,  
                'recommend'            : recommends,
                } 
        
            
            return JsonResponse({'product' : products}, status = 200)
        
        except KeyError:
            return JsonResponse({"message" : 'KeyError'}, status = 400)  
        
        except Product.DoesNotExist:
            return JsonResponse({"message": 'Not Found Data'}, status = 404)
        
class CategoryView(View):
    def get(self, request):
        main_categories = MainCategory.objects.all()

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