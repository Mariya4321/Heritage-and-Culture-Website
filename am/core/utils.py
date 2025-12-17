from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

def authenticate(email, password):
    try:
        user = User.objects.get(email=email)
        if check_password(password, user.password):
            return user
        else:
            return None
    except User.DoesNotExist:
        return None