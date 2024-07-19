from django.contrib import admin

# Register your models here.

from .models import Tag, Tool, Comment, HomePageMessage

class ToolAdmin(admin.ModelAdmin):
    list_display = ["name","visits","hidden"]

# admin.site.register(Suggestions)
admin.site.register(Tag)
admin.site.register(Tool,ToolAdmin)
admin.site.register(Comment)
admin.site.register(HomePageMessage)
