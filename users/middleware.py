
from django.shortcuts import reverse, redirect


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self,request):

        if request.user.is_authenticated or request.path == reverse("login"):
            return self.get_response(request)
        else:
            return redirect(reverse("login"))