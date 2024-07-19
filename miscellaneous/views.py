from django.shortcuts import render, redirect
# from .models import Suggestions
from django.utils import timezone
from django.http import HttpResponse, FileResponse, JsonResponse
from django.conf import settings

from .models import Tag, Tool, HomePageMessage
from django.template.loader import render_to_string
from django.db.models import Q
from django.urls import reverse
from django.core.paginator import Paginator

# comment imports
from .models import Comment
# Create your views here.

def maintenence(request):
    pass

def sitemap_txt(request):
    sitemap = open(file= settings.BASE_DIR / 'static/outward/sitemap.txt', mode='rb')
    response = HttpResponse(content=sitemap,content_type="text/plain")
    return response

def robots_txt(request):
    robots = open(file= settings.BASE_DIR / 'static/outward/robots.txt', mode='rb')
    response = HttpResponse(content=robots,content_type="text/plain")
    return response

# def maintenance(request):
#     return render(request, "miscellaneous/countdown.html")

# moving tools data onto database was succesful, new home page view
def home_page(request):
    home_page_message = HomePageMessage.objects.all().first()
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest"
    if is_ajax_request and request.method == "GET":
        try:
            search = request.GET["search"]
        except:
            search = None
        
        try:
            sort = request.GET["sort_by"]
        except:
            sort = None

        if search != None:
            search_term = request.GET["search"]
            #queries both the name of the tool and the tag name incrementally
            tools = Tool.objects.filter(Q(name__icontains=search_term) | Q(tags__name__icontains=search_term)).distinct()
            html = render_to_string(
                template_name="tools_results_partial.html", 
                context={"tools": tools, "home_page_message": home_page_message}
            )

            return JsonResponse(data={"html_from_view": html}, safe=False)
        elif sort != None:
            sort_by = request.GET["sort_by"]
            if sort_by == "A to Z":
                # alphabetical order
                tools = Tool.objects.order_by("name")
            elif sort_by == "Z to A":
                # reverse alphabetical order
                tools = Tool.objects.order_by("-name")
            elif sort_by == "Newest":
                # newest to oldest
                tools = Tool.objects.order_by("date_added")[::-1]
            elif sort_by == "Most Popular":
                # most popular to least popular based on visits
                tools = Tool.objects.order_by("-visits")
            elif sort_by == "Oldest":
                # oldest to newest
                tools = Tool.objects.order_by("date_added")
            else:
                # default sort - Featured and then newest to oldest
                tools = Tool.objects.order_by('-featured', '-date_added')
            
            html = render_to_string(
                template_name="tools_results_partial.html", 
                context={"tools": tools, "home_page_message": home_page_message}
            )
            return JsonResponse(data={"html_from_view": html}, safe=False)
    else:
        tools = Tool.objects.order_by('-featured', '-date_added')
        return render(request,"index.html",{"tools":tools, "home_page_message": home_page_message})
        

# decrapated, New system uses local storage on the frontend
# def theme(request):
#     if request.method == "POST":
#         request.session.get('theme', 'dark')
#         if request.POST['theme'] == 'light':
#             request.session['theme'] = 'light'
#         elif request.POST['theme'] == 'dark':
#             request.session['theme'] = 'dark'
#         return HttpResponse(status=200)
#     else:
#         return HttpResponse(f"{request.session.get('theme', 'dark')}",content_type="text/plain",status=200)

# moving tools data onto database was succesful
def tags(request,tags):
    # for debugging
    # print(tags)
    tags_list = tags.split("-")
    # for debugging
    # print(tags_list)
    filtered_tools = Tool.objects.filter(tags__name__in=[tags_list[0]]).distinct()
    # print(filtered_tools.values_list("name","tags__name"))
    for i in range(1,len(tags_list)):
        filtered_tools = filtered_tools.filter(tags__name__in=[tags_list[i]]).distinct()
        # for debugging
        # print(filtered_tools.values_list("name","tags__name"))
    return render(request, "index.html",{'tools':filtered_tools,"filter_tags":tags_list})

def about(request):
    return render(request, "about.html")

def comment_section(request):
    if request.method == "GET":
        # print(request.GET["show_hide"])
        if request.GET["show_hide"] == "hide":
            request.session["comment_section_status"] = False
            return JsonResponse(data={"pass":"through"})
        else:
            request.session["comment_section_status"] = True
        
        comments = Comment.objects.order_by("-date_sent")
        pagination = Paginator(comments, 5)
        page_number = request.GET.get('page')
        page_obj = pagination.get_page(page_number)
        html = render_to_string(
            template_name="comment_section.html", 
            context={"comments": page_obj}
        )
        return JsonResponse(data={"comment_section_html": html}, safe=False)

def comment(request):
    return HttpResponse(status=404)
    if request.method == "POST":
        new_comment = Comment(commenter_name=request.POST["commenter_name"],date_sent=timezone.now(),comment=request.POST["comment"],comment_type=request.POST["comment_type"])
        new_comment.save()
        print("saved")
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)

def search(request):
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest"
    if is_ajax_request and request.method == "GET":
        try:
            search = request.GET["search"]
        except:
            search = None
        
        try:
            sort = request.GET["sort_by"]
        except:
            sort = None

        if search != None:
            search_term = request.GET["search"]
            #queries both the name of the tool and the tag name incrementally
            tools = Tool.objects.filter(Q(name__icontains=search_term) | Q(tags__name__icontains=search_term)).distinct()
            # SQL of the above query for debugging
            # SELECT DISTINCT "miscellaneous_tool"."id", "miscellaneous_tool"."name", "miscellaneous_tool"."url", "miscellaneous_tool"."description", "miscellaneous_tool"."category", "miscellaneous_tool"."visits", "miscellaneous_tool"."date_added", "miscellaneous_tool"."hidden" FROM "miscellaneous_tool" LEFT OUTER JOIN "miscellaneous_tool_tags" ON ("miscellaneous_tool"."id" = "miscellaneous_tool_tags"."tool_id") LEFT OUTER JOIN "miscellaneous_tag" ON ("miscellaneous_tool_tags"."tag_id" = "miscellaneous_tag"."id") WHERE ("miscellaneous_tool"."name" LIKE %1% ESCAPE '\' OR "miscellaneous_tag"."name" LIKE %1% ESCAPE '\')
            html = render_to_string(
                template_name="search_autocomplete.html", 
                context={"tools": tools[0:3]}
            )
            return JsonResponse(data={"html_from_view": html}, safe=False)
    elif request.method == "GET":
        search_term = request.GET["search"]
        #queries both the name of the tool and the tag name incrementally
        tools = Tool.objects.filter(Q(name__icontains=search_term) | Q(tags__name__icontains=search_term)).distinct()
    return render(request, "search_results.html",{"search_term":search_term,"tools":tools})

def secret_tester(request):
    print("in secret tester")
    if request.method == "POST":
        print("hey")
        print(request.POST["password"])
        if request.POST["password"] == "amaltools2023":
            print("correct")
            request.session["secret_tester"] = True
            return redirect(reverse("home"))
        else:
            return render(request, "secret_test_login.html",{"msg":"Incorrect Password"})
    return render(request, "secret_test_login.html")

def acknowledgement(request):
    return render(request, "acknowledgements.html")

def maths_tools_page(request):
    tools = Tool.objects.filter(category="Maths")
    return render(request,"index.html",{"tools":tools})

def programming_tools_page(request):
    tools = Tool.objects.filter(category="Programming")
    return render(request, "index.html", {"tools":tools})

def converters_tools_page(request):
    tools = Tool.objects.filter(category="Converters")
    return render(request, "index.html", {"tools":tools})

def fileconverters_tools_page(request):
    tools = Tool.objects.filter(category="File Converters")
    return render(request, "index.html", {"tools":tools})

def others_tools_page(request):
    tools = Tool.objects.filter(category="Other")
    return render(request, "index.html", {"tools":tools})

# deprecated, New system uses database
# def tags(request,tags):
#     if tags == None:
#         print("yes")
#     tags = tags.split("-")
#     print(tags)
#     list_tools = format_txt.format_txt(file_path=settings.BASE_DIR / 'static_files/tools.txt')
#     filter_tags = []
#     filtered_tools = []
#     for i in range(len(list_tools)):
#         var = list_tools[i]["tags"]
#         tag_check_count = 0
#         for tag in tags:
#             tags_to_check_num = len(tags)
#             print(f"{list_tools[i]['name']}, {var},{tag}")
#             if tag in var:
#                 tag_check_count += 1
#             print(tag_check_count)
#             # if tag in var and list_tools[i] not in filtered_tools :
#             #     
#             # else:
#             #     print("got here")
#             #     if list_tools[i] in filtered_tools:
#             #         print(f"removed {list_tools[i]}")
#             #         filtered_tools.remove(list_tools[i])
#         if tags_to_check_num == tag_check_count:
#             print("added")
#             print(f"tags need to find {tags_to_check_num} what {tag_check_count} tags found")
#             filtered_tools.append(list_tools[i])
#     print(filtered_tools)
#     print(tags)
#     return render(request, "index.html",{'tools':filtered_tools,"filter_tags":tags})

# deprecated, New system uses database
# def home_page(request):
#     tools = format_txt.format_txt(file_path=settings.BASE_DIR / 'static_files/tools.txt')
#     return render(request, "index.html",{'tools':tools})

# def suggestion_page(request):
#     if request.method == "POST":
#         suggestion = Suggestions(name=request.POST["name"],email=request.POST["email"],creation_date=timezone.now(),suggestion=request.POST["suggestion"])
#         suggestion.save()
#         msg_state = "pass"
#         return render(request, "miscellaneous/suggestion_page.html",{"msg_state":msg_state})
#     else:
#         return render(request, "miscellaneous/suggestion_page.html")

# def suggestions_overview(request):
#     suggestions_all = Suggestions.objects.all()
#     return render(request, "miscellaneous/suggestion_overview.html",{"suggestions":suggestions_all})
