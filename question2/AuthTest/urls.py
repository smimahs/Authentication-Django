from django.urls import path,include
from . import views
from django.conf.urls import url


urlpatterns = [
    path('signup',views.signUp,name='signup'),
    path('signin',views.signIn,name='signin'),
    #path('sendpassword/<str:mobile>',views.send_Password,name='sendpassword'),
    #url(r'^sendpassword/$',views.send_Password,name='sendpassword'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^sendtemppassword$',views.check_temporary_password,name='sendtemppassword'),
    
]