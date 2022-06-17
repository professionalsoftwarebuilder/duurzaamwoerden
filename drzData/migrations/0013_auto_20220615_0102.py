# Generated by Django 3.0.5 on 2022-06-15 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drzData', '0012_auto_20220615_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='vraag',
            name='Contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drzData.Contact'),
        ),
        migrations.AddField(
            model_name='vraag',
            name='id',
            field=models.BigIntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]