# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields
import djangocms_text_ckeditor.fields
import filer.fields.folder
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='GridloadingItemFolderPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='cmsplugin_gridloading_gridloadingitemfolderplugin', to='cms.CMSPlugin', auto_created=True, primary_key=True, serialize=False, parent_link=True)),
                ('folder', filer.fields.folder.FilerFolderField(help_text='Show all the image(s) include in the selected folder.', to='filer.Folder', verbose_name='Folder')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GridloadingItemPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='cmsplugin_gridloading_gridloadingitemplugin', to='cms.CMSPlugin', auto_created=True, primary_key=True, serialize=False, parent_link=True)),
                ('content', djangocms_text_ckeditor.fields.HTMLField(default='', verbose_name='Content', blank=True)),
                ('link_url', models.URLField(null=True, verbose_name='Link', blank=True)),
                ('link_target', models.CharField(verbose_name='Target', max_length=100, blank=True, choices=[('_blank', 'Open in new window'), ('_self', 'Open in same window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')])),
                ('image', filer.fields.image.FilerImageField(to='filer.Image', null=True, verbose_name='Image', blank=True)),
                ('link_page', cms.models.fields.PageField(help_text='A link to a page has priority over a text link.', to='cms.Page', null=True, verbose_name='Page', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GridloadingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='cmsplugin_gridloading_gridloadingplugin', to='cms.CMSPlugin', auto_created=True, primary_key=True, serialize=False, parent_link=True)),
                ('effect', models.CharField(default='opacity', max_length=255, verbose_name='Loading effect', choices=[('opacity', 'Opacity'), ('move-up', 'Move Up'), ('scale-up', 'Scale Up'), ('fall-perspective', 'Fall Perspective'), ('fly', 'Fly'), ('flip', 'Flip'), ('helix', 'Helix'), ('pop-up', 'Pop Up')])),
                ('aspect_ratio', models.CharField(help_text='Determines width and height of the image according to the selected ratio. All images will be with same size. Not select ratio to maintain portrait/landscape of image.', default='', choices=[('1x1', '1x1'), ('4x3', '4x3'), ('16x9', '16x9'), ('16x10', '16x10'), ('21x9', '21x9'), ('3x4', '3x4'), ('9x16', '9x16'), ('10x16', '10x16'), ('9x21', '9x21')], verbose_name='Aspect ratio', blank=True, max_length=255)),
                ('extra_styles', models.CharField(help_text='An arbitrary string of CSS classes to add', verbose_name='Extra styles', blank=True, max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
