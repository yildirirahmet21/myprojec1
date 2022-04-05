from django.shortcuts import render
from .models import FiksturModelim,PuanDurumu,takimanalizi
import logging
from django.core.management import call_command
from fonksiyonlar.graph1 import grafik1
import pandas as pd
import sqlite3 as db
logger = logging.getLogger(__name__)


def homepage(request):
    print('home page çalıştı')
    datam = FiksturModelim.objects.all()
    return render(request,'main/home.html',context={'datam':datam})

def macayrinti(request,my_id):
         print("Maç Ayrıntı Çalışıyor")
         obj= FiksturModelim.objects.get(id=my_id)
         call_command('updatepuan', obj.Sezon_id)
         call_command('updatetakim', obj.Sezon_id)
         puan1 = PuanDurumu.objects.filter(Takımİd=obj.ev_id)
         puan2 = PuanDurumu.objects.filter(Takımİd=obj.dep_id)
         puand = takimanalizi.objects.all()
         return render(request,'maclar.html',context={'obj':obj,'puan1':puan1,'puan2':puan2,'puand':puand})

def puandurumu(request):
    print("Puan Durumu Çalışıyor")
    call_command('updatedata')
    data = PuanDurumu.objects.all()
    
    p1 = grafik1(data)
    return render(request,'puandurumu.html',context={'plot_div':p1})

