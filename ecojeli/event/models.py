from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

class EventIndexPage(Page):
    heading = models.CharField(max_length=250, blank=True, null=True, verbose_name="Подзаголовок")

    intro = RichTextField(blank=True)

    bgimg = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Задний фон"
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('intro'),
        ImageChooserPanel('bgimg'),
    ]


class EventPage(Page):
    date = models.DateField("Дата проведения")
    bgimg = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Задний фон"
    )
    intro = models.CharField(max_length=250, blank=True, null=True, verbose_name="Подзаголовок")
    body = StreamField([
        ('rtfblock', RichTextBlock(label="Текст")),
        ('embedblock', EmbedBlock(label="Ссылка"))

    ], blank=True, verbose_name="Содержимое")
    author = models.CharField(max_length=250, blank=True, null=True, verbose_name="Автор")

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    joinbtn = models.CharField(max_length=500, blank=True, null=True, verbose_name="Участвовать ссылка")
    reviewbtn = models.CharField(max_length=500, blank=True, null=True, verbose_name="Оставить отзыв ссылка")


    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('bgimg'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('author'),
        FieldPanel('joinbtn'),
        FieldPanel('reviewbtn')
    ]