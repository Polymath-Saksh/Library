# Generated by Django 3.1.5 on 2021-02-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20210227_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('btitle', models.CharField(max_length=30, unique=True)),
                ('author', models.CharField(blank=True, max_length=30)),
                ('istatus', models.CharField(choices=[('Available', True), ('Issued', False)], default='Available', max_length=10)),
                ('uissued', models.CharField(blank=True, max_length=30)),
                ('date', models.DateField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='All_Books',
        ),
        migrations.DeleteModel(
            name='Available_Books',
        ),
        migrations.DeleteModel(
            name='Issued_Books',
        ),
    ]
