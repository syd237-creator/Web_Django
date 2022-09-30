# Generated by Django 4.0.4 on 2022-06-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='author',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='ip',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='name',
            field=models.CharField(default='Annoymous', max_length=255),
        ),
    ]