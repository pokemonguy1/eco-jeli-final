from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from .blocks import FigCaptionBlock

class BlogIndexPage(Page):

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]


class BlogPage(Page):

    date = models.DateField("Дата публикации")
    intro = models.CharField(max_length=250, blank=True, null=True, verbose_name="Подзаголовок")
    body = RichTextField(blank=True, verbose_name="Содержание")
    author = models.CharField(max_length=250, blank=True, null=True, verbose_name="Автор")

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('author'),
    ]