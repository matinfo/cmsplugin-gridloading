# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import GridloadingPlugin, GridloadingItemPlugin, GridloadingItemFolderPlugin


class GridloadingBase(CMSPluginBase):
    """
    Base Classes
    """
    module = _('Gridloading')


class GridloadingChildBase(GridloadingBase):
    """
    Base Child Plugin
    """
    require_parent = True
    parent_classes = ['GridloadingCMSPlugin']

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['image'] = instance.image
        return context

    def get_item_template(self, instance, name='item'):
        return 'cmsplugin_gridloading/plugins/{}.html'.format(name)

    def get_render_template(self, context, instance, placeholder):
        return self.get_item_template(instance=instance)


class GridloadingCMSPlugin(GridloadingBase):
    """
    Wrapper Plugin
    """
    name = _('Gridloading')
    model = GridloadingPlugin
    render_template = 'cmsplugin_gridloading/plugins/base.html'
    allow_children = True
    child_classes = [
        'GridloadingItemCMSPlugin',
        'GridloadingItemFolderCMSPlugin'
    ]

    fieldsets = (
        (None, {
            'fields': (
                'effect',
                'aspect_ratio',
                'extra_styles',
            )
        }),
    )


class GridloadingItemCMSPlugin(GridloadingChildBase):
    """
    Item Plugin
    """
    name = _('Gridloading item')
    model = GridloadingItemPlugin
    cache = False
    render_template = False
    allow_children = True

    fieldsets = (
        (None, {
            'fields': (
                'image',
                'content',
            )
        }),
        (_('Link settings'), {
            'classes': ('collapse',),
            'fields': (
                ('link_url', 'link_page'),
                ('link_target'),
            )
        }),
    )

    def get_render_template(self, context, instance, placeholder):
        return self.get_item_template(instance=instance, name='item')


class GridloadingItemFolderCMSPlugin(GridloadingChildBase):
    """
    Folder Plugin
    """
    name = _('Gridloading folder')
    model = GridloadingItemFolderPlugin
    cache = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['gridloading_template'] = self.get_item_template(instance=instance, \
            name='image_item')
        return context

    def get_render_template(self, context, instance, placeholder):
        return self.get_item_template(instance=instance, name='item_folder')


plugin_pool.register_plugin(GridloadingCMSPlugin)
plugin_pool.register_plugin(GridloadingItemCMSPlugin)
plugin_pool.register_plugin(GridloadingItemFolderCMSPlugin)

