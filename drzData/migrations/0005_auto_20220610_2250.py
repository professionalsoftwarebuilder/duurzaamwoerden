# Generated by Django 3.0.5 on 2022-06-10 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drzData', '0004_auto_20220610_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groep',
            options={'verbose_name_plural': 'Organisaties, Instanties, Bedrijven, enz.'},
        ),
        migrations.AddField(
            model_name='groep',
            name='grp_Type',
            field=models.CharField(blank=True, choices=[('B', 'Bedrijf'), ('I', 'Instantie'), ('S', 'Stichting'), ('O', 'Organisatie'), ('G', 'Gemeente'), ('R', 'Rijksoverheid'), ('A', 'Afdeling')], default='O', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='adres',
            name='Contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drzData.Contact'),
        ),
        migrations.AlterField(
            model_name='adres',
            name='Groep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drzData.Groep'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cnt_Groepen',
            field=models.ManyToManyField(blank=True, to='drzData.Groep'),
        ),
        migrations.AlterField(
            model_name='nummer',
            name='Contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drzData.Contact'),
        ),
        migrations.AlterField(
            model_name='nummer',
            name='Groep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drzData.Groep'),
        ),
    ]