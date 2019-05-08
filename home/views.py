from django.shortcuts import render
from .models import *


nav_logo = NavLogo.objects
site_header = SiteHeader.objects.all()
about_header = AboutHeader.objects.all()
about_item = AboutItem.objects.all()
services_header = ServicesHeader.objects.all()
services_item = ServicesItem.objects.all()
cta = CTA.objects.all()
testimonials_header = TestimonialsHeader.objects.all()
testimonials = Testimonial.objects.all()
gallery_header = GalleryHeader.objects.all()
gallery_items = GalleryItem.objects.all()
slider_item = SliderItem.objects.all()
contact_header = ContactHeader.objects.all()
contact_cta = ContactCTA.objects.all()

dict1 = {
         'nav_logo': nav_logo,
         'site_header': site_header,
         'about_header': about_header,
         'about_item': about_item,
         'services_header': services_header,
         'services_item': services_item,
         'cta': cta,
         'testimonials_header': testimonials_header,
         'testimonials': testimonials,
         'gallery_header': gallery_header,
         'gallery_items': gallery_items,
         'slider_item': slider_item,
         'contact_header': contact_header,
         }


def index(request):
    return render(request, 'home/index.html', dict1)