
import bcrypt
import jwt

from django.http     import JsonResponse

from users.models    import User
from westagram.settings import SECRET_KEY,ALGORITHM  

def Signin_decorator(func):
    def wrapper(self,request,*args,**kwargs):
        
        try:
            access_token = request.headers.get('Authorization',None) # HTTP request의 헤더 Authorization 값 가져오는데 없으면 None
            payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM) # payload:토큰을 디코딩하면 나오는 사용자정보 / 동일한 사용자라면 동일한 payload가 반환
            user = User.objects.get(email=payload['email']) # payload와 매치되는 사용자 정보를 HTTP request user에 저장
            request.user = user
            return func(self, request, *args, **kwargs)
            
        except User.DoesNotExist: # User 테이블에 매치되는 값이 없을 때
            return JsonResponse({'message': 'USER_DOES_NOT_EXIST_ERROR'}, status=400)
            
    return wrapper