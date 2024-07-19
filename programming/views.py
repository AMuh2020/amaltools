from django.shortcuts import render

from .functions import img_b64, css_to_inline
# Create your views here.

def image_b64(request):
    if request.method == "POST":
        # print(request.POST['direction'])
        if request.POST['direction'] == "image_to_base64":
            file = request.FILES['image'].read()
            # print(file[0:10])
            base64_string = img_b64.img_to_b64(file)
            # print(base64_string[0:10])
            return render(request,"programming/img_b64.html",{"base64_string":base64_string,"direction":"image_to_base64"})
        elif request.POST['direction'] == "base64_to_image":
            # print("here")
            base64_string = request.POST['base64_string']
            return render(request,"programming/img_b64.html",{"base64_string":base64_string,"direction":"base64_to_image"})
    return render(request,"programming/img_b64.html")

def css_to_inline_view(request):
    library_reference = {
        "name": "Beutiful Soup 4",
        "link": "https://www.crummy.com/software/BeautifulSoup/bs4/doc/",
    }
    if request.method == "POST":
        html = request.POST["html"]
        # print(html) 
        new_html = css_to_inline.css_to_inline(html)
        return render(request,"programming/css_to_inline.html",{"html":new_html,"library_reference":library_reference})
    return render(request,"programming/css_to_inline.html",{"library_reference":library_reference})

def html_viewer(request):
    return render(request,"programming/html_viewer.html")