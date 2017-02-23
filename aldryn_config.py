# -*- coding: utf-8 -*-
from aldryn_client import forms


class Form(forms.BaseForm):

    gridloading_effects = forms.CharField('List of additional grid loading effects (comma separated)', required=False)

    def to_settings(self, data, settings):
        settings['GRIDLOADING_EFFECTS'] = data['gridloading_effects']
        return settings
