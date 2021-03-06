# Generated by Django 2.1 on 2018-12-24 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='book',
        ),
        migrations.AddField(
            model_name='borrow',
            name='book',
            field=models.OneToOneField(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to='library.Book'),
        ),
        migrations.RemoveField(
            model_name='borrow',
            name='student',
        ),
        migrations.AddField(
            model_name='borrow',
            name='student',
            field=models.OneToOneField(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to='library.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
