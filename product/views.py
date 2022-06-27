from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from .models import Product
class ProductListView(View):
    def get(self, request):
        main_category = request.GET.get('main_category')
        category      = request.GET.get('category')
        sort          = request.GET.get('sort', 'id')
        limit         = int(request.GET.get('limit', 36))
        offset        = int(request.GET.get('offset', 0))

        q = Q()
            
        if main_category:
            q &= Q(sub_category__main_category_id=main_category)

        if category:
            q &= Q(category_id=category)

        sort_type = {
            'id'   : 'id',
            'rand'  : '?'
        }

        products = Product.objects.select_related('category').filter(q).order_by(sort_type[sort])[offset:offset+limit]

        product_list = [{
            'id'        : product.id,
            'name'      : product.name,
            
        } for product in products]

        return JsonResponse({'products_list':product_list}, status=200)
