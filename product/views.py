from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from .models import Product, Category

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        try:
            #:8000/products?main_category_id=1&limt=10&offset=2&sort=random
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
            
            order_filed = sort_set.get(sort, 'id')
            
            products = Product.objects.filter(q).order_by(order_filed)[offset:offset+limit]

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
        