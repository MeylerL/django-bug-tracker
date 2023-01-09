from django.urls import path


from . import views

app_name = 'bug_page'

urlpatterns = [
    path('register/', views.user_form, name='user_form'),
    path('user_login/', views.user_login, name = 'user_login'),
    path('view_bugs/', views.bug_table, name = 'bug_table'),
    path('make_bugs/', views.bug_form, name = 'bug_form'),
    path('update_bug/', views.update_bug, name = 'update_bug'),
]
