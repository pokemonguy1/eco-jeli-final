from wagtail.blocks import StructBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock

class FigCaptionBlock(StructBlock):

    caption = CharBlock()
    figure = ImageChooserBlock(label="Изображение")

    class Meta:
        icon='images'
        template = 'blocks/fig_caption_block.html'
        label="Изображение с подписью"