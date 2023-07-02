from django.urls import path
from .import views


urlpatterns=[
    path('home/',views.home,name='home'),
    path('afterlogin/',views.afterLogin,name='after_login'),
    path('login/',views.userLogin,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('afterlogin/',views.afterLogin,name='after_login'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/<str:username>/', views.edit_profile, name='edit_profile'),
    path('profile/picture/', views.change_profile_picture, name='edit_profile_picture'),
    path('create-post/', views.create_post, name='create_post'),

]