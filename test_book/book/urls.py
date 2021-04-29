from django.urls import path,include
from book import views
from django.conf.urls import url

urlpatterns=[
      path('book/',views.BookList.as_view()),
      url('useris/(?P<token>.*)$',views.Useris.as_view()),
]