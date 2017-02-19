# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import filer.fields.folder
import cms.models.fields
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='GridloadingItemFolderPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, related_name='cmsplugin_gridloading_gridloadingitemfolderplugin', to='cms.CMSPlugin')),
                ('folder', filer.fields.folder.FilerFolderField(help_text='Show all the image(s) include in the selected folder.', verbose_name='Folder', to='filer.Folder')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GridloadingItemPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, related_name='cmsplugin_gridloading_gridloadingitemplugin', to='cms.CMSPlugin')),
                ('content', djangocms_text_ckeditor.fields.HTMLField(blank=True, default='', verbose_name='Content')),
                ('link_url', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('link_target', models.CharField(blank=True, max_length=100, verbose_name='Target', choices=[('_blank', 'Open in new window'), ('_self', 'Open in same window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')])),
                ('link_text', models.CharField(blank=True, max_length=200, verbose_name='Link text')),
                ('link_page', cms.models.fields.PageField(blank=True, help_text='A link to a page has priority over a text link.', null=True, verbose_name='Page', to='cms.Page')),('image', filer.fields.image.FilerImageField(blank=True, null=True, verbose_name='Image', to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GridloadingPlugin',
            fields=[
                ('effect', models.CharField(max_length=255, default='opacity', verbose_name='CSS Effect', choices=[('opacity', 'Opacity'), ('move-up', 'Move Up'), ('scale-up', 'Scale Up'), ('fall-perspective', 'Fall Perspective'), ('fly', 'Fly'), ('flip', 'Flip'), ('helix', 'Helix'), ('pop-up', 'Pop Up')])),
                ('aspect_ratio', models.CharField(blank=True, max_length=255, choices=[('1x1', '1x1'), ('4x3', '4x3'), ('16x9', '16x9'), ('16x10', '16x10'), ('21x9', '21x9'), ('3x4', '3x4'), ('9x16', '9x16'), ('10x16', '10x16'), ('9x21', '9x21')], help_text='Determines width and height of the image according to the selected ratio.', default='', verbose_name='Aspect ratio')),
                ('extra_styles', models.CharField(blank=True, help_text='An arbitrary string of CSS classes to add', max_length=50, verbose_name='Extra styles')),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, related_name='cmsplugin_gridloading_gridloadingplugin', to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
