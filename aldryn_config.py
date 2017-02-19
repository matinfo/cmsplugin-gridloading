# -*- coding: utf-8 -*-
from aldryn_client import forms


class Form(forms.BaseForm):

    gridloading_shortname = forms.CharField('Site shortname')

    def to_settings(self, data, settings):
        settings['GRIDLOADING_SHORTNAME'] = data['gridloading_shortname']
        return settings
