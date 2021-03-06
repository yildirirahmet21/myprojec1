# Generated by Django 3.2.12 on 2022-02-10 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_puandurumu_ligi̇d'),
    ]

    operations = [
        migrations.CreateModel(
            name='takimanalizi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Takımİd', models.IntegerField()),
                ('TakımAdı_x', models.CharField(max_length=50)),
                ('Oynadığı_İ', models.IntegerField()),
                ('G_İ', models.IntegerField()),
                ('B_İ', models.IntegerField()),
                ('M_İ', models.IntegerField()),
                ('Attığı_İ', models.IntegerField()),
                ('Yediği_İ', models.IntegerField()),
                ('Puan_İ', models.IntegerField()),
                ('Oynadığı_D', models.IntegerField()),
                ('G_D', models.IntegerField()),
                ('B_D', models.IntegerField()),
                ('M_D', models.IntegerField()),
                ('Attığı_D', models.IntegerField()),
                ('Yediği_D', models.IntegerField()),
                ('Puan_D', models.IntegerField()),
                ('Oynadığı', models.IntegerField()),
                ('G', models.IntegerField()),
                ('B', models.IntegerField()),
                ('M', models.IntegerField()),
                ('Attığı', models.IntegerField()),
                ('Yediği', models.IntegerField()),
                ('Puan', models.IntegerField()),
                ('Lig', models.IntegerField()),
                ('FormTüm', models.CharField(max_length=50)),
                ('Formİ', models.CharField(max_length=50)),
                ('FormD', models.CharField(max_length=50)),
                ('Var', models.IntegerField()),
                ('Yok', models.IntegerField()),
                ('KgSeri', models.CharField(max_length=50)),
                ('Varİ', models.IntegerField()),
                ('Yokİ', models.IntegerField()),
                ('KgSeriİ', models.CharField(max_length=50)),
                ('VarD', models.IntegerField()),
                ('YokD', models.IntegerField()),
                ('KgSeriD', models.CharField(max_length=50)),
                ('Alt', models.IntegerField()),
                ('Üst', models.IntegerField()),
                ('Seri', models.CharField(max_length=50)),
                ('Altİ', models.IntegerField()),
                ('Ustİ', models.IntegerField()),
                ('Seriİ', models.CharField(max_length=50)),
                ('AltD', models.IntegerField()),
                ('UstD', models.IntegerField()),
                ('SeriD', models.CharField(max_length=50)),
                ('GGİ', models.IntegerField()),
                ('GBİ', models.IntegerField()),
                ('GMİ', models.IntegerField()),
                ('BGİ', models.IntegerField()),
                ('BBİ', models.IntegerField()),
                ('BMİ', models.IntegerField()),
                ('MGİ', models.IntegerField()),
                ('MBİ', models.IntegerField()),
                ('MMİ', models.IntegerField()),
                ('MMD', models.IntegerField()),
                ('MBD', models.IntegerField()),
                ('MGD', models.IntegerField()),
                ('BMD', models.IntegerField()),
                ('BBD', models.IntegerField()),
                ('BGD', models.IntegerField()),
                ('GMD', models.IntegerField()),
                ('GBD', models.IntegerField()),
                ('GGD', models.IntegerField()),
                ('GG', models.IntegerField()),
                ('GB', models.IntegerField()),
                ('GM', models.IntegerField()),
                ('BG', models.IntegerField()),
                ('BB', models.IntegerField()),
                ('BM', models.IntegerField()),
                ('MG', models.IntegerField()),
                ('MB', models.IntegerField()),
                ('MM', models.IntegerField()),
                ('İ_G_O', models.FloatField()),
                ('İ_B_O', models.FloatField()),
                ('İ_M_O', models.FloatField()),
                ('D_G_O', models.FloatField()),
                ('D_B_O', models.FloatField()),
                ('D_M_O', models.FloatField()),
                ('G_O', models.FloatField()),
                ('B_O', models.FloatField()),
                ('M_O', models.FloatField()),
                ('Attığı_İ_O', models.FloatField()),
                ('Attığı_D_O', models.FloatField()),
                ('Attığı_Ort', models.FloatField()),
                ('Puan_İ_O', models.FloatField()),
                ('Puan_D_O', models.FloatField()),
                ('Puan_Ort', models.FloatField()),
                ('Ust_İ_O', models.FloatField()),
                ('Ust_D_O', models.FloatField()),
                ('Ust_Ort', models.FloatField()),
                ('Var_İ_O', models.FloatField()),
                ('Var_D_O', models.FloatField()),
                ('Var_Ort', models.FloatField()),
                ('İY_Gİ_O', models.FloatField()),
                ('İY_Bİ_O', models.FloatField()),
                ('İY_Mİ_O', models.FloatField()),
                ('İY_GD_O', models.FloatField()),
                ('İY_BD_O', models.FloatField()),
                ('İY_MD_O', models.FloatField()),
                ('İY_G_O', models.FloatField()),
                ('İY_B_O', models.FloatField()),
                ('İY_M_O', models.FloatField()),
                ('Ligid', models.IntegerField()),
            ],
        ),
    ]
