# Generated by Django 4.0.4 on 2022-06-08 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='blogtag',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
