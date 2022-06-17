# Generated by Django 3.0.5 on 2022-06-11 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drzData', '0005_auto_20220610_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='NummerGroep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmg_Number', models.CharField(help_text='Mobiel, Telefoon, E-mail, Facebook, enz.', max_length=85, verbose_name='Nummer')),
                ('nmg_Medium', models.CharField(blank=True, choices=[('M', 'Mobiel nummer'), ('H', 'Huistelefoon'), ('E', 'E-Mail'), ('F', 'Fax'), ('A', 'Facebook'), ('L', 'LinkedIn'), ('T', 'Twitter')], max_length=1, null=True, verbose_name='Medium')),
                ('nmg_Notities', models.CharField(blank=True, help_text='Kanttekening bij dit medium', max_length=120, null=True, verbose_name='Notitie')),
                ('Groep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drzData.Groep')),
            ],
        ),
        migrations.CreateModel(
            name='AdresGroep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adg_Straat', models.CharField(blank=True, max_length=100, null=True, verbose_name='Straat')),
                ('adg_HuisNr', models.CharField(blank=True, max_length=10, null=True, verbose_name='Huisnummer')),
                ('adg_HuisNrToev', models.CharField(blank=True, max_length=10, null=True, verbose_name='Toevoeging')),
                ('adg_PostCd', models.CharField(blank=True, max_length=15, null=True, verbose_name='Postcode')),
                ('adg_Plaats', models.CharField(blank=True, max_length=85, null=True, verbose_name='Plaats')),
                ('adg_type', models.CharField(blank=True, choices=[('W', 'Woonadres'), ('B', 'Bezoekadres'), ('A', 'Afleveradres'), ('V', 'Verblijfadres')], default='W', max_length=1, null=True)),
                ('adg_Notities', models.TextField(blank=True, null=True, verbose_name='Notities')),
                ('Groep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drzData.Groep')),
            ],
            options={
                'verbose_name_plural': 'Adressen Groepen',
            },
        ),
    ]