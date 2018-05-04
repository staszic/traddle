from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    img_url = models.ImageField(upload_to='media/icons', null=True)
    style_cat = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    headline = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    body_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    mod_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media/images', blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.headline

    def get_comments_count(self):
        return Comment.objects.filter(post=self).count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=50, verbose_name='imię')
    email = models.EmailField(verbose_name='adres e-mail (nie będzie publikowany)')
    text = models.TextField(verbose_name='treść komentarza')
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.text