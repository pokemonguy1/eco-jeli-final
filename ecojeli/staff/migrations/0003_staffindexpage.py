# Generated by Django 4.1.2 on 2022-10-31 18:00

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0077_alter_revision_user'),
        ('staff', '0002_rename_carousel_image_staff_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('heading', models.CharField(blank=True, max_length=250, null=True, verbose_name='Подзаголовок')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
