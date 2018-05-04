from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:year>/', views.year_archive, name='yearly'),
    path('<int:year>/category/<slug>', views.year_category_list, name='category_listed_yearly'),
    path('<int:year>/<int:month>/', views.month_archive, name='monthly'),
    path('<int:year>/<int:month>/category/<slug>', views.month_category_list, name='category_listed_monthly'),
    path('<int:year>/<int:month>/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<slug>/', views.category_list, name='category_listed'),
    path('tag/<slug>/', views.tag_list, name='tag_listed'),
    url(r'^', views.home, name='home'),
]