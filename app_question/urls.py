from django.urls import path

from app_question.views import add_question, update_question, show_single_question, show_question_list, show_all

app_name='question'

urlpatterns = [
    path('add', add_question),
    path('update', update_question),
    path('show', show_single_question),
    path('search',show_question_list),
    path('all',show_all),
]