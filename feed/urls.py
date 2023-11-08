from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # i want to redirect to feed if path is ""
    path('', lambda request: redirect('feed/')),
    
    path('feed/', views.message_list, name='message_list'),
    path('messages/create/', views.create_message, name='create_message'),
    path('messages/<int:message_id>/', views.comment_list, name='comment_list'),
    path('messages/<int:message_id>/comment/', views.create_comment, name='create_comment'),
    path('messages/<int:message_id>/edit/', views.update_message, name='update_message'),
    path('messages/<int:message_id>/delete/', views.delete_message, name='delete_message'),
    path('message/<int:message_id>/like/', views.like_message, name='like_message'),
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),

    # auth
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
