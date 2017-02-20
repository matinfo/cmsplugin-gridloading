=====================
cmsplugin-gridloading
=====================

Cascading grid layout (image or/and text) wall plugin using Masonry (http://masonry.desandro.com) library, + grid loading effects from AnimOnScroll by http://www.codrops.com.

Offer Image ratios selection and the choice of 8 loading CSS effect : Opacity, Move Up, Scale Up, Fall Perspective, Fly, Flip, Helix, Pop Up. 

Posibility to upload Image by Image or by group of images by selecting a Folder using Django Filer. 

Grid Loading is build on the principle of plugin-in-plugin provided by django-cms since version 3.0.

Useful to create photowall for example!

Support multi Wall by page.

See original demos: https://tympanus.net/Development/GridLoadingEffects/


.. image:: https://travis-ci.org/matinfo/cmsplugin-gridloading.svg?branch=master
    :target: https://travis-ci.org/matinfo/cmsplugin-gridloading

.. image:: https://img.shields.io/coveralls/matinfo/cmsplugin-gridloading.svg
  :target: https://coveralls.io/r/matinfo/cmsplugin-gridloading


Grid Loading is build on the principle of plugin-in-plugin provided by django-cms
since version 3.0.

Installation
============

::

    pip install cmsplugin-gridloading

Add ``cmsplugin_gridloading`` to ``INSTALLED_APPS``.
