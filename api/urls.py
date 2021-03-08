from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
     path('snippets/', views.SnippetList.as_view()),
    path('snippets/<np>/', views.SnippetList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)