from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# class EmailBackend(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             email = email.lower()
#             user = UserModel.objects.get(email=email)
#         except UserModel.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password):
#                 return user
#         return None

# class SecretTesterBackend(ModelBackend):
#     def authenticate(self, request, nickname=None, secret=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             nickname = nickname.lower()
#             secret = secret.lower()
#             user = UserModel.objects.get(secret=secret)
#         except UserModel.DoesNotExist:
#             return None
#         else:
#             if user.check_password(secret):
#                 return user
#         return None