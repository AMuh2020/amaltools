from django.db import models

# Create your models here.
# class Suggestions(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     creation_date = models.DateTimeField('date created')
#     suggestion = models.CharField(max_length=500)

#     # Returns name    
#     def __str__(self):
#         return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True)

    # Returns name
    def __str__(self):
        return self.name

options = {
    ("Maths","Maths"),
    ("Programming","Programming"),
    ("Other","Other"),
    ("Converters","Converters"),
    ("File Converters","File Converters"),
}

# class for tools 
class Tool(models.Model):
    name = models.CharField(max_length=100) # name of tool
    url = models.CharField(max_length=200) # url to tool
    description = models.CharField(max_length=1000) # description of tool
    category = models.CharField(max_length=100, choices=options, default="Other") # category of tool
    tags = models.ManyToManyField(Tag, blank=True)  # tags for tool
    visits = models.IntegerField(default=0) # number of times tool has been visited
    date_added = models.DateTimeField('date added') # date tool was added
    hidden = models.BooleanField(default=False) # if tool is hidden from users
    featured = models.BooleanField(default=False) # if tool is featured

    # Returns name
    def __str__(self):
        return self.name



class Comment(models.Model):
    commenter_name = models.CharField(max_length=100) # name of commenter
    date_sent = models.DateTimeField('date commented') # date comment was made
    comment = models.CharField(max_length=1000) # comment   
    COMMENT_TYPES = [
        ('General Comment', 'General Comment'),
        ('Tool Suggestion', 'Tool Suggestion'),
        ('Bug Report', 'Bug Report'),
        ('Other', 'Other'),
    ]
    comment_type = models.CharField(blank=True ,max_length=30, choices=COMMENT_TYPES) # type of comment

    def __str__(self):
        return self.comment

# shows latest message on the home page
class HomePageMessage(models.Model):
    message = models.TextField() # message to be displayed on the home page
    date_added = models.DateTimeField('date added', auto_now_add=True)  # Automatically set to now when object is first created.
    
    def __str__(self):
        return self.message