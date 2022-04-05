import pandas as pd
import requests
import json
from django.core.management.base import BaseCommand, CommandError
from main.models import FiksturModelim



def Fikstür(tarih):

    json_url = 'http://goapi.mackolik.com/livedata?'
    j = requests.get(url=json_url,params = { "date" : tarih } )

    content = json.loads(j.content)
    df1 = pd.DataFrame.from_dict(content['m'])

    df1 = df1[[0,1,2,3,4,5,6,7,10,11,12,13,14,16,18,19,20,21,22,34,35,36]]

    df1['Ulke']= df1[36].apply(lambda x: x[1])
    df1['Ulke_id']= df1[36].apply(lambda x: x[2])
    df1['Lig']= df1[36].apply(lambda x: x[3])
    df1['Sezon_id']= df1[36].apply(lambda x: x[4])
    df1['Sezon_Yıl']= df1[36].apply(lambda x: x[5])
    df1['Lig_Adı']= df1[36].apply(lambda x: x[9])

    df1 = df1.drop([36],axis=1)

    df1 = df1.rename(columns={0: 'id',1: 'ev_id',2: 'Ev',3: 'dep_id',4: 'Dep',5: 'Seç_id',6: 'Dk_Skor',7: 'Canlı_skor',
                          10: 'iye_s',11: 'iyd_s',12: 'mse_s',13: 'msd_s',14: 'Nesine_id',16: 'Saat',18: 'OranMS1',
                          19: 'OranMS0',20: 'OranMS2',21: 'OranAlt',22: 'OranÜst',34: 'Canlı_Seç',35: 'Tarih'})

    df1 = df1[['Ulke_id','Sezon_id','id','Nesine_id','Canlı_Seç',
    'Seç_id','ev_id','dep_id','Ulke','Lig','Sezon_Yıl','Tarih','Saat',
    'Lig_Adı','Ev','Dep','Dk_Skor','Canlı_skor','iye_s','iyd_s',
    'mse_s','msd_s','OranMS1','OranMS0','OranMS2','OranAlt','OranÜst']]

    return df1




class Command(BaseCommand):
    help = 'add data'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        from datetime import datetime
        bugun = datetime.today().strftime('%d/%m/%Y')
        df=Fikstür(bugun)
       
        datem = []
        for i in df['Tarih']:
            res = datetime.strptime(i, "%d/%m/%Y").strftime("%Y-%m-%d")
            datem.append(res)
        df['Tarih'] = datem
        FiksturModelim.objects.all().delete()
        self.stdout.write(self.style.ERROR('Veri Tabanı verileri silindi'))
        json_list = json.loads(json.dumps(list(df.T.to_dict().values())))
        for dic in json_list:
            FiksturModelim.objects.get_or_create(**dic)
       
  