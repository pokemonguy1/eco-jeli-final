from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey


from .blocks import FigCaptionBlock



class Slider(Orderable):

    page = ParentalKey("home.HomePage", related_name="slides", on_delete=models.CASCADE)

    #slide_header = models.CharField(max_length=200, verbose_name="Заголовок Слайда", default="") #koroche if still operational error "no such column home_slider.slide_header, delete this row
    carousel_title = models.CharField(max_length=250, verbose_name="Заголовок слайда", default="", null=True, blank=True)
    carousel_caption = models.CharField(max_length=600, verbose_name="Текст слайда", default="", null=True, blank=True)
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Изображение слайда"
    )


class HomePage(Page):

    max_count = 1

    subtitle = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Подзаголовок"
    )


    body = RichTextField(blank=True, verbose_name="Содержание")


    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                InlinePanel("slides", min_num=1, label="Слайд"),
            ],
            heading="Слайдер",
        ),
        FieldPanel('subtitle'),
        StreamFieldPanel('body'),

    ]
