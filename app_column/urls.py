from django.urls import path

from app_column.views import add_column, search_column, show_column

app_name = 'column'

urlpatterns = [
    path('add', add_column),
    path('search', search_column),
    path('show',show_column),
]
