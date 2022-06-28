import json

from django.http   import JsonResponse
from django.views  import View

from core.utils     import login_decorator
from users.models   import User
from order.models   import Cart
from product.models import Product, Productoption
class CartView(View):
    @login_decorator
    def post(self, request):
        try:
            data              = json.loads(request.body)
            user_id           = request.user.id
            product_option_id = Productoption.objects.get(id=data['product_option_id']).id
            quantity          = data['quantity']
        
            if Cart.objects.filter(user=user_id, product_option=product_option_id).exists():
                return JsonResponse({'MESSAGE' : 'PRODUCT_ALREADY_EXIST'}, status=400)
                
            Cart.objects.create(
                user_id            = user_id,
                product_option_id  = product_option_id,
                quantity           = quantity
            )

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status= 201)

        except KeyError: 
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status= 400)

        except Productoption.DoesNotExist: 
            return JsonResponse({'MESSAGE' : 'DOES_NOT_EXIST'}, status = 401)

    @login_decorator
    def get(self, request):
        carts = Cart.objects.filter(user_id=request.user)
        
        result=[
           {
             "name"       : cart.product_option.product.name,
             "price"      : cart.product_option.price,
             "product_id" : cart.product_option.product.id,
             "quantity"   : cart.quantity,
             "cart_id"    : cart.id
            }
        for cart in carts
        ]

        return JsonResponse({'result': result}, status=200)
    
       
    @login_decorator
    def delete(self, request):
        user = request.user
        cart_id = request.GET.get('cart_id')
        
        if not Cart.objects.filter(user=request.user).exists(): 
            return JsonResponse({'MESSAGE':'DOES_NOT_EXIST'}, status = 400)

        cart = Cart.objects.filter(id=cart_id,user=user)
        
        cart.delete()
        return JsonResponse({"message":"CART_DELETE"})

    @login_decorator
    def patch(self, request):
        try:
            data          = json.loads(request.body)
            user          = request.user
            cart_id       = Cart.objects.get(id=data['cart_id']).id
            
            if not Cart.objects.filter(id=cart_id, user=user).exists():
                return JsonResponse({"message":"INVALID_CART_ID"}, status=400)
            
            cart = Cart.objects.get(id=cart_id, user=user)
            
            cart.quantity = data['quantity']
            cart.save()
            
            return JsonResponse({"quantity":cart.quantity}, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

