import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_user(request):
    request_body = json.loads(request.body.decode())

    if request.method == "POST":
        username = request_body['username']
        password = request_body['password']
        authenticated_user = authenticate(username=username, password=password)

        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({"valid": True, "token": token.key})
            return HttpResponse(data, content_type='application/json')
        else:
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')

@csrf_exempt
def register_user(request):
    request_body = json.loads(request.body.decode())
    
    new_user = User.objects.create_user(
        username = request_body['username'],
        first_name = request_body['first_name'],
        last_name = request_body['last_name'],
        email = request_body['email'],
        password = request_body['password']
    )

    token = Token.objects.create(user=new_user)
    data = json.dumps({"token": token.key})
    return HttpResponse(data, content_type='application/json')