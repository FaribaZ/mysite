from django.db import models
from wagtail.admin.panels import FieldPanel, PageChooserPanel, MultiFieldPanel, InlinePanel
from wagtail.models import Page

# Create your models here.
class FlexPage(Page):
 templates = "flex/flex_page.html"
 
 subtitle = models.CharField(max_length=100, blank=False, null=True)
 
 content_panels = Page.content_panels + [
  FieldPanel ("subtitle"),
 ]
 
 class Meta():
     verbose_name= "Flex Page"
     verbose_name_plural= "Flex Pages"