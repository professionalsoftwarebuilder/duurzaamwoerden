# Generated by Django 3.2.5 on 2022-07-28 14:52

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('drzData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coachgesprek',
            name='cgs_AanmeldingWoonCorp',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('V', 'Verhuizing'), ('P', 'Plaatsing nieuwe apparatuur'), ('K', 'Na een klacht'), ('Ko', 'Kleinschalig onderhoud'), ('Go', 'Grootschalig onderhoud'), ('On', 'Oplevering nieuwbouw')], help_text='De reden van aanmelding indien aangemeld via wooncooperatie', max_length=14, null=True, verbose_name='Aanmeldingsrede Wooncooperatie'),
        ),
    ]
