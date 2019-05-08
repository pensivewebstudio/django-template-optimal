
<h2>Django and Bootstrap 4</h2>

This repository is a template for a one-page style website using Bootstrap 4 for the front end and Django for the back end. It serves as a template reference for different bootstrap 4 layouts, an example of how Django can be used to create simple, one-page style web applications or to use as a theme for your site as is. The project comes with dummy content in the SQLite database which can be replaced via the admin URL by your own contact for a ready to use site. You can see a live demo of the template at: [github-project-optimal.pensivewebstudio.com](http://www.github-project-optimal.pensivewebstudio.com).

You can see a live demo of a site that I build using this template at: [portfolio-item-optimal-structure.pensivewebstudio.com/](http://www.portfolio-item-optimal-structure.pensivewebstudio.com/).

#The Front-End: 

<h3>Structure of the Layouts</h3>

The implementation is a single page design where each html article represents a page of the website, #page-about, #page-services etc.… .. . I’ve named the articles #page-one, #page-two and so on to make the layout generic assuming you would want to rename them as you wish. For example, you could rename the article below: #page-about, if you wanted to make it your about page.

```

  <!-- #page-one -->
  <article id="page-one" class="page-icons page-section vertical-padding">

    <header class="page-section-header container">
      <h2 class="page-section-title display-4 pt-4 text-center">Page Section Title</h2>
      <p class="page-section-text lead mx-md-5">Page Section Text: Lorem Ipsum is simply dummy text of the
        printing and typesetting industry which will be replaced with text one you and your business upon completion
        of your site. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
        labore et dolore magna aliqua.</p>
    </header>

    <div class="layout-iconcolumns container vertical-padding">
      <div class="row text-center">

        <section class="col-md-4 my-3">
          <div class="icon-small layout-icon">
            <i class="fas fa-circle"></i>
          </div>
          <h3 class="layout-title">Layout Title</h3>
          <p class="layout-text">Layout Text: Lorem ipsum dolor sit amet consectetur, adipisicing elit. Perspiciatis doloremque
            possimus dignissimos illo praesentium
            id consectetur tempora dolorum! Vel sapiente vitae, deserunt minima et rem accusamus?</p>
        </section>

        <section class="col-md-4 my-3">
          <div class="icon-small layout-icon">
            <i class="fas fa-square"></i>
          </div>
          <h3 class="layout-title">Layout Title</h3>
          <p class="layout-text">Layout Text: Dolorem repudiandae ipsa fugit distinctio modi earum dicta eum tenetur, vel temporibus
            laudantium totam libero
            odit ex labore commodi maiores molestias. Quo, hic maxime. Accusantium impedit dolorem cum error?</p>
        </section>

        <section class="col-md-4 my-3">
          <div class="icon-small layout-icon">
            <i class="fas fa-circle"></i>
          </div>
          <h3 class="layout-title">Layout Title</h3>
          <p class="layout-text">Layout Text: Et, alias asperiores? Repellat repudiandae, eum temporibus quibusdam iure, recusandae
            illo nesciunt, doloremque
            eligendi maiores tempora eos aliquid minus iusto ipsum facere. Minus, vitae autem dolores vero dolore?</p>
        </section>

      </div>
    </div>

  </article>
  <!-- #page-one 
------------------------------------------------------------>

```

Most layouts (not the floater layout) also have an optional `<header>`. They should be self-explanatory.

<h3>The Back-End</h3>

<h3>Structure of the Django Project</h3>


The implementation is a single page design where the primary funtionallity of the project is governed by one app, the “home” app. The static files used by the app are stored in a static folder within this app. The project uses for loops within the templates to display objects from the database allowing you to add and display as many of each type of object as you wish.

```

<!-- #page-services -->
<article id="page-services" class="page-icons page-section vertical-padding">
  {% for services_header in services_header.all %}
    <header class="page-section-header container">
      <h2 class="page-section-title display-4 pt-4 text-center">{{ services_header.services_header_title }}</h2>
      <p class="page-section-text lead mx-md-5">{{ services_header.services_header_text }}</p>
    </header>
  {% endfor %}

  <div class="layout-iconcolumns container vertical-padding">
    <div class="row text-center">
      {% for services_item in services_item.all %}
        <section class="col-md-4 my-3">
          <div class="icon layout-icon">
            <i class="{{ services_item.services_Item_fav_class }}"></i>
          </div>
          <h3 class="layout-title">{{ services_item.services_item_title }}</h3>
          <p class="layout-text">{{ services_item.services_item_text }}</p>
        </section>
      {% endfor %}
    </div>
  </div>

</article>
<!-- #page-services -->

```

<h3>Passing Object from the database.<h3>

I’ve passed all objects from the database to a single view function for simplicity:

```
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
    return render(request, 'home/index.html', dict1

```

<h3>Authors and Contributors</h3>

 Ray Villalobos: The front-end of this project is based on a template by Ray built for a LinkedIn learning course called [Bootstrap 4 Layouts: Responsive Single-Page Design](https://www.linkedin.com/learning/bootstrap-4-layouts-responsive-single-page-design/creating-a-bootstrap-4-layout?u=104). You can see a live demo of his project at: [raybo.org/bootstrap4layouts/](http://www.raybo.org/bootstrap4layouts/).
