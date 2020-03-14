from django.urls import path
from projectfiles import views

app_name='html'

urlpatterns = [

    path('', views.index, name='Home'),
    path('contactMe/', views.contactMe, name='contactMe'),
    path('learn_more/',views.learnMore,name='learnMore')


]