from django.urls import path
from dashreporting.views import dash1
from dashreporting.dash_apps import app1

app_name="dashreporting"

urlpatterns = [

    path('app1/',dash1,name='dashapp'),
    
]
