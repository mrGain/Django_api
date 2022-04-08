from django import urls
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'todo-view-set', views.TodoViewSet, basename='todo')

urlpatterns = [
    path('',views.home,name='home'),
    path('get-todo/',views.get_todo,name='get_todo'), 
    path('patch-todo/',views.patch_todo,name='patch_todo'), 
    path('post-todo/',views.post_todo,name='post_todo'),

    #for class based view.
    path('todo/',views.TodoView.as_view(),name = ''),
]
urlpatterns += router.urls
