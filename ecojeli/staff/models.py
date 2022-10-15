from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel

class Staff(Orderable):

    page = ParentalKey("StaffPage", related_name="staff", on_delete=models.CASCADE)

    name = models.CharField(max_length=250, verbose_name="ФИО", default="", null=True, blank=True)
    email = models.CharField(max_length=250, verbose_name="Почта", default="", null=True, blank=True)
    role = models.CharField(max_length=250, verbose_name="Должность", default="", null=True, blank=True)
    photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Фотография"
    )

class StaffPage(Page):
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                InlinePanel("staff", min_num=1, label="Карточка"),
            ],
            heading="Сотрудники"
        )
    ]
