from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
    path('',views.index, name='index'),
    path('create/',views.create, name='create'),
    path('detail/<int:reviewpk>',views.detail, name='detail'),
    path('new/',views.new, name='new'),
    path('edit/<int:reviewpk>',views.edit, name='edit'),
    path('update/<int:reviewpk>',views.update, name='update'),
    path('delete/<int:reviewpk>',views.delete, name='delete'),
]