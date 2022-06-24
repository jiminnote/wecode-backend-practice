import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Max

from product.models import Product, Productoption, Recommend, Productfeature, Feature

## query paramete     request.GET['param']   reqeust.GET.get()
## path  params        
class ProductdetailView(View):
    def get(self,request, product_id):
        try: 
            product         = Product.objects.get(id=product_id)
            product_option  = Productoption.objects.filter(product_id=product_id)
            recommends      = Recommend.objects.filter(reference_product_id=product_id)
            product_feature = Productfeature.objects.filter(product_id=product_id)
            product_option  = [
                {
                    'sizes_mL'        : product_options.sizes_mL,
                    'image_url'       : product_options.image_url,
                    'price'           : product_options.price,
                    'is_include_pump' : product_options.is_include_pump,
                    'content'         : product_options.content
                } for product_options in product_option 
            ]
            
            recommend = [
                {
                    'name'              : recommend.recommend_product.name,
                    'product_id'        : recommend.recommend_product.productoption_set.first().product_id ,   
                    'product_image_url' : recommend.recommend_product.productoption_set.first().image_url,
                    'product_content'   : recommend.recommend_product.Products_feature.first().content,
                    
                } for recommend in recommends 
            ]
            
            product_features = [
                {
                    'content' : feature.content,
                    'feature' : feature.feature.name
                }
                for feature in product_feature
            ] 
                        
            products = {
                'id'                   : product.id,
                'name'                 : product.name,
                'content'              : product.content,
                # 'main_category'        : product.category.main_sub_category.main_category_set.name,       
                'category'             : product.category.name,
                'additional_name'      : product.additional_name,
                'additional_content'   : product.additional_content,
                'additional_image_url' : product.additional_image_url,
                'features'             : product_features,
                'product_option'       : product_option,  
                'recommend'            : recommend,
                } 
        
            
            return JsonResponse({'product' : products}, status = 200)
        
        except KeyError:
            return JsonResponse({"message" : 'KeyError'}, status = 400)  
        
        except Product.DoesNotExist:
            return JsonResponse({"message": 'Not Found Data'}, status = 400)
        
