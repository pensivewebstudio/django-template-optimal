from django.db import models


# Site Navigation -----------------

class NavLogo(models.Model):
    nav_logo_fav_class = models.CharField(max_length=255, null=True)
    nav_logo_text = models.CharField(max_length=255, null=True)

# ---------------------------------


# Site header ---------------------

class SiteHeader(models.Model):
    site_header_image_url = models.CharField(max_length=2083)
    site_header_title = models.CharField(max_length=255)
    site_header_text = models.CharField(max_length=255)
# ---------------------------------


# About Page Section --------------

class AboutHeader(models.Model):
    about_header_title = models.CharField(max_length=255)
    about_header_text = models.CharField(max_length=255)


class AboutItem(models.Model):
    about_Item_fav_class = models.CharField(max_length=255)
    about_item_title = models.CharField(max_length=255)
    about_item_text = models.CharField(max_length=255)


# ---------------------------------


# Services Page Section -----------

class ServicesHeader(models.Model):
    services_header_title = models.CharField(max_length=255)
    services_header_text = models.CharField(max_length=255)


class ServicesItem(models.Model):
    services_Item_fav_class = models.CharField(max_length=255)
    services_item_title = models.CharField(max_length=255)
    services_item_text = models.CharField(max_length=255)


# ---------------------------------


# Call to Action Page Section -----

class CTA(models.Model):
    cta_image_url = models.CharField(max_length=2083)
    cta_title = models.CharField(max_length=255)
    cta_text = models.CharField(max_length=255)


# ---------------------------------


# Testimonials Page Section -------

class TestimonialsHeader(models.Model):
    testimonials_header_title = models.CharField(max_length=255)
    testimonials_header_text = models.CharField(max_length=255)


class Testimonial(models.Model):
    testimonial_image_url = models.CharField(max_length=2083)
    testimonial_title = models.CharField(max_length=255)
    testimonial_text = models.CharField(max_length=255)


# ---------------------------------


# Gallery Page Section ------------

# Gallery Header
class GalleryHeader(models.Model):
    gallery_header_title = models.CharField(max_length=255)
    gallery_header_text = models.CharField(max_length=255)


# Gallery Item
class GalleryItem(models.Model):
    gallery_item_image_url = models.CharField(max_length=2083)

# ---------------------------------

# Slider Page Section -------------


# slider Item
class SliderItem(models.Model):
    slider_image_url = models.CharField(max_length=2083)

# ---------------------------------


# Contact Page Section ------------


# Contact Header
class ContactHeader(models.Model):
    contact_header_title = models.CharField(max_length=255)
    contact_header_text = models.CharField(max_length=255)


class ContactCTA(models.Model):
    contact_cta = models.CharField(max_length=255)

# ---------------------------------
