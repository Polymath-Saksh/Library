# Generated by Django 3.1.5 on 2021-02-26 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20210226_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_books',
            name='istatus',
            field=models.CharField(choices=[('Available', True), ('Issued', False)], default='Available', max_length=10),
        ),
    ]