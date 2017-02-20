# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import collections
from functools import partial


import django.forms.models
from django.db import models
from django.utils.html import strip_tags
from django.utils.translation import ugettext, ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from cms.models.fields import PageField


from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.folder import FilerFolderField
from filer.fields.image import FilerImageField

import djangocms_text_ckeditor.fields
from djangocms_attributes_field.fields import AttributesField

from . import compat, constants
from .utils import get_additional_effect


if compat.LTE_DJANGO_1_6:
    # related_name='%(app_label)s_%(class)s' does not work on  Django 1.6
    CMSPluginField = partial(
        models.OneToOneField,
        to=CMSPlugin,
        related_name='+',
        parent_link=True,
    )
else:
    # Once djangoCMS < 3.3.1 support is dropped
    # Remove the explicit cmsplugin_ptr field declarations
    CMSPluginField = partial(
        models.OneToOneField,
        to=CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )



class GridloadingPlugin(CMSPlugin):
    """
    Gridloading: "Wrapper" Model
    """

    effect = models.CharField(
        verbose_name=_('CSS Effect'),
        choices=constants.EFFECT_CHOICES + get_additional_effect(),
        default=constants.EFFECT_DEFAULT,
        max_length=255,
    )
    aspect_ratio = models.CharField(
        verbose_name=_('Aspect ratio'),
        choices=constants.ASPECT_RATIO_CHOICES,
        blank=True,
        default='',
        max_length=255,
        help_text=_('Determines width and height of the image '
                    'according to the selected ratio.'),
    )
    extra_styles = models.CharField(
        _('Extra styles'), max_length=50, blank=True,
        help_text=_('An arbitrary string of CSS classes to add'))

    cmsplugin_ptr = CMSPluginField()

    def __str__(self):
        data = django.forms.models.model_to_dict(self)
        data.update(dict(
            effect_label=_('Effect'),
            aspect_ratio_label=_('Aspect ratio'),
        ))
        fields = [
            'effect',
            'aspect_ratio',
        ]
        return ', '.join([
            u'{key}: {value}'.format(
                key=data['{}_label'.format(field)],
                value=data[field]
            ) for field in fields
        ])

    def srcset(self):
        # more or less copied from image plugin.
        # TODO: replace with generic sizes/srcset solution
        items = collections.OrderedDict()
        if self.aspect_ratio:
            aspect_width, aspect_height = tuple([int(i) for i in self.aspect_ratio.split('x')])
        else:
            aspect_width, aspect_height = None, None
        for device in constants.DEVICES:
            width = device['width_gutter']  # TODO: should this should be based on the containing col size?
            width_tag = str(width)
            if aspect_width is not None and aspect_height is not None:
                height = int(float(width)*float(aspect_height)/float(aspect_width))
                crop = True
            else:
                height = 0
                crop = False
            items[device['identifier']] = {
                'size': (width, height),
                'size_str': '{}x{}'.format(width, height),
                'width_str': '{}w'.format(width),
                # 'subject_location': self.file.subject_location,
                'upscale': True,
                'crop': crop,
                'aspect_ratio': (aspect_width, aspect_height),
                'width_tag': width_tag,
            }

        return items



class GridloadingItemPlugin(CMSPlugin):
    """
    Gridloading: "Item" Model
    """
    cmsplugin_ptr = CMSPluginField()

    image = FilerImageField(verbose_name=_('Image'), blank=True, null=True)
    content = HTMLField(verbose_name=_('Content'), blank=True, default='')
    link_url = models.URLField(_("Link"), blank=True, null=True)
    link_page = PageField(
        verbose_name=_('Page'),
        blank=True,
        null=True,
        help_text=_("A link to a page has priority over a text link.")
    )
    link_target = models.CharField(
        verbose_name=_("Target"),
        max_length=100,
        blank=True,
        choices=constants.TARGET_CHOICES,
    )
    link_text = models.CharField(
        verbose_name=_('Link text'),
        max_length=200,
        blank=True
    )

    def __str__(self):
        image_text = content_text = ''

        if self.image_id:
            image_text = u'%s' % (self.image.name or self.image.original_filename)
        if self.content:
            text = strip_tags(self.content).strip()
            if len(text) > 100:
                content_text = u'%s...' % text[:100]
            else:
                content_text = u'%s' % text

        if image_text and content_text:
            return u'%s (%s)' % (image_text, content_text)
        else:
            return image_text or content_text


    def copy_relations(self, oldinstance):
        self.image_id = oldinstance.image_id
        self.link_page_id = oldinstance.link_page_id

    def get_link(self):
        link = self.link_url or u''

        if self.link_page_id:
            link = self.link_page.get_absolute_url()
        return link


class GridloadingItemFolderPlugin(CMSPlugin):
    """
    Gridloading: "Image folder" Model
    """
    cmsplugin_ptr = CMSPluginField()

    folder = FilerFolderField(verbose_name=_('Folder'), \
        help_text=_('Show all the image(s) include in the selected folder.'))

    def __str__(self):
        if self.folder_id:
            return self.folder.pretty_logical_path
        else:
            return _('<folder is missing>')

    def copy_relations(self, oldinstance):
        self.folder_id = oldinstance.folder_id
