from config.urls import path
from .views import HomePageView

urlpatterns =[
    path('',HomePageView.as_view(), name='home'),
]