from django.contrib import admin
from .models import BlogPost, Comment, Author
# Register your models here.
admin.site.register(Author)
admin.site.register(BlogPost)
admin.site.register(Comment)
