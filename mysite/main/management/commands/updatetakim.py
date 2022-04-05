import pandas as pd
import requests
import json
from django.core.management.base import BaseCommand, CommandError
from main.models import takimanalizi

class Ligİstatistikleri():

    headers = {

        'Accept': 'application/json, text/javascript, */*; q=0.01 ',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,und;q=0.5',
        'Referer': 'http://arsiv.mackolik.com/Puan-Durumu',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Cookie': '_ga=GA1.2.2133557660.1587285911; __gfp_64b=khm1_e4Ki4XykKFyexukCucnluehxQEeR.Nabuw3oXX.I7; _hjid=4742c787-abce-4f83-97d7-dea512cbde9b; __gads=ID=261b1cb6dd1a79f1:T=1587285925:S=ALNI_MaNT3AyBA15hmX0-oh_RO2dlaHxww; OPTAW_gaCookie=GA1.3.2133557660.1587285911; _gid=GA1.2.1069800500.1590499689; _gat_UA-241588-3=1; am_cookie_test=true; _gat=1; intdate=1590499718190; GED_PLAYLIST_ACTIVITY=W3sidSI6IkZkOHgiLCJ0c2wiOjE1OTA0OTk3MTksIm52IjoxLCJ1cHQiOjE1OTA0OTk3MTQsImx0IjoxNTkwNDk5NzE4fV0.; M_BK=125939,472394,255822,120375,375028,255824,123372,156089,218843,120255,123371,466106,255826,103520,114039,123370,255825'


    }

    def __init__(self, ligid=59416):

        self.ligid = ligid
        
        #Sadece Lig id ile çalışır.
        #Lig İçin tüm istatistikleri döndürür
      
      
        
    def HaftanınMacları(self):
           
          #Lig İçin haftanın maçları alınır
         
      
            json_url = 'http://arsiv.mackolik.com/AjaxHandlers/StandingHandler.ashx?'
            j = requests.get(url=json_url, headers=Ligİstatistikleri.headers, params={'op': 'standing', 'id': self.ligid})
            standing = json.loads(j.content)
            maclar = pd.DataFrame.from_dict(standing['f'])
            maclar1 = maclar[[0,1,2,3,4,6,7,8,12,13]]
            
            maclar1.columns = ['Macid','Tarih','Saat','Evid','Depid','Ms1','Ms0','Ms2','Alt','Ust']
            
            return maclar1

    def PuanDurumu(self):
        
            
            #Ligin son puan durumunu alır
        
           
      
            json_url = 'http://arsiv.mackolik.com/AjaxHandlers/StandingHandler.ashx?'
            j = requests.get(url=json_url, headers=Ligİstatistikleri.headers, params={'op': 'standing', 'id': self.ligid})
            standing = json.loads(j.content)
            PuanDurum = pd.DataFrame.from_dict(standing['s'])
            
        
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
            PuanTüm['Lig'] = self.ligid

            return PuanTüm
     
    def Form(self):
        
            json_url = 'http://arsiv.mackolik.com/Standings/Data/FormData.aspx?'
            frm = requests.get(url=json_url, headers=Ligİstatistikleri.headers, params={'id': self.ligid})
            Formx = pd.DataFrame(eval(frm.text))
            Form = Formx.iloc[:, 0:4]
            Form.columns = ['Takımİd','FormTüm','Formİ','FormD']
        
            return Form

    def KgVar(self):

            json_url = 'http://arsiv.mackolik.com/Standings/Data/KGData.aspx?'
            au = requests.get(url=json_url, headers=Ligİstatistikleri.headers, params={'id': self.ligid})
            kg = pd.DataFrame(eval(au.text))
            kg.columns = ['Takımİd','X','Var','Yok','KgSeri','Varİ','Yokİ','KgSeriİ','VarD','YokD','KgSeriD']
            kg.drop('X', axis=1,inplace = True)

            return kg

       
    def AltUst(self):

            json_url = 'http://arsiv.mackolik.com/Standings/Data/UnderOverData.aspx?'
            au = requests.get(url=json_url, headers=Ligİstatistikleri.headers, params={'id': self.ligid})
            AltUst = pd.DataFrame(eval(au.text))
            AltUst.columns = ['Takımİd','X','Alt','Üst','Seri','Altİ','Ustİ','Seriİ','AltD','UstD','SeriD']
            AltUst.drop('X', axis=1,inplace = True)

            return AltUst

    def IyMs(self):
        
            json_url = 'http://arsiv.mackolik.com/Standings/Data/MatchResultData.aspx'
            im = requests.get(url=json_url, headers=Ligİstatistikleri.headers, params={'id': self.ligid})
            IYMS= pd.DataFrame(eval(im.text))
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
       
            return IYMS
    
    def Hafta(self):
        
        h  = self.PuanDurumu()
        hafta = min(h['Oynadığı'])
        
        return hafta
    
    def Tumİstatistikler(self):
        
        Puan = self.PuanDurumu()
        Form = self.Form()
        kg = self.KgVar()
        au = self.AltUst()
        im = self.IyMs()
        
        Res1 = Puan.merge(Form,on='Takımİd').merge(kg,on='Takımİd').merge(au,on='Takımİd').merge(im,on='Takımİd')
        
        return Res1
    
    def LigTemelAnaliz(self):
        
        ist = self.Tumİstatistikler()
        
        #Üstündeki fonksiyonda tüm istatistikleri belli olan veriler birleştirilir ve 
        #bir takım takım için gerekli istatistikler ortaya çıkar
        
        İ_O = ist['Oynadığı_İ']+0.0000000001
        D_O = ist['Oynadığı_D']+0.0000000001
        O = ist['Oynadığı']+0.000000001
        
        ist['İ_G_O'] = round((ist['G_İ']/İ_O)*100,2)
        ist['İ_B_O'] = round((ist['B_İ']/İ_O)*100,2)
        ist['İ_M_O'] = round((ist['M_İ']/İ_O)*100,2)
        
        ist['D_G_O'] = round((ist['G_D']/D_O)*100,2)
        ist['D_B_O'] = round((ist['B_D']/D_O)*100,2)
        ist['D_M_O'] = round((ist['M_D']/D_O)*100,2)
        
        ist['G_O'] = round((ist['G']/O)*100,2)
        ist['B_O'] = round((ist['B']/O)*100,2)
        ist['M_O'] = round((ist['M']/O)*100,2)
        
        
        ist['Attığı_İ_O'] = round(ist['Attığı_İ']/İ_O,2)
        ist['Attığı_D_O'] = round(ist['Attığı_D']/D_O,2)
        ist['Attığı_Ort'] = round(ist['Attığı']/O,2)
        
        ist['Puan_İ_O'] = round(ist['Puan_İ']/İ_O,2)
        ist['Puan_D_O'] = round(ist['Puan_D']/D_O,2)
        ist['Puan_Ort'] = round(ist['Puan']/O,2)
        
        ist['Ust_İ_O'] = round(ist['Ustİ']/İ_O,2)*100
        ist['Ust_D_O'] = round(ist['UstD']/D_O,2)*100
        ist['Ust_Ort'] = round(ist['Üst']/O,2)*100
        
        ist['Var_İ_O'] = round(ist['Varİ']/İ_O,2)*100
        ist['Var_D_O'] = round(ist['VarD']/D_O,2)*100
        ist['Var_Ort'] = round(ist['Var']/O,2)*100
        
        
        ist['İY_Gİ_O'] = round((ist['GGİ']+ist['GBİ']+ist['GMİ'])/İ_O,2)*100
        ist['İY_Bİ_O'] = round((ist['BGİ']+ist['BBİ']+ist['BMİ'])/İ_O,2)*100
        ist['İY_Mİ_O'] = round((ist['MGİ']+ist['MBİ']+ist['MMİ'])/İ_O,2)*100
        
        ist['İY_GD_O'] = round((ist['GGD']+ist['GBD']+ist['GMD'])/D_O,2)*100
        ist['İY_BD_O'] = round((ist['BGD']+ist['BBD']+ist['BMD'])/D_O,2)*100
        ist['İY_MD_O'] = round((ist['MGD']+ist['MBD']+ist['MMD'])/D_O,2)*100
        
        ist['İY_G_O'] = round((ist['GG']+ist['GB']+ist['GM'])/O,2)*100
        ist['İY_B_O'] = round((ist['BG']+ist['BB']+ist['BM'])/O,2)*100
        ist['İY_M_O'] = round((ist['MG']+ist['MB']+ist['MM'])/O,2)*100
        ist['Ligid'] = self.ligid
        
        
        

        return ist


class Command(BaseCommand):
    help = 'add data'

    def add_arguments(self, parser):
        parser.add_argument('Ligid', type=int)

    def handle(self, *args, **options):
        takimanalizi.objects.all().delete()
        self.stdout.write(self.style.ERROR(' Takım Analizi Veri Tabanı verileri silindi'))

        if takimanalizi.objects.filter(Ligid=options['Ligid']):
            print("Bu veri Var")
        else:
            print("Bu Veri yok ekleniyor")
            lig = Ligİstatistikleri(options['Ligid'])
            df = lig.LigTemelAnaliz()
            json_list = json.loads(json.dumps(list(df.T.to_dict().values())))
            for dic in json_list:
                takimanalizi.objects.get_or_create(**dic)