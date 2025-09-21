import json

import bcrypt
import jwt
from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError 

from core.utils     import login_decorator
from core.validator import validate_email,validate_name,validate_password
from wesop.settings import SECRET_KEY,ALGORITHM
from users.models   import User

class SignupView(View): 
    def post(self,request):
        try:
            data         = json.loads(request.body)   
            email        = data['email'] 
            first_name   = data['first_name'] 
            last_name    = data['last_name']
            password     = data['password']
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({"message":"DUPLICATE_EMAIL"}, status = 400)
            
            validate_email(email)
            validate_name(first_name)
            validate_name(last_name)
            validate_password(password)
            
            User.objects.create(
                first_name   = first_name,
                last_name    = last_name,
                email        = email,
                password     = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            )
            return JsonResponse({"message":"SUCCESS"}, status = 201)
        
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status = 400)
        except ValidationError as e :
            return JsonResponse({'message' : e.message }, status = 400)    
class SigninView(View):
    def post(self,request):
        try: 
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']
            
            if not User.objects.filter(email = email).exists():
                return JsonResponse({"message":"INVALID_USER"}, status = 401)
            
            user = User.objects.get(email = email)
            
            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message": "INVALID_USER"}, status = 401)
            
            token  = jwt.encode({'user_id' : user.id}, SECRET_KEY, ALGORITHM)
            
            return JsonResponse({  "full_name" : user.last_name+user.first_name,
                                   "access_token":token},status=200)
        
        except KeyError: 
            return JsonResponse({"message":"KEY_ERROR"},status=400)

class UserView(View):
    @login_decorator
    def get(self,request):
        user = request.user
        
        user_information = {
            "id"         : user.id,
            "last_name"  : user.last_name,
            "first_name" : user.first_name,
            "full_name"  : user.last_name+user.first_name,
            "email"      : user.email,
            "password"   : user.password,
            }
            
        return JsonResponse({'user_information' : user_information}, status = 200)
    
    @login_decorator
    def patch(self,request):
        try:
            user = request.user
            data = json.loads(request.body) 
            
            first_name = data.get('first_name') if data.get('first_name') else user.first_name
            last_name  = data.get('last_name') if data.get('last_name') else user.last_name
            password   = data.get('password') 

            validate_name(first_name) 
            validate_name(last_name)
            
            user.first_name = first_name
            user.last_name  = last_name
            full_name       = user.last_name + user.first_name
            
            if password:
                validate_password(password)
                hashed_passsword = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
                user.passwrod    = hashed_passsword

            user.save()

            return JsonResponse({"full_name" : full_name, "id" : user.id },status=200)
         
        except ValidationError as e :
            return JsonResponse({'message' : e.message}, status = 400)

        
    

