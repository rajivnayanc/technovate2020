from django.db import models

# Create your models here.


class Blogs(models.Model):
    blog_title = models.TextField()
    blog_content = models.TextField()
    blog_image = models.ImageField(
        upload_to='blogs_image', height_field=None, width_field=None, max_length=None)
    author_name = models.TextField()
    author_profile_link = models.URLField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title
