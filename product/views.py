
import json

from django.http      import JsonResponse
from django.views     import View

from product.models import Product, Productoption, Recommend, Productfeature

## query paramete     request.GET['param']   reqeust.GET.get()
## path  params        
class ProductdetailView(View):
    def get(self,request, product_id):
        try: 
            products         = Product.objects.get(id=product_id)
            product_options  = Productoption.objects.filter(product_id=product_id)
            recommends       = Recommend.objects.filter(reference_product_id=product_id)
            product_features = Productfeature.objects.filter(product_id=product_id)
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
                'id'                   : products.id,
                'name'                 : products.name,
                'content'              : products.content,
                'main_category'        : products.category.main_sub_category.main_category.name,       
                'category'             : products.category.name,
                'additional_name'      : products.additional_name,
                'additional_content'   : products.additional_content,
                'additional_image_url' : products.additional_image_url,
                'features'             : product_features,
                'product_option'       : product_options,  
                'recommend'            : recommends,
                } 
        
            
            return JsonResponse({'product' : products}, status = 200)
        
        except KeyError:
            return JsonResponse({"message" : 'KeyError'}, status = 400)  
        
        except Product.DoesNotExist:
            return JsonResponse({"message": 'Not Found Data'}, status = 400)
        

