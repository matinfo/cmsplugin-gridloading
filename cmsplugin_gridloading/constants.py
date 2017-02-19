# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.utils.translation import ugettext_lazy as _



EFFECT_DEFAULT = 'opacity'
EFFECT_CHOICES = [
    (EFFECT_DEFAULT, _('Opacity')),
    ('move-up', _('Move Up')),
    ('scale-up', _('Scale Up')),
    ('fall-perspective', _('Fall Perspective')),
    ('fly', _('Fly')),
    ('flip', _('Flip')),
    ('helix', _('Helix')),
    ('pop-up', _('Pop Up')),
]

TARGET_CHOICES = (
    ('_blank', _('Open in new window')),
    ('_self', _('Open in same window')),
    ('_parent', _('Delegate to parent')),
    ('_top', _('Delegate to top')),
)

ASPECT_RATIOS = (
    (4, 3),
    (16, 9),
    (16, 10),
    (21, 9),
)

ASPECT_RATIOS_REVERSED = ([(y, x) for x, y in ASPECT_RATIOS])

ASPECT_RATIO_CHOICES = (
    tuple([
        ('{0}x{1}'.format(1, 1), '{0}x{1}'.format(1, 1))
    ]) + tuple([
        ('{0}x{1}'.format(x, y), '{0}x{1}'.format(x, y))
        for x, y in ASPECT_RATIOS
    ]) + tuple([
        ('{0}x{1}'.format(x, y), '{0}x{1}'.format(x, y))
        for x, y in ASPECT_RATIOS_REVERSED
    ]))

SIZE_CHOICES = (
    ('lg', _('Large'),),
    ('md', _('Medium'),),
    ('sm', _('Small'),),
    ('xs', _('Extra Small'),),
)

DEVICES = (
    {
        'identifier': 'xs',
        'name': _('Mobile phones'),
        'width': 768,
        'width_gutter': 750,
        'icon': 'mobile-phone',
    },
    {
        'identifier': 'sm',
        'name': _('Tablets'),
        'width': 768,
        'width_gutter': 750,
        'icon': 'tablet',
    },
    {
        'identifier': 'md',
        'name': _('Laptops'),
        'width': 992,
        'width_gutter': 970,
        'icon': 'laptop',
    },
    {
        'identifier': 'lg',
        'name': _('Large desktops'),
        'width': 1200,
        'width_gutter': 1170,
        'icon': 'desktop',
    },
)

for device in DEVICES:
    identifier = device['identifier']
    device['long_description'] = '{name} (<{width}px)'.format(**device)
    device['size_name'] = dict(SIZE_CHOICES).get(identifier)
