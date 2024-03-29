# Generated by Django 4.1.2 on 2022-10-14 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('blog', '0004_alter_blogpage_bgimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='bgimg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Задний фон'),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='heading',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Подзаголовок'),
        ),
    ]
