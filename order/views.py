import json

from django.http   import JsonResponse
from django.views  import View

from core.utils     import login_decorator
from users.models   import User
from order.models   import Cart
from product.models import Productoption

class CartView(View):
    @login_decorator
    def post(self, request):
        try:
            data           = json.loads(request.body)
            user           = request.user
            product_option = Productoption.objects.get(id=data['product_option_id'])
    
            cart, created = Cart.objects.get_or_create(
                    user            = user,
                    product_option  = product_option,
                    defaults={"quantity": 1}
                    )
            if not created:
                cart.quantity += 1
                cart.save()
            
            return JsonResponse({'message' : 'SUCCESS'}, status= 201)
        except Productoption.DoesNotExist:
            return JsonResponse({'message' : 'DOES_NOT_EXIST'}, status= 404)

    @login_decorator
    def get(self, request):
        carts = Cart.objects.filter(user_id=request.user.id)
        
        result=[
           {
             "name"              : cart.product_option.product.name,
             "price"             : cart.product_option.price,
             "product_option_id" : cart.product_option.id,
             "size_mL"           : cart.product_option.sizes_mL,
             "quantity"          : cart.quantity,
             "cart_id"           : cart.id
            }
        for cart in carts
        ]

        return JsonResponse({'result': result}, status=200)
    
    @login_decorator
    def delete(self, request):
        user    = request.user
        cart_id = request.GET.get('cart_id')
        
        if not Cart.objects.filter(id=cart_id, user=user).exists(): 
            return JsonResponse({'message':'DOES_NOT_EXIST'}, status = 400)

        cart = Cart.objects.filter(id=cart_id,user=user)
        cart.delete()
        
        return JsonResponse({"message":"CART_DELETE"}, status = 204)

    @login_decorator
    def patch(self, request):
        try:
            data    = json.loads(request.body)
            user    = request.user
            cart_id = data['cart_id']
            
            if not Cart.objects.filter(id=cart_id, user=user).exists():
                return JsonResponse({"message":"INVALID_CART_ID"}, status=404)
            
            cart = Cart.objects.get(id=cart_id, user=user)
            
            cart.quantity = data['quantity']
            cart.save()
            
            return JsonResponse({"message": "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

