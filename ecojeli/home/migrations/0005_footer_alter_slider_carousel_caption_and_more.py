# Generated by Django 4.1.2 on 2022-10-13 13:51

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_slider_carousel_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodytext', wagtail.fields.RichTextField()),
            ],
        ),
        migrations.AlterField(
            model_name='slider',
            name='carousel_caption',
            field=models.CharField(blank=True, default='', max_length=600, null=True, verbose_name='Текст слайда'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='carousel_title',
            field=models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='Заголовок слайда'),
        ),
    ]
