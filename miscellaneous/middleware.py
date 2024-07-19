from django.http import HttpResponsePermanentRedirect
from django.template.response import TemplateResponse
from django.conf import settings

from django.shortcuts import reverse, redirect
from .models import Tool
#https://adamj.eu/tech/2020/03/02/how-to-make-django-redirect-www-to-your-bare-domain/

class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #also added for now https
        host = request.get_host().partition(":")[0]
        if host == "www.amaltools.com" or host == "http://amaltools.com":
            return HttpResponsePermanentRedirect("https://amaltools.com" + request.path)
        else:
            return self.get_response(request)


class MaintenencePageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        path = request.META.get('PATH_INFO', "")
        # print(path)

        # if settings.MAINTENANCE_MODE and path!= reverse("maintenance"):
        #     response = redirect(reverse("maintenance"))
        #     return response
        # else:
        #     return self.get_response(request)

        
        if settings.MAINTENANCE_MODE == True and request.session.get("secret_tester",False) == False and request.path != reverse("tester")[0:-1] and request.path != reverse("tester"):
            t = TemplateResponse(request, 'down.html',status=307) #504 for service unavailable
            t.render()
            return t
        else:
            return self.get_response(request)

# new middleware to count page views uses request.path
class PageViewsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        path = request.path
        print(path)
        # session check for page viewd in last 2 hours
        if settings.MAINTENANCE_MODE == False:
            try:
                path = path.split('/')[2]
                # print(path)
                tool = Tool.objects.get(url=path)
                # print(tool)
                tool.visits += 1
                # print(tool.visits)
                tool.save()
                # print(tool.visits)
            except:
                # print("not a tools page")
                pass
                    
                # path = path.split('/')  # split path into list
                # # print(path[1])
                # tool = Tool.objects.filter(url=path[1]).first()
                # # print(tool)
                # tool.visits += 1
                # tool.save()
        return self.get_response(request)
    

class TesterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        # print("here")
        # print(request.session.get("secret_tester",False))
        if request.path == reverse("tester")[0:-1] or request.path == reverse("tester"):
            return self.get_response(request)
        if request.session.get("secret_tester",False) == False and settings.MAINTENANCE_MODE == True:
            if request.path == reverse("home") or request.path == reverse("home")[0:-1]:
                t = TemplateResponse(request, 'down.html',status=200) #504 for service unavailable
                t.render()
                return t
            t = TemplateResponse(request, 'down.html',status=307) #504 for service unavailable
            t.render()
            return t
        else:
            pass
        return self.get_response(request)