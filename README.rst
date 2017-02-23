=====================
cmsplugin-gridloading
=====================

**django CMS Grid Loading** is a set of plugins for `django CMS <http://django-cms.org>`_
that allow you to publish Cascading Grid layout (image or text block)
using `Masonry <http://masonry.desandro.com>`_ wall library, plus grid loading effects
with `AnimOnScroll <http://www.codrops.com>`_.

Possibility to set ratio for images by wall. The wall of 3 columns is full responsive.

Possibility to choose the loading of blocs from 8 predefined effect: Opacity,
Move Up, Scale Up, Fall Perspective, Fly, Flip, Helix, Pop Up. 

If you select image by image, in this case the ``content`` become the overlay
on mouse hover of the image, otherwise ``content`` become a text bloc.

Image item permit to add link and corresponding target.

The ``content`` is added using the Django CMS default rich text editor.

It uses files managed by `Django Filer <https://github.com/divio/django-filer>`_.
The plugins allow you to select a single image by image or an entire folder of images.

This addon is compatible with `Divio Cloud <http://divio.com>`_ and is also available on the
`django CMS Marketplace <https://marketplace.django-cms.org/en/addons/browse/cmsplugin-gridloading/>`_
for easy installation.

Grid Loading is built on the principle of plugin-in-plugin provided by django-cms
since version 3.0.

.. image:: example.png

Useful to create photo wall for example.

To see all grid loading effects: https://tympanus.net/Development/GridLoadingEffects/

Contributing
============

This is a an open-source project. We'll be delighted to receive your
feedback in the form of issues and pull requests. Before submitting your
pull request, please review django-cms `contribution guidelines
<http://docs.django-cms.org/en/latest/contributing/index.html>`_.


Documentation
=============

See ``REQUIREMENTS`` in the `setup.py <https://github.com/divio/djangocms-audio/blob/master/setup.py>`_
file for additional dependencies:

* Python 2.7, 3.3 or higher
* Django 1.8 or higher
* Django Filer 1.2.4 or higher

Make sure `django Filer <http://django-filer.readthedocs.io/en/latest/installation.html>`_
is installed and configured appropriately.


Installation
------------

For a manual install:

* run ``pip install cmsplugin-gridloading``
* add ``cmsplugin_gridloading`` to your ``INSTALLED_APPS``
* run ``python manage.py migrate cmsplugin_gridloading``


Configuration
-------------

Note that the provided templates are very minimal by design. You are encouraged
to adapt and override them to your project's requirements.

You can provide additional effect choices by adding a ``GRIDLOADING_EFFECTS`` setting::

    GRIDLOADING_EFFECTS = [
        ('new-css3-effect', _('New CSS 3 Effect')),
    ]

Your CSS effect need setup for example like this::

.. code-block:: css

    .gridloading.new-css3-effect {
        ...
    }
