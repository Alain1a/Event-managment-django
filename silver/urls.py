from django.urls import path
from .views import home, Register,Login,Signup,Forgot_Passward, Create_new_account,about_us
from .import views

urlpatterns = [
    path('', home, name='home'),
    path('Register', Register, name='Register'),
    path('Login', Login, name='Login'),
    path('Createaccount', Signup, name='Signup'),
    path('About', about_us, name='About Us'),
    path('Forgot_Password', Forgot_Passward, name='Forgot_Passward'),
    # path('Forgot', views.Forgot, name='Forgot'),
    # path('Book Your Ticket.html', login, name='login')
    
    # path('park/', Signup, name='Signup'),
   
]

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('Register', views.Register, name='Register'),
#     path('Login', views.Login, name='Login'),
#     path('Create', views.Signup, name='Signup'),
#     path('About', views.about_us, name='About'),
#     path('Reset', views.Forgot, name='Forgot'),
#     # path('Book Your Ticket.html', login, name='login')
    
#     # path('park/', Signup, name='Signup'),
   
# ]












