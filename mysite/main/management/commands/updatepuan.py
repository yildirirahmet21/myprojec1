import pandas as pd
import requests
import json
import urllib
from django.core.management.base import BaseCommand, CommandError
from main.models import PuanDurumu

def LigStat(idx):
  

    headers = {
    
        'Accept': 'application/json, text/javascript, */*; q=0.01 ',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,und;q=0.5',  
        'Referer': 'http://arsiv.mackolik.com/Puan-Durumu',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Cookie': '_ga=GA1.2.2133557660.1587285911; __gfp_64b=khm1_e4Ki4XykKFyexukCucnluehxQEeR.Nabuw3oXX.I7; _hjid=4742c787-abce-4f83-97d7-dea512cbde9b; __gads=ID=261b1cb6dd1a79f1:T=1587285925:S=ALNI_MaNT3AyBA15hmX0-oh_RO2dlaHxww; OPTAW_gaCookie=GA1.3.2133557660.1587285911; _gid=GA1.2.1069800500.1590499689; _gat_UA-241588-3=1; am_cookie_test=true; _gat=1; intdate=1590499718190; GED_PLAYLIST_ACTIVITY=W3sidSI6IkZkOHgiLCJ0c2wiOjE1OTA0OTk3MTksIm52IjoxLCJ1cHQiOjE1OTA0OTk3MTQsImx0IjoxNTkwNDk5NzE4fV0.; M_BK=125939,472394,255822,120375,375028,255824,123372,156089,218843,120255,123371,466106,255826,103520,114039,123370,255825'
    
      }
    
################# Request İstekleri  ##############################################################################

    
    try:
        
        #Puan Durumu #############################################
        json_url = 'http://arsiv.mackolik.com/AjaxHandlers/StandingHandler.ashx?op=standing&id=' + str(idx)
        j = requests.get(url=json_url , headers=headers)
        standing = json.loads(j.content) 
        PuanDurum = pd.DataFrame.from_dict(standing['s'])
        
        
        #Form Data################################################
        json_url = 'http://arsiv.mackolik.com/Standings/Data/FormData.aspx?id=' + str(idx)
        frm = requests.get(url=json_url , headers=headers)
        Form =  pd.DataFrame(eval(frm.text))  
        
        
        #ALt Üst Data################################################
        json_url = 'http://arsiv.mackolik.com/Standings/Data/UnderOverData.aspx?id=' + str(idx)
        au = requests.get(url=json_url , headers=headers)
        AltUst =  pd.DataFrame(eval(au.text))  
        
        #KG Data################################################
        json_url = 'http://arsiv.mackolik.com/Standings/Data/KGData.aspx?id=' + str(idx)
        kg = requests.get(url=json_url , headers=headers)
        KGData =  pd.DataFrame(eval(kg.text))  
        
        
        #IYMS Data################################################
        json_url = 'http://arsiv.mackolik.com/Standings/Data/MatchResultData.aspx?id=' + str(idx)
        iyms = requests.get(url=json_url , headers=headers)
        IYMS =  pd.DataFrame(eval(iyms.text))    
        
    except:
        print('Lig istatistik Kaynağında Hata Oluştu')
    
 ##################### Düzeltmeler ###############################################333333

    try:
        #Puan Durumu #############################################
        
        PuanDurum.columns = ['Takımİd','TakımAdı','Oynadığı_İ','Oynadığı_D','G_İ','G_D','B_İ','B_D','M_İ','M_D','Attığı_İ','Attığı_D',
                    'Yediği_İ','Yediği_D','Puan_İ','Puan_D','A','B','C','D']


        Puanİçerde  = PuanDurum[['Takımİd','TakımAdı','Oynadığı_İ','G_İ','B_İ','M_İ','Attığı_İ',
                    'Yediği_İ','Puan_İ']]


        PuanDışarda  = PuanDurum[['Takımİd','TakımAdı','Oynadığı_D','G_D','B_D','M_D','Attığı_D',
                    'Yediği_D','Puan_D']]


        PuanTüm = pd.merge(Puanİçerde,PuanDışarda,on = 'Takımİd')

        PuanTüm['Oynadığı'] =  PuanTüm['Oynadığı_İ'] + PuanTüm['Oynadığı_D']
        PuanTüm['G'] =  PuanTüm['G_İ'] + PuanTüm['G_D']
        PuanTüm['B'] =  PuanTüm['B_İ'] + PuanTüm['B_D']
        PuanTüm['M'] =  PuanTüm['M_İ'] + PuanTüm['M_D']
        PuanTüm['Attığı'] =  PuanTüm['Attığı_İ'] + PuanTüm['Attığı_D']
        PuanTüm['Yediği'] =  PuanTüm['Yediği_İ'] + PuanTüm['Yediği_D']
        PuanTüm['Puan'] =  PuanTüm['Puan_İ'] + PuanTüm['Puan_D']

        PuanTüm.drop('TakımAdı_y', axis=1 ,inplace = True) 

        #Form Data #############################################
        
        Form = Form.iloc[:, 0:4]
        Form.columns = ['Takımİd','FormTüm','Formİ','FormD']
        PuanTüm = pd.merge(PuanTüm,Form,on = 'Takımİd')   
        
        
        #Alt Üst Data #############################################
        
        AltUst.columns = ['Takımİd','X','Alt','Üst','Seri','Altİ','Ustİ','Seriİ','AltD','UstD','SeriD']
        AltUst.drop('X', axis=1,inplace = True)
        PuanTüm = pd.merge(PuanTüm,AltUst,on = 'Takımİd') 
        
        
        #KG Data #############################################
        
        KGData.columns = KGData.columns = ['Takımİd','X','Var','Yok','KgSeri','Varİ','Yokİ','KgSeriİ','VarD','YokD','KgSeriD']
        PuanTüm = pd.merge(PuanTüm,KGData,on = 'Takımİd')  
        
        
        #IYMS Data #############################################
        
        IYMS.columns = ['Takımİd','X','Y','Z','GGİ','GBİ','GMİ','BGİ','BBİ','BMİ','MGİ','MBİ','MMİ',
                                     'MMD','MBD','MGD','BMD','BBD','BGD','GMD','GBD','GGD']


        IYMS['GG'] = IYMS['GGİ'] + IYMS['GGD']
        IYMS['GB'] = IYMS['GBİ'] + IYMS['GBD']
        IYMS['GM'] = IYMS['GMİ'] + IYMS['GMD']
        IYMS['BG'] = IYMS['BGİ'] + IYMS['BGD']
        IYMS['BB'] = IYMS['BBİ'] + IYMS['BBD']
        IYMS['BM'] = IYMS['BMİ'] + IYMS['BMD']
        IYMS['MG'] = IYMS['MGİ'] + IYMS['MGD']
        IYMS['MB'] = IYMS['MBİ'] + IYMS['MBD']
        IYMS['MM'] = IYMS['MMİ'] + IYMS['MMD']


        IYMS.drop(['X', 'Y','Z'], axis=1,inplace = True)
        PuanTüm = pd.merge(PuanTüm,IYMS,on = 'Takımİd')
        PuanTüm.drop('TakımAdı_x', axis=1,inplace = True)
        PuanSon = PuanTüm.insert(1, 'Ligİd', str(idx))
        return PuanTüm 
    
    
    except:
        
        print('Veri Düzenlemesinde Bir Hata Oluştu')


class Command(BaseCommand):
    help = 'add data'

    def add_arguments(self, parser):
         parser.add_argument('lig_id', type=int)

    def handle(self, *args, **options):
        PuanDurumu.objects.all().delete()
        self.stdout.write(self.style.ERROR(' Puan Durumu Veri Tabanı verileri silindi'))
        if PuanDurumu.objects.filter(Ligİd=options['lig_id']):
            print("Bu veri Var")
        else:
            print("Bu Veri yok ekleniyor")
            df=LigStat(options['lig_id'])
            json_list = json.loads(json.dumps(list(df.T.to_dict().values())))
            for dic in json_list:
                PuanDurumu.objects.get_or_create(**dic)
           