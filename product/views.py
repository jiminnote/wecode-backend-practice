from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from .models import Product, Category

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        try:
            main_category_id = request.GET.get('main_category')
            category_id      = request.GET.get('category_id')
            limit            = int(request.GET.get('limit', 20))
            offset           = int(request.GET.get('offset', 0))

            q = Q()

            if category_id:
                q &= Q(category__id = category_id)
                
            if main_category_id:
                q &= Q(main_category__id = main_category_id)
            
            products = Product.objects.filter(q)[offset:offset+limit]

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
                } for product in products]
            
            return JsonResponse({"message" : result}, status = 200)
        
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)
        
        except Category.DoesNotExist:
            return JsonResponse({"message" : "NO_CATEGORY_FOUND"}, status = 400)
        
        
        
        
        

        
