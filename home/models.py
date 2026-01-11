from django.db import models
from django.core.exceptions import ValidationError
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, PageChooserPanel, MultiFieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.snippets.models import register_snippet
from wagtail.contrib.table_block.blocks import TableBlock
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from .widgets import ColorPickerWidget


class CarouselSlideBlock(blocks.StructBlock):
    """Individual carousel slide"""
    slide_type = blocks.ChoiceBlock(
        choices=[
            ('image', 'Image'),
            ('video', 'Video (YouTube/Vimeo)'),
        ],
        default='image',
        help_text="Choose between image or video slide"
    )
    image = ImageChooserBlock(required=False, help_text="Upload an image (for image slides)")
    image_fit = blocks.ChoiceBlock(
        choices=[
            ('cover', 'Cover (fill area, may crop)'),
            ('contain', 'Contain (show full image, may letterbox)'),
            ('fill', 'Fill (stretch to fit)'),
            ('top', 'Cover - Align Top'),
            ('bottom', 'Cover - Align Bottom'),
            ('left', 'Cover - Align Left'),
            ('right', 'Cover - Align Right'),
        ],
        default='cover',
        required=False,
        help_text="How the image should fit within the carousel"
    )
    video_url = blocks.URLBlock(required=False, help_text="YouTube or Vimeo URL (for video slides)")
    heading = blocks.CharBlock(required=False, max_length=255, help_text="Slide heading")
    description = blocks.TextBlock(required=False, max_length=500, help_text="Slide description")
    button_text = blocks.CharBlock(required=False, max_length=50, help_text="Button text")
    button_link = blocks.URLBlock(required=False, help_text="Button link")
    text_position = blocks.ChoiceBlock(
        choices=[
            ('left', 'Left'),
            ('center', 'Center'),
            ('right', 'Right'),
        ],
        default='center',
        help_text="Position of text overlay"
    )

    class Meta:
        icon = 'image'
        label = 'Carousel Slide'


class CarouselBlock(blocks.StructBlock):
    """Carousel/Slider for images and videos"""
    slides = blocks.ListBlock(CarouselSlideBlock(), max_num=6, help_text="Add up to 6 slides")
    autoplay = blocks.BooleanBlock(required=False, default=True, help_text="Auto-play carousel")
    autoplay_speed = blocks.IntegerBlock(
        default=5000,
        min_value=2000,
        max_value=10000,
        help_text="Auto-play speed in milliseconds (2000-10000)"
    )
    transition_effect = blocks.ChoiceBlock(
        choices=[
            ('fade', 'Fade'),
            ('slide', 'Slide'),
            ('zoom', 'Zoom'),
        ],
        default='fade',
        help_text="Transition effect between slides"
    )
    show_dots = blocks.BooleanBlock(required=False, default=True, help_text="Show navigation dots")
    show_arrows = blocks.BooleanBlock(required=False, default=True, help_text="Show navigation arrows")

    class Meta:
        template = 'blocks/carousel_block.html'
        icon = 'image'
        label = 'Carousel'


class HeroBlock(blocks.StructBlock):
    """Hero section with background image and text"""
    heading = blocks.CharBlock(required=True, max_length=255, help_text="Main heading")
    subheading = blocks.RichTextBlock(required=False, help_text="Subheading text")
    background_image = ImageChooserBlock(required=False)
    cta_text = blocks.CharBlock(required=False, max_length=100, help_text="Call to action button text")
    cta_link = blocks.PageChooserBlock(required=False, help_text="Call to action link")
    secondary_cta_text = blocks.CharBlock(required=False, max_length=100, help_text="Secondary button text")
    secondary_cta_link = blocks.URLBlock(required=False, help_text="Secondary button link")

    class Meta:
        template = 'blocks/hero_block.html'
        icon = 'image'
        label = 'Hero Section'


class ServiceCardBlock(blocks.StructBlock):
    """Individual service card"""
    title = blocks.CharBlock(required=True, max_length=100)
    description = blocks.TextBlock(required=False, max_length=300)
    icon = blocks.CharBlock(required=False, max_length=50, help_text="Icon class name (e.g., 'fa-certificate')")
    link = blocks.PageChooserBlock(required=False)

    class Meta:
        icon = 'doc-full'
        label = 'Service Card'


class ServiceCardsBlock(blocks.StructBlock):
    """Container for multiple service cards"""
    heading = blocks.CharBlock(required=False, max_length=255)
    subheading = blocks.RichTextBlock(required=False)
    cards = blocks.ListBlock(ServiceCardBlock())

    class Meta:
        template = 'blocks/service_cards_block.html'
        icon = 'list-ul'
        label = 'Service Cards'


class ImageTextBlock(blocks.StructBlock):
    """Image with text section"""
    image = ImageChooserBlock(required=False)
    heading = blocks.CharBlock(required=False, max_length=255)
    text = blocks.RichTextBlock(required=False)
    image_position = blocks.ChoiceBlock(
        choices=[
            ('left', 'Left'),
            ('right', 'Right'),
        ],
        default='left'
    )

    class Meta:
        template = 'blocks/image_text_block.html'
        icon = 'doc-full'
        label = 'Image & Text'


class ContactFormBlock(blocks.StructBlock):
    """Contact form section"""
    heading = blocks.CharBlock(required=False, max_length=255)
    subheading = blocks.TextBlock(required=False)
    background_color = blocks.ChoiceBlock(
        choices=[
            ('light-blue', 'Light Blue'),
            ('dark-blue', 'Dark Blue'),
            ('white', 'White'),
        ],
        default='light-blue'
    )

    class Meta:
        template = 'blocks/contact_form_block.html'
        icon = 'mail'
        label = 'Contact Form'


class HeadingBlock(blocks.StructBlock):
    """Section heading"""
    text = blocks.CharBlock(required=True, max_length=255)
    level = blocks.ChoiceBlock(
        choices=[
            ('h1', 'Heading 1'),
            ('h2', 'Heading 2'),
            ('h3', 'Heading 3'),
            ('h4', 'Heading 4'),
        ],
        default='h2'
    )
    alignment = blocks.ChoiceBlock(
        choices=[
            ('left', 'Left'),
            ('center', 'Center'),
            ('right', 'Right'),
        ],
        default='left'
    )

    class Meta:
        template = 'blocks/heading_block.html'
        icon = 'title'
        label = 'Heading'


class ParagraphBlock(blocks.StructBlock):
    """Rich text paragraph"""
    content = blocks.RichTextBlock()
    alignment = blocks.ChoiceBlock(
        choices=[
            ('left', 'Left'),
            ('center', 'Center'),
            ('right', 'Right'),
            ('justify', 'Justify'),
        ],
        default='left'
    )

    class Meta:
        template = 'blocks/paragraph_block.html'
        icon = 'pilcrow'
        label = 'Paragraph'


class HTMLBlock(blocks.StructBlock):
    """Custom HTML, CSS, and JavaScript code"""
    html = blocks.TextBlock(
        help_text="Enter HTML, CSS (wrapped in <style> tags), and JavaScript (wrapped in <script> tags)"
    )

    class Meta:
        template = 'blocks/html_block.html'
        icon = 'code'
        label = 'HTML/CSS/JS Code'


class EmbedMapBlock(blocks.StructBlock):
    """Embedded map or media"""
    embed_url = EmbedBlock(
        required=False,
        help_text="Paste URL from YouTube, Vimeo, etc. (for oEmbed-compatible services)"
    )
    iframe_code = blocks.TextBlock(
        required=False,
        help_text="Or paste iframe embed code directly (for Google Maps, etc.)"
    )
    height = blocks.IntegerBlock(
        default=450,
        min_value=200,
        max_value=1000,
        help_text="Height in pixels"
    )

    def clean(self, value):
        errors = {}

        # Check if at least one of the fields is filled
        if not value.get('embed_url') and not value.get('iframe_code'):
            errors['embed_url'] = ValidationError('Please provide either an embed URL or iframe code')
            errors['iframe_code'] = ValidationError('Please provide either an embed URL or iframe code')

        if errors:
            raise blocks.StructBlockValidationError(block_errors=errors)

        return super().clean(value)

    class Meta:
        template = 'blocks/embed_map_block.html'
        icon = 'site'
        label = 'Embed (Map/Video/etc)'


class ImageBlock(blocks.StructBlock):
    """Standalone image with caption"""
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False, max_length=255)
    alignment = blocks.ChoiceBlock(
        choices=[
            ('left', 'Left'),
            ('center', 'Center'),
            ('right', 'Right'),
            ('full', 'Full Width'),
        ],
        default='center'
    )
    link = blocks.URLBlock(required=False, help_text="Optional link URL")

    class Meta:
        template = 'blocks/image_block.html'
        icon = 'image'
        label = 'Image'


class QuoteBlock(blocks.StructBlock):
    """Testimonial or quote"""
    quote = blocks.TextBlock()
    author = blocks.CharBlock(required=False, max_length=100)
    author_title = blocks.CharBlock(required=False, max_length=100, help_text="Job title or company")
    author_image = ImageChooserBlock(required=False)

    class Meta:
        template = 'blocks/quote_block.html'
        icon = 'openquote'
        label = 'Quote/Testimonial'


class TestimonialItemBlock(blocks.StructBlock):
    """Individual testimonial for slider"""
    quote = blocks.TextBlock(help_text="The testimonial text")
    author = blocks.CharBlock(required=True, max_length=100, help_text="Author name")
    author_title = blocks.CharBlock(required=False, max_length=100, help_text="Job title or company")
    author_image = ImageChooserBlock(required=False, help_text="Author photo")
    rating = blocks.IntegerBlock(required=False, min_value=1, max_value=5, default=5, help_text="Star rating (1-5)")

    class Meta:
        icon = 'user'
        label = 'Testimonial'


class TestimonialSliderBlock(blocks.StructBlock):
    """Testimonial slider/carousel"""
    heading = blocks.CharBlock(required=False, max_length=255, default="What Our Clients Say")
    subheading = blocks.TextBlock(required=False, help_text="Optional subheading text")
    testimonials = blocks.ListBlock(TestimonialItemBlock(), min_num=1, max_num=10, help_text="Add testimonials")
    autoplay = blocks.BooleanBlock(required=False, default=True, help_text="Auto-play slider")
    autoplay_speed = blocks.IntegerBlock(default=5000, min_value=3000, max_value=10000, help_text="Speed in milliseconds")

    class Meta:
        template = 'blocks/testimonial_slider_block.html'
        icon = 'openquote'
        label = 'Testimonial Slider'


class ButtonBlock(blocks.StructBlock):
    """Call to action button"""
    text = blocks.CharBlock(required=True, max_length=50)
    link_page = blocks.PageChooserBlock(required=False)
    link_url = blocks.URLBlock(required=False)
    style = blocks.ChoiceBlock(
        choices=[
            ('primary', 'Primary (Blue)'),
            ('secondary', 'Secondary (Outline)'),
            ('success', 'Success (Green)'),
            ('danger', 'Danger (Red)'),
        ],
        default='primary'
    )
    alignment = blocks.ChoiceBlock(
        choices=[
            ('left', 'Left'),
            ('center', 'Center'),
            ('right', 'Right'),
        ],
        default='left'
    )

    class Meta:
        template = 'blocks/button_block.html'
        icon = 'radio-full'
        label = 'Button'


class SpacerBlock(blocks.StructBlock):
    """Add vertical spacing"""
    height = blocks.ChoiceBlock(
        choices=[
            ('small', 'Small (30px)'),
            ('medium', 'Medium (60px)'),
            ('large', 'Large (100px)'),
            ('xlarge', 'Extra Large (150px)'),
        ],
        default='medium'
    )

    class Meta:
        template = 'blocks/spacer_block.html'
        icon = 'arrows-up-down'
        label = 'Spacer'


class DividerBlock(blocks.StructBlock):
    """Horizontal divider line"""
    style = blocks.ChoiceBlock(
        choices=[
            ('solid', 'Solid Line'),
            ('dashed', 'Dashed Line'),
            ('dotted', 'Dotted Line'),
        ],
        default='solid'
    )

    class Meta:
        template = 'blocks/divider_block.html'
        icon = 'horizontalrule'
        label = 'Divider'


class AccordionItemBlock(blocks.StructBlock):
    """Individual accordion item"""
    title = blocks.CharBlock(max_length=255)
    content = blocks.RichTextBlock()

    class Meta:
        icon = 'list-ul'


class AccordionBlock(blocks.StructBlock):
    """FAQ or collapsible content"""
    items = blocks.ListBlock(AccordionItemBlock())

    class Meta:
        template = 'blocks/accordion_block.html'
        icon = 'list-ul'
        label = 'Accordion/FAQ'


class ColumnBlock(blocks.StructBlock):
    """Individual column"""
    content = blocks.RichTextBlock()

    class Meta:
        icon = 'placeholder'


class ColumnsBlock(blocks.StructBlock):
    """Multi-column layout"""
    columns = blocks.ListBlock(ColumnBlock(), min_num=2, max_num=4)

    class Meta:
        template = 'blocks/columns_block.html'
        icon = 'grip'
        label = 'Columns'


class SitemapLinkBlock(blocks.StructBlock):
    """Individual sitemap link"""
    title = blocks.CharBlock(max_length=100)
    url = blocks.URLBlock(required=False, help_text="External URL")
    page = blocks.PageChooserBlock(required=False, help_text="Or choose a page")

    class Meta:
        icon = 'link'


class SitemapColumnBlock(blocks.StructBlock):
    """Sitemap column with heading and links"""
    heading = blocks.CharBlock(max_length=100)
    links = blocks.ListBlock(SitemapLinkBlock())

    class Meta:
        icon = 'list-ul'


class SitemapBlock(blocks.StructBlock):
    """Full sitemap section with multiple columns"""
    heading = blocks.CharBlock(required=False, max_length=100, default="Sitemap", help_text="Section heading")
    show_heading = blocks.BooleanBlock(required=False, default=True)
    background_style = blocks.ChoiceBlock(
        choices=[
            ('light', 'Light Background'),
            ('dark', 'Dark Background'),
            ('gradient', 'Gradient Background'),
        ],
        default='dark'
    )
    columns = blocks.ListBlock(SitemapColumnBlock(), min_num=2, max_num=6)

    class Meta:
        template = 'blocks/sitemap_block.html'
        icon = 'site'
        label = 'Sitemap Section'


class HomePage(Page):
    """Main home page with flexible content sections"""

    body = StreamField([
        ('carousel', CarouselBlock()),
        ('hero', HeroBlock()),
        ('heading', HeadingBlock()),
        ('paragraph', ParagraphBlock()),
        ('html', HTMLBlock()),
        ('table', TableBlock()),
        ('embed_map', EmbedMapBlock()),
        ('image', ImageBlock()),
        ('service_cards', ServiceCardsBlock()),
        ('image_text', ImageTextBlock()),
        ('quote', QuoteBlock()),
        ('testimonial_slider', TestimonialSliderBlock()),
        ('button', ButtonBlock()),
        ('accordion', AccordionBlock()),
        ('columns', ColumnsBlock()),
        ('spacer', SpacerBlock()),
        ('divider', DividerBlock()),
        ('contact_form', ContactFormBlock()),
        ('sitemap', SitemapBlock()),
    ], blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Home Page"


class FlexiblePage(Page):
    """Flexible content page for About, Contact, ISO Standards, etc."""

    intro = RichTextField(blank=True, help_text="Optional introduction text")

    body = StreamField([
        ('carousel', CarouselBlock()),
        ('hero', HeroBlock()),
        ('heading', HeadingBlock()),
        ('paragraph', ParagraphBlock()),
        ('html', HTMLBlock()),
        ('table', TableBlock()),
        ('embed_map', EmbedMapBlock()),
        ('image', ImageBlock()),
        ('service_cards', ServiceCardsBlock()),
        ('image_text', ImageTextBlock()),
        ('quote', QuoteBlock()),
        ('testimonial_slider', TestimonialSliderBlock()),
        ('button', ButtonBlock()),
        ('accordion', AccordionBlock()),
        ('columns', ColumnsBlock()),
        ('spacer', SpacerBlock()),
        ('divider', DividerBlock()),
        ('contact_form', ContactFormBlock()),
        ('sitemap', SitemapBlock()),
    ], blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Flexible Page"
        verbose_name_plural = "Flexible Pages"


@register_setting
class NavigationSettings(BaseSiteSetting):
    """Site-wide navigation settings"""
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    show_search = models.BooleanField(default=True, help_text="Show search bar in navigation")

    panels = [
        FieldPanel('logo'),
        FieldPanel('show_search'),
    ]

    class Meta:
        verbose_name = 'Navigation Settings'


@register_setting
class FooterSettings(BaseSiteSetting):
    """Site-wide footer settings"""
    footer_menu = models.ForeignKey(
        'FooterMenu',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Select the footer menu to display"
    )
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    copyright_text = models.CharField(max_length=255, blank=True, default="© 2025 All rights reserved")
    show_contact_info = models.BooleanField(default=True, help_text="Show contact information in footer")

    panels = [
        FieldPanel('footer_menu'),
        FieldPanel('show_contact_info'),
        FieldPanel('phone'),
        FieldPanel('email'),
        FieldPanel('address'),
        FieldPanel('facebook_url'),
        FieldPanel('twitter_url'),
        FieldPanel('linkedin_url'),
        FieldPanel('instagram_url'),
        FieldPanel('youtube_url'),
        FieldPanel('copyright_text'),
    ]

    class Meta:
        verbose_name = 'Footer Settings'


# DEPRECATED - Use HeaderMenu instead
class MainMenu(ClusterableModel):
    """Main navigation menu - DEPRECATED"""
    title = models.CharField(max_length=100, help_text="Menu title (for admin reference only)")

    panels = [
        FieldPanel('title'),
        InlinePanel('menu_items', label="Menu Items"),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Main Menu"
        verbose_name_plural = "Main Menus"


class MenuItem(ClusterableModel, Orderable):
    """Individual menu item"""
    menu = ParentalKey(
        'MainMenu',
        on_delete=models.CASCADE,
        related_name='menu_items'
    )
    title = models.CharField(max_length=100, help_text="Menu item title")
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Link to a page"
    )
    link_url = models.URLField(blank=True, help_text="Or link to an external URL")
    open_in_new_tab = models.BooleanField(default=False, help_text="Open link in new tab")
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        help_text="Font Awesome icon class (e.g., 'fa-home')"
    )

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('open_in_new_tab'),
        FieldPanel('icon_class'),
        InlinePanel('submenu_items', label="Submenu Items"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def has_submenu(self):
        return self.submenu_items.exists()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"
        ordering = ['sort_order']


class SubMenuItem(ClusterableModel, Orderable):
    """Submenu/dropdown item (Level 2)"""
    parent = ParentalKey(
        'MenuItem',
        on_delete=models.CASCADE,
        related_name='submenu_items'
    )
    title = models.CharField(max_length=100, help_text="Submenu item title")
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Link to a page"
    )
    link_url = models.URLField(blank=True, help_text="Or link to an external URL")
    open_in_new_tab = models.BooleanField(default=False, help_text="Open link in new tab")
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        help_text="Font Awesome icon class (e.g., 'fa-home')"
    )
    description = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional description for the menu item"
    )

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('open_in_new_tab'),
        FieldPanel('icon_class'),
        FieldPanel('description'),
        InlinePanel('sub_submenu_items', label="Sub-submenu Items (Level 3)"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def has_submenu(self):
        return self.sub_submenu_items.exists()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Submenu Item"
        verbose_name_plural = "Submenu Items"
        ordering = ['sort_order']


class SubSubMenuItem(Orderable):
    """Sub-submenu item (Level 3)"""
    parent = ParentalKey(
        'SubMenuItem',
        on_delete=models.CASCADE,
        related_name='sub_submenu_items'
    )
    title = models.CharField(max_length=100, help_text="Sub-submenu item title")
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Link to a page"
    )
    link_url = models.URLField(blank=True, help_text="Or link to an external URL")
    open_in_new_tab = models.BooleanField(default=False, help_text="Open link in new tab")
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        help_text="Font Awesome icon class (e.g., 'fa-home')"
    )
    description = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional description for the menu item"
    )

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('open_in_new_tab'),
        FieldPanel('icon_class'),
        FieldPanel('description'),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sub-submenu Item"
        verbose_name_plural = "Sub-submenu Items"
        ordering = ['sort_order']


@register_snippet
class HeaderMenu(ClusterableModel):
    """
    Consolidated header navigation menu.
    Combines top bar, middle bar, and bottom bar (ISO standards) into one manageable menu.
    """
    title = models.CharField(max_length=100, help_text="Menu title (for admin reference only)")

    # Top Bar Settings
    phone_number = models.CharField(max_length=30, blank=True, help_text="Phone number to display in top bar")
    show_price_badge = models.BooleanField(default=False, help_text="Show price badge in top bar")
    price_badge_text = models.CharField(max_length=30, blank=True, default="£0.00", help_text="Price badge text")

    # Action Buttons
    show_quote_button = models.BooleanField(default=True, help_text="Show 'Request a Quote' button")
    quote_button_text = models.CharField(max_length=50, default="Request a Quote", help_text="Quote button text")
    quote_button_link = models.URLField(blank=True, default="/contact/", help_text="Quote button link")

    show_portal_button = models.BooleanField(default=True, help_text="Show 'Client Portal' button")
    portal_button_text = models.CharField(max_length=50, default="Client Portal", help_text="Portal button text")
    portal_button_link = models.URLField(blank=True, default="/admin/", help_text="Portal button link")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel([
            FieldPanel('phone_number'),
            FieldPanel('show_price_badge'),
            FieldPanel('price_badge_text'),
        ], heading="Top Bar Settings"),
        MultiFieldPanel([
            InlinePanel('top_links', label="Top Bar Links", help_text="Links like 'Why Choose Us', 'Resources', 'Contact'"),
        ], heading="Top Bar Links"),
        MultiFieldPanel([
            InlinePanel('main_links', label="Main Navigation Links", help_text="Links like 'ISO Certification', 'ISO Consultancy'"),
        ], heading="Main Navigation"),
        MultiFieldPanel([
            FieldPanel('show_quote_button'),
            FieldPanel('quote_button_text'),
            FieldPanel('quote_button_link'),
            FieldPanel('show_portal_button'),
            FieldPanel('portal_button_text'),
            FieldPanel('portal_button_link'),
        ], heading="Action Buttons"),
        MultiFieldPanel([
            InlinePanel('iso_standards', label="ISO Standards", help_text="ISO standards shown in the bottom bar"),
        ], heading="ISO Standards Bar"),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Header Menu"
        verbose_name_plural = "Header Menus"


class HeaderTopLink(Orderable):
    """Top bar link (Why Choose Us, Resources, Contact, etc.)"""
    menu = ParentalKey('HeaderMenu', on_delete=models.CASCADE, related_name='top_links')
    title = models.CharField(max_length=100)
    link_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    link_url = models.URLField(blank=True)
    open_in_new_tab = models.BooleanField(default=False)

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('open_in_new_tab'),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        return self.link_url or '#'

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort_order']


class HeaderMainLink(ClusterableModel, Orderable):
    """Main navigation link with optional dropdown (ISO Certification, ISO Consultancy, etc.)"""
    menu = ParentalKey('HeaderMenu', on_delete=models.CASCADE, related_name='main_links')
    title = models.CharField(max_length=100)
    link_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    link_url = models.URLField(blank=True)
    open_in_new_tab = models.BooleanField(default=False)

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('open_in_new_tab'),
        InlinePanel('dropdown_items', label="Dropdown Items"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        return self.link_url or '#'

    @property
    def has_dropdown(self):
        return self.dropdown_items.exists()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort_order']


class HeaderMainLinkDropdownItem(Orderable):
    """Dropdown item for main navigation link"""
    parent = ParentalKey('HeaderMainLink', on_delete=models.CASCADE, related_name='dropdown_items')
    title = models.CharField(max_length=100)
    link_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    link_url = models.URLField(blank=True)
    open_in_new_tab = models.BooleanField(default=False)

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('open_in_new_tab'),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        return self.link_url or '#'

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort_order']


class HeaderISOStandard(ClusterableModel, Orderable):
    """ISO Standard in bottom bar (with optional dropdown)"""
    menu = ParentalKey('HeaderMenu', on_delete=models.CASCADE, related_name='iso_standards')
    title = models.CharField(max_length=100, help_text="e.g., 'ISO 9001'")
    link_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    link_url = models.URLField(blank=True)

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        InlinePanel('dropdown_items', label="Dropdown Items"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        return self.link_url or '#'

    @property
    def has_dropdown(self):
        return self.dropdown_items.exists()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort_order']


class HeaderISODropdownItem(Orderable):
    """Dropdown item for ISO Standard"""
    parent = ParentalKey('HeaderISOStandard', on_delete=models.CASCADE, related_name='dropdown_items')
    title = models.CharField(max_length=100)
    link_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    link_url = models.URLField(blank=True)
    open_in_new_tab = models.BooleanField(default=False)

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('open_in_new_tab'),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        return self.link_url or '#'

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort_order']


@register_setting
class SiteMenuSettings(BaseSiteSetting):
    """Select which menus to display on the site"""
    header_menu = models.ForeignKey(
        'HeaderMenu',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Select the header menu (includes top bar, main nav, and ISO standards)"
    )
    footer_menu = models.ForeignKey(
        'FooterMenu',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Select the footer menu"
    )

    # Keep old fields for backwards compatibility during migration
    top_nav_menu = models.ForeignKey(
        'TopNavMenu',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="[DEPRECATED] Use Header Menu instead"
    )
    middle_nav_menu = models.ForeignKey(
        'MiddleNavMenu',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="[DEPRECATED] Use Header Menu instead"
    )
    main_menu = models.ForeignKey(
        'MainMenu',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="[DEPRECATED] Use Header Menu instead"
    )
    bottom_nav_menu = models.ForeignKey(
        'BottomNavMenu',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="[DEPRECATED] Use Header Menu instead"
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('header_menu'),
            FieldPanel('footer_menu'),
        ], heading="Menu Selection"),
    ]

    class Meta:
        verbose_name = 'Site Menu Settings'


# DEPRECATED - Use HeaderMenu instead
class TopNavMenu(ClusterableModel):
    """Top navigation bar menu - DEPRECATED"""
    title = models.CharField(max_length=100, help_text="Menu title (for admin reference only)")
    phone_number = models.CharField(max_length=20, blank=True, help_text="Phone number to display")
    show_price = models.BooleanField(default=False, help_text="Show price badge (£0.00)")
    price_text = models.CharField(max_length=20, blank=True, default="£0.00", help_text="Price text to display")

    panels = [
        FieldPanel('title'),
        InlinePanel('top_nav_items', label="Top Nav Items"),
        FieldPanel('phone_number'),
        FieldPanel('show_price'),
        FieldPanel('price_text'),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Top Navigation Menu"
        verbose_name_plural = "Top Navigation Menus"


class TopNavMenuItem(ClusterableModel, Orderable):
    """Top navigation menu item"""
    menu = ParentalKey(
        'TopNavMenu',
        on_delete=models.CASCADE,
        related_name='top_nav_items'
    )
    title = models.CharField(max_length=100, help_text="Menu item title")
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Link to a page"
    )
    link_url = models.URLField(blank=True, help_text="Or link to an external URL")
    open_in_new_tab = models.BooleanField(default=False, help_text="Open link in new tab")
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        help_text="Font Awesome icon class (e.g., 'fa-home')"
    )
    show_dropdown_arrow = models.BooleanField(default=False, help_text="Show dropdown arrow icon")

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('open_in_new_tab'),
        FieldPanel('icon_class'),
        FieldPanel('show_dropdown_arrow'),
        InlinePanel('top_nav_submenu_items', label="Dropdown Items"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def has_submenu(self):
        return self.top_nav_submenu_items.exists()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Top Nav Item"
        verbose_name_plural = "Top Nav Items"
        ordering = ['sort_order']


class TopNavSubMenuItem(Orderable):
    """Top navigation dropdown item"""
    parent = ParentalKey(
        'TopNavMenuItem',
        on_delete=models.CASCADE,
        related_name='top_nav_submenu_items'
    )
    title = models.CharField(max_length=100, help_text="Submenu item title")
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Link to a page"
    )
    link_url = models.URLField(blank=True, help_text="Or link to an external URL")
    open_in_new_tab = models.BooleanField(default=False, help_text="Open link in new tab")

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('open_in_new_tab'),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Top Nav Dropdown Item"
        verbose_name_plural = "Top Nav Dropdown Items"
        ordering = ['sort_order']


# DEPRECATED - Use HeaderMenu instead
class MiddleNavMenu(ClusterableModel):
    """Middle navigation bar menu - DEPRECATED"""
    title = models.CharField(max_length=100, help_text="Menu title (for admin reference only)")
    show_request_quote = models.BooleanField(default=True, help_text="Show 'Request a quote' button")
    request_quote_text = models.CharField(max_length=50, default="Request a quote", help_text="Request quote button text")
    request_quote_link = models.URLField(blank=True, help_text="Request quote button link")
    show_client_portal = models.BooleanField(default=True, help_text="Show 'Client Portal' button")
    client_portal_text = models.CharField(max_length=50, default="Client Portal", help_text="Client portal button text")
    client_portal_link = models.URLField(blank=True, default="/admin/", help_text="Client portal button link")

    panels = [
        FieldPanel('title'),
        InlinePanel('middle_nav_items', label="Middle Nav Items"),
        FieldPanel('show_request_quote'),
        FieldPanel('request_quote_text'),
        FieldPanel('request_quote_link'),
        FieldPanel('show_client_portal'),
        FieldPanel('client_portal_text'),
        FieldPanel('client_portal_link'),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Middle Navigation Menu"
        verbose_name_plural = "Middle Navigation Menus"


class MiddleNavMenuItem(Orderable):
    """Middle navigation menu item"""
    menu = ParentalKey(
        'MiddleNavMenu',
        on_delete=models.CASCADE,
        related_name='middle_nav_items'
    )
    title = models.CharField(max_length=100, help_text="Menu item title")
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Link to a page"
    )
    link_url = models.URLField(blank=True, help_text="Or link to an external URL")
    open_in_new_tab = models.BooleanField(default=False, help_text="Open link in new tab")

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('open_in_new_tab'),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Middle Nav Item"
        verbose_name_plural = "Middle Nav Items"
        ordering = ['sort_order']


# DEPRECATED - Use HeaderMenu instead
class BottomNavMenu(ClusterableModel):
    """Bottom navigation bar menu - DEPRECATED"""
    title = models.CharField(max_length=100, help_text="Menu title (for admin reference only)")

    panels = [
        FieldPanel('title'),
        InlinePanel('bottom_nav_items', label="Bottom Nav Items (ISO Standards)"),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Bottom Navigation Menu"
        verbose_name_plural = "Bottom Navigation Menus"


class BottomNavMenuItem(ClusterableModel, Orderable):
    """Bottom navigation menu item (ISO standards)"""
    menu = ParentalKey(
        'BottomNavMenu',
        on_delete=models.CASCADE,
        related_name='bottom_nav_items'
    )
    title = models.CharField(max_length=100, help_text="ISO Standard (e.g., 'ISO 9001')")
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Link to a page"
    )
    link_url = models.URLField(blank=True, help_text="Or link to an external URL")
    show_dropdown_arrow = models.BooleanField(default=False, help_text="Show dropdown arrow")

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('show_dropdown_arrow'),
        InlinePanel('bottom_nav_submenu_items', label="Dropdown Items"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def has_submenu(self):
        return self.bottom_nav_submenu_items.exists()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Bottom Nav Item"
        verbose_name_plural = "Bottom Nav Items"
        ordering = ['sort_order']


class BottomNavSubMenuItem(Orderable):
    """Bottom navigation dropdown item"""
    parent = ParentalKey(
        'BottomNavMenuItem',
        on_delete=models.CASCADE,
        related_name='bottom_nav_submenu_items'
    )
    title = models.CharField(max_length=100, help_text="Submenu item title")
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Link to a page"
    )
    link_url = models.URLField(blank=True, help_text="Or link to an external URL")
    open_in_new_tab = models.BooleanField(default=False, help_text="Open link in new tab")

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('open_in_new_tab'),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Bottom Nav Dropdown Item"
        verbose_name_plural = "Bottom Nav Dropdown Items"
        ordering = ['sort_order']


@register_snippet
class FooterMenu(ClusterableModel):
    """Footer menu with multiple columns"""
    title = models.CharField(max_length=100, help_text="Footer menu title (for admin reference only)")

    panels = [
        FieldPanel('title'),
        InlinePanel('footer_columns', label="Footer Columns"),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Footer Menu"
        verbose_name_plural = "Footer Menus"


class FooterColumn(ClusterableModel, Orderable):
    """Individual footer column"""
    footer_menu = ParentalKey(
        'FooterMenu',
        on_delete=models.CASCADE,
        related_name='footer_columns'
    )
    title = models.CharField(max_length=100, help_text="Column heading")

    panels = [
        FieldPanel('title'),
        InlinePanel('column_links', label="Links"),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Footer Column"
        verbose_name_plural = "Footer Columns"


class FooterLink(Orderable):
    """Individual footer link"""
    column = ParentalKey(
        'FooterColumn',
        on_delete=models.CASCADE,
        related_name='column_links'
    )
    title = models.CharField(max_length=100, help_text="Link text")
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Link to a page"
    )
    link_url = models.URLField(blank=True, help_text="Or link to an external URL")
    open_in_new_tab = models.BooleanField(default=False, help_text="Open link in new tab")

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('open_in_new_tab'),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Footer Link"
        verbose_name_plural = "Footer Links"


@register_setting
class ColorThemeSettings(BaseSiteSetting):
    """Site-wide color theme customization"""

    # Primary Colors
    primary_color = models.CharField(
        max_length=7,
        default='#0066cc',
        help_text="Main brand color (e.g., #0066cc)"
    )
    secondary_color = models.CharField(
        max_length=7,
        default='#28a745',
        help_text="Secondary brand color (e.g., #28a745)"
    )
    accent_color = models.CharField(
        max_length=7,
        default='#ff6b6b',
        help_text="Accent/highlight color (e.g., #ff6b6b)"
    )

    # Navbar Colors (Global - applies to all navbars if specific ones not set)
    navbar_background = models.CharField(
        max_length=7,
        default='#ffffff',
        help_text="Default navbar background color (fallback for all navbars)"
    )
    navbar_text_color = models.CharField(
        max_length=7,
        default='#333333',
        help_text="Default navbar text color (fallback for all navbars)"
    )
    navbar_hover_color = models.CharField(
        max_length=7,
        default='#0066cc',
        help_text="Default navbar link hover color (fallback for all navbars)"
    )
    navbar_active_color = models.CharField(
        max_length=7,
        default='#0066cc',
        help_text="Default active navbar link color (fallback for all navbars)"
    )

    # Top Navigation Bar Colors
    top_nav_background = models.CharField(
        max_length=7,
        default='#f5f5f5',
        blank=True,
        help_text="Top navbar background color (Why Choose Us, Resources, etc.)"
    )
    top_nav_text_color = models.CharField(
        max_length=7,
        default='#333333',
        blank=True,
        help_text="Top navbar text color"
    )
    top_nav_hover_color = models.CharField(
        max_length=7,
        default='#0066cc',
        blank=True,
        help_text="Top navbar link hover color"
    )

    # Middle Navigation Bar Colors
    middle_nav_background = models.CharField(
        max_length=7,
        default='#ffffff',
        blank=True,
        help_text="Middle navbar background color (Logo, ISO Certification, etc.)"
    )
    middle_nav_text_color = models.CharField(
        max_length=7,
        default='#333333',
        blank=True,
        help_text="Middle navbar text color"
    )
    middle_nav_hover_color = models.CharField(
        max_length=7,
        default='#0066cc',
        blank=True,
        help_text="Middle navbar link hover color"
    )

    # Bottom Navigation Bar Colors
    bottom_nav_background = models.CharField(
        max_length=7,
        default='#f8f9fa',
        blank=True,
        help_text="Bottom navbar background color (ISO Standards)"
    )
    bottom_nav_text_color = models.CharField(
        max_length=7,
        default='#333333',
        blank=True,
        help_text="Bottom navbar text color"
    )
    bottom_nav_hover_color = models.CharField(
        max_length=7,
        default='#0066cc',
        blank=True,
        help_text="Bottom navbar link hover color"
    )

    # Footer Colors
    footer_background = models.CharField(
        max_length=7,
        default='#2c3e50',
        help_text="Footer background color"
    )
    footer_text_color = models.CharField(
        max_length=7,
        default='#ecf0f1',
        help_text="Footer text color"
    )
    footer_link_color = models.CharField(
        max_length=7,
        default='#ffffff',
        help_text="Footer link color"
    )
    footer_link_hover_color = models.CharField(
        max_length=7,
        default='#3498db',
        help_text="Footer link hover color"
    )

    # Button Colors
    button_primary_bg = models.CharField(
        max_length=7,
        default='#0066cc',
        help_text="Primary button background"
    )
    button_primary_text = models.CharField(
        max_length=7,
        default='#ffffff',
        help_text="Primary button text color"
    )
    button_primary_hover = models.CharField(
        max_length=7,
        default='#0052a3',
        help_text="Primary button hover color"
    )

    button_secondary_bg = models.CharField(
        max_length=7,
        default='#6c757d',
        help_text="Secondary button background"
    )
    button_secondary_text = models.CharField(
        max_length=7,
        default='#ffffff',
        help_text="Secondary button text color"
    )
    button_secondary_hover = models.CharField(
        max_length=7,
        default='#5a6268',
        help_text="Secondary button hover color"
    )

    # Link Colors
    link_color = models.CharField(
        max_length=7,
        default='#0066cc',
        help_text="Default link color"
    )
    link_hover_color = models.CharField(
        max_length=7,
        default='#004999',
        help_text="Link hover color"
    )

    # Background Colors
    body_background = models.CharField(
        max_length=7,
        default='#f8f9fa',
        help_text="Body background color"
    )
    section_background = models.CharField(
        max_length=7,
        default='#ffffff',
        help_text="Section background color"
    )

    # Border & Divider Colors
    border_color = models.CharField(
        max_length=7,
        default='#dee2e6',
        help_text="Border and divider color"
    )

    # Text Colors
    heading_color = models.CharField(
        max_length=7,
        default='#212529',
        help_text="Heading text color"
    )
    body_text_color = models.CharField(
        max_length=7,
        default='#333333',
        help_text="Body text color"
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('primary_color', widget=ColorPickerWidget),
            FieldPanel('secondary_color', widget=ColorPickerWidget),
            FieldPanel('accent_color', widget=ColorPickerWidget),
        ], heading="Brand Colors"),

        MultiFieldPanel([
            FieldPanel('navbar_background', widget=ColorPickerWidget),
            FieldPanel('navbar_text_color', widget=ColorPickerWidget),
            FieldPanel('navbar_hover_color', widget=ColorPickerWidget),
            FieldPanel('navbar_active_color', widget=ColorPickerWidget),
        ], heading="Navbar Colors (Global Defaults)"),

        MultiFieldPanel([
            FieldPanel('top_nav_background', widget=ColorPickerWidget),
            FieldPanel('top_nav_text_color', widget=ColorPickerWidget),
            FieldPanel('top_nav_hover_color', widget=ColorPickerWidget),
        ], heading="Top Navigation Bar Colors"),

        MultiFieldPanel([
            FieldPanel('middle_nav_background', widget=ColorPickerWidget),
            FieldPanel('middle_nav_text_color', widget=ColorPickerWidget),
            FieldPanel('middle_nav_hover_color', widget=ColorPickerWidget),
        ], heading="Middle Navigation Bar Colors"),

        MultiFieldPanel([
            FieldPanel('bottom_nav_background', widget=ColorPickerWidget),
            FieldPanel('bottom_nav_text_color', widget=ColorPickerWidget),
            FieldPanel('bottom_nav_hover_color', widget=ColorPickerWidget),
        ], heading="Bottom Navigation Bar Colors"),

        MultiFieldPanel([
            FieldPanel('footer_background', widget=ColorPickerWidget),
            FieldPanel('footer_text_color', widget=ColorPickerWidget),
            FieldPanel('footer_link_color', widget=ColorPickerWidget),
            FieldPanel('footer_link_hover_color', widget=ColorPickerWidget),
        ], heading="Footer Colors"),

        MultiFieldPanel([
            FieldPanel('button_primary_bg', widget=ColorPickerWidget),
            FieldPanel('button_primary_text', widget=ColorPickerWidget),
            FieldPanel('button_primary_hover', widget=ColorPickerWidget),
            FieldPanel('button_secondary_bg', widget=ColorPickerWidget),
            FieldPanel('button_secondary_text', widget=ColorPickerWidget),
            FieldPanel('button_secondary_hover', widget=ColorPickerWidget),
        ], heading="Button Colors"),

        MultiFieldPanel([
            FieldPanel('link_color', widget=ColorPickerWidget),
            FieldPanel('link_hover_color', widget=ColorPickerWidget),
        ], heading="Link Colors"),

        MultiFieldPanel([
            FieldPanel('body_background', widget=ColorPickerWidget),
            FieldPanel('section_background', widget=ColorPickerWidget),
            FieldPanel('border_color', widget=ColorPickerWidget),
            FieldPanel('heading_color', widget=ColorPickerWidget),
            FieldPanel('body_text_color', widget=ColorPickerWidget),
        ], heading="Background & Text Colors"),
    ]

    class Meta:
        verbose_name = "Color Theme Settings"
