# Generated by Django 2.0.4 on 2018-04-19 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('due', models.DateTimeField(verbose_name='due date')),
                ('end', models.DateTimeField(verbose_name='end date')),
            ],
        ),
    ]
