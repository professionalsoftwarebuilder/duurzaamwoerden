# Generated by Django 3.2.5 on 2022-06-19 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drzData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adres',
            name='adr_type',
            field=models.CharField(blank=True, choices=[('W', 'Woonadres'), ('B', 'Bezoekadres'), ('A', 'Afleveradres'), ('V', 'Verblijfadres')], default='W', max_length=1, null=True, verbose_name='Type adres'),
        ),
        migrations.AlterField(
            model_name='adresgroep',
            name='adg_type',
            field=models.CharField(blank=True, choices=[('W', 'Woonadres'), ('B', 'Bezoekadres'), ('A', 'Afleveradres'), ('V', 'Verblijfadres')], default='W', max_length=1, null=True, verbose_name='Type adres'),
        ),
        migrations.AlterField(
            model_name='groep',
            name='grp_Type',
            field=models.CharField(blank=True, choices=[('B', 'Bedrijf'), ('I', 'Instantie'), ('S', 'Stichting'), ('O', 'Organisatie'), ('G', 'Gemeente'), ('R', 'Rijksoverheid'), ('A', 'Afdeling')], default='O', max_length=1, null=True, verbose_name='Type groep'),
        ),
        migrations.AlterField(
            model_name='nummer',
            name='nmb_Notities',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Notitie'),
        ),
    ]