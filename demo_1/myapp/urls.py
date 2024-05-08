from django.urls import path, re_path
from myapp.views import MyView
from . import views
urlpatterns = [
    path('hello/', views.hello), #1
    path('menuitem/', views.menuitem), #3
    path('menuitems/', views.dishes), #4
    
    # dynamic parameter (route urls)
    path('greet/<str:name>', views.greet), #5
    path('menuSearch/<str:item>', views.menuSearch), #6
    path('addPage/<int:num1>/<int:num2>', views.addPage), #7
    
    # dynamic parameter (query urls) 
    # /recipe/?food=pizza
    path('recipe/', views.recipe), #8
    
    # Regular Expression
    re_path(r'^user/(?P<username>[a-zA-Z]*)/?$', views.user_profile), #9
    # [\w\s-] -> defination for alpha numeric values with hypen and for spacebar
    # \d{2,4} -> limit the character size from 2 to 4
    
    path('foodlist/', views.restro), #10
    path('foodSearch/<str:item>', views.restro2), #11
    
    path('home/', views.home, name='home'), #12
    path('about/', views.about, name='about'), #12
    path('food/', views.food, name='food'), #12
    path('food/<str:item>', views.detail, name='detail'), #12
    
    # forms
    path('simpleform/', views.simpleform, name='simpleform'), #13
    path('simpleform2/', views.simpleform2, name='simpleform2'), #14
    path('simpleform3/', views.simpleform3, name='simpleform3'), #15
    
    path('getform/', MyView.as_view(), name='getform'), #16
    path('testcss/', views.testcss, name='testcss'), #16
    
    path('validation/', views.validation), #17
    path('val_django_form/',views.val_django_form), #18
    
    path('signup/', views.signup), #19
    path('signup2/', views.Sign), #20
    
    path('getcookie/', views.get_cookie), #21
    path('setcookie/', views.set_cookie), #21
    path('deletecookie/', views.delete_cookie), #21
    
    path('blogpost/', views.blogpost), #22
    path('blogpost2/<int:id>', views.blogpost2), #22
    
    path('setcookie2/', views.set_cookie2), # 23
    path('getcookie2/', views.get_cookie2), # 23
    
    path('set-session/', views.set_session, name='set_session'), #24
    path('get-session/', views.get_session, name='get_session'), #24
    path('delete-session/', views.delete_session, name='delete_session'), #24
    
    path('user-login/', views.user_login, name='login'), #25
    path('user-homee/', views.homee, name='homee'), #25
    path('user-logout/', views.user_logout, name='logout'), #25
    ]