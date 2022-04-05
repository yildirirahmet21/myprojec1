
from django.urls import path
from .views import macayrinti,puandurumu


app_name="main"

urlpatterns = [

    path('<int:my_id>',macayrinti,name='ayrinti'),
    path('PuanDurumu/',puandurumu,name='puandurumu'),
     
]

