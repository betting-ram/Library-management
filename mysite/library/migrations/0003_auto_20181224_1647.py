# Generated by Django 2.1 on 2018-12-24 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20181224_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='book',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='library.Book'),
        ),
    ]
