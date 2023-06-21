from django.urls import path
from page import views 

urlpatterns=[
    path('main/',views.main_page,name='main'),
    path('sub/<str:pk>',views.sub_page,name='dame'),
]
