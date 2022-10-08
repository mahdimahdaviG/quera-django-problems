from cmath import inf
from time import timezone
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
import copy
# TODO write all of your code here...

class Author(models.Model):
    name = models.CharField(max_length=50)

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def copy(self):
        new_post = BlogPost()
        new_post.title = self.title
        new_post.body = self.body
        new_post.author = self.author
        new_post.date_created = timezone.now
        new_post.save()

        new_post_comments = Comment.objects.filter(blog_post_id = self.id)
        for comment in new_post_comments:
            new_comment = Comment()
            new_comment.blog_post = new_post
            new_comment.text = comment.text
            print(new_comment)
            new_comment.save(self)
            # print(Comment.objects.all())

        return new_post.id

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)

