from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, PageChooserPanel, MultiFieldPanel, InlinePanel

class HomePage(Page):
 templates = "home/home_page.html"
 max_count = 1
 banner_title = models.CharField(max_length=100, blank=False, null=True)
 banner_subtitle = RichTextField(default=" ", features = ["italic", "bold"])
 
 banner_image = models.ForeignKey(
  "wagtailimages.Image",
  null=True,
  blank=False,
  on_delete=models.SET_NULL,
  related_name="banner"
 )

 banner_cta = models.ForeignKey(
  "wagtailcore.Page",
  null=True,
  blank=True,
  on_delete=models.SET_NULL,
  related_name="+"
 )
 content_panels = Page.content_panels + [
  FieldPanel ("banner_title"),
  FieldPanel ("banner_subtitle"),
  FieldPanel("banner_image"),
  PageChooserPanel("banner_cta"),
 ]
