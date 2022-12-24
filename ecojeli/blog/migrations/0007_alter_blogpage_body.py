# Generated by Django 4.1.2 on 2022-10-31 17:52

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.StreamField([('rtfblock', wagtail.blocks.RichTextBlock(label='Текст')), ('embedblock', wagtail.embeds.blocks.EmbedBlock(label='Ссылка'))], blank=True, use_json_field=None, verbose_name='Содержимое'),
        ),
    ]