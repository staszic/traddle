from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post, Category, Tag, Comment
from .forms import CommentForm


# Create your views here.
def home(request):
    post_list = Post.objects.order_by('-pub_date')
    cat_list = Category.objects.order_by('slug')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'post_list': posts, 'cat_list': cat_list}
    return render(request, 'blog/home.html', context)


def year_archive(request, year):
    post_list = Post.objects.filter(pub_date__year=year).order_by('-pub_date')
    cat_list = Category.objects.order_by('slug')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'year': year, 'post_list': posts, 'cat_list': cat_list}
    return render(request, 'blog/home.html', context)


def month_archive(request, year, month):
    post_list = Post.objects.filter(pub_date__year=year).filter(pub_date__month=month).order_by('-pub_date')
    cat_list = Category.objects.order_by('slug')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'year': year, 'month': month, 'post_list': posts, 'cat_list': cat_list}
    return render(request, 'blog/home.html', context)


def post_detail(request, year, month, pk):
    post = Post.objects.filter(pk=pk).get()
    comments_list = Comment.objects.filter(post=post).order_by('created_date')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            message = 'Komentarz dodano.'
    else:
        form = CommentForm()
    context = {'post': post, 'comment_form': form, 'comments_list': comments_list}
    return render(request, 'blog/post.html', context)


def year_category_list(request, year, slug):
    category = Category.objects.filter(slug=slug).get()
    post_list = Post.objects.filter(pub_date__year=year).filter(category=category).order_by('-pub_date')
    cat_list = Category.objects.order_by('slug')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    url = request.resolver_match.url_name
    context = {'year': year, 'post_list': posts, 'cat_list': cat_list, 'url': url}
    return render(request, 'blog/home.html', context)


def month_category_list(request, year, month, slug):
    category = Category.objects.filter(slug=slug).get()
    post_list = Post.objects.filter(pub_date__year=year).filter(pub_date__month=month).filter(category=category)\
        .order_by('-pub_date')
    cat_list = Category.objects.order_by('slug')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    url = request.resolver_match.url_name
    context = {'year': year, 'month': month, 'post_list': posts, 'cat_list': cat_list, 'url': url}
    return render(request, 'blog/home.html', context)


def category_list(request, slug):
    category = Category.objects.filter(slug=slug).get()
    post_list = Post.objects.filter(category=category).order_by('-pub_date')
    cat_list = Category.objects.order_by('slug')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    url = request.resolver_match.url_name
    context = {'category': category, 'post_list': posts, 'cat_list': cat_list, 'url': url}
    return render(request, 'blog/home.html', context)


def tag_list(request, slug):
    tag = Tag.objects.filter(slug=slug).get()
    post_list = Post.objects.filter(tags=tag).order_by('-pub_date')
    cat_list = Category.objects.order_by('slug')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'tag': tag, 'post_list': posts, 'cat_list': cat_list}
    return render(request, 'blog/home.html', context)