from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()

    # Store datetime objects
    # Adds time whenever an instance of this class is created
    created_on = models.DateTimeField(auto_now_add=True)
    # Adds time whenever an instance of this class is saved (remember .save() or use django admin)
    last_modified = models.DateTimeField(auto_now=True)

    # Many categories can be related to many posts
    # First argument: what model to relate to
    # Second argument: Can access category.posts, list of posts with that category (example Music.posts)
    categories = models.ManyToManyField('Category', related_name='posts')


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    # Establishes a many to one relation: A post can have many comments but not the other way around
    # First argument: What model it relates to (same as ManyToManyField)
    # Second argument: What to do if the post is deleted, delete the comment!
    post = models.ForeignKey('Post', on_delete=models.CASCADE)



