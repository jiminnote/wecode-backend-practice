import bcrypt
import jwt
from django.http import JsonResponse

from users.models   import User
from wesop.settings import SECRET_KEY,ALGORITHM             

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            assess_token = request.headers.get('Authorization',None) 
            payload      = jwt.decode(assess_token, SECRET_KEY, ALGORITHM) 
            user         = User.objects.get(email=payload['user_id']) 
            request.user = user
            return func(self, request, *args, **kwargs)

        except jwt.exceptions.InvalidSignatureError: 
            return JsonResponse({'message': 'INVALID_SIGNATURE_ERROR'}, status=401)

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message': 'DECODE_ERROR' }, status=401)

        except User.DoesNotExist:
            return JsonResponse({'message': 'USER_DOES_NOT_EXIST_ERROR'}, status=401)

        except jwt.exceptions.ExpiredSignatureError:
            return JsonResponse({"message": "EXPIRED_TOKEN"}, status=401)
    return wrapper